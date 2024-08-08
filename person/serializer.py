from rest_framework import serializers
from .models import Person
import re

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError("Name should not contain numbers.")
        return value

    def validate_role(self, value):
        if value not in [Person.USER, Person.ADMIN]:
            raise serializers.ValidationError("Invalid role.")
        return value
