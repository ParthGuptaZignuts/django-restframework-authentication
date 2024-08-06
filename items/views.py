from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from items.models import Items
from .serializer import ItemSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework.views import APIView
from django.urls import reverse

token_generator = PasswordResetTokenGenerator()

@api_view(['POST'])
@permission_classes([])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create_user(
            username = data['username'],
            password = data['password'],
            email    = data['email']
        )
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def login_user(request):
    data = request.data
    try:
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            subject = 'Login Notification'
            html_message = render_to_string('login_notification_email.html', {
                'user': user,
                'login_time': timezone.now().strftime('%d-%m-%Y'),
            })
            plain_message = strip_tags(html_message)

            send_mail(
                subject,
                plain_message,
                settings.EMAIL_HOST_USER, 
                [user.email],             
                fail_silently=False,
                html_message=html_message, 
            )

            return Response({"username": user.username, "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_items(request):
    try:
        paginator  = PageNumberPagination()
        paginator.page_size = 10
        items      = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def single_item(request, item_id):
    try:
        item       = Items.objects.get(id=item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    data = request.data
    try:
        item             = Items.objects.create(
        item_name        = data['item_name'],
        item_description = data['item_description']
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_item(request , item_id):
    data = request.data
    try:
        item                  = Items.objects.get(id=item_id)
        item.item_name        = data['item_name']
        item.item_description = data['item_description']
        item.save()
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, item_id):
    try:
        item = Items.objects.get(id=item_id)
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    data = request.data

    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if not user.check_password(old_password):
        return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    if not new_password:
        return Response({'error': 'New password cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user.set_password(new_password)
        user.save()
        login_url = "http://127.0.0.1:8000/api/login-user"
        subject = 'Password Changed Successfully'
        html_message = render_to_string('password_changed_notification_email.html', {
            'login_link': login_url
        })
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
            html_message=html_message,
        )
        return Response({'message': 'Password changed successfully. A notification email has been sent.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def request_password_reset(request):
    email = request.data.get('email')
    try:
        user       = User.objects.get(email=email)
        token      = token_generator.make_token(user)
        uid        = urlsafe_base64_encode(force_bytes(user.pk))
        reset_link = request.build_absolute_uri(reverse('reset-password', args=[uid, token]))

        subject      = 'Password Reset Request'
        html_message = render_to_string('password_reset_email.html', {
            'user': user,
            'reset_link': reset_link,
        })
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
            html_message=html_message,
        )
        return Response({'message': 'Password reset link sent successfully.'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
@permission_classes([])
def reset_password(request, uidb64, token):
    try:
        uid  = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            if not new_password:
                return Response({'error': 'New password cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            subject      = "Password Changed Successfully"

            html_message = render_to_string('password_reset_successfully.html')
            
            plain_message = strip_tags(html_message)

            send_mail(
                subject,
                plain_message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
                html_message=html_message,
            )

            return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)