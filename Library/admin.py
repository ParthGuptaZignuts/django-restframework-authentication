from django.contrib import admin
from Library.models import Library , Book

admin.site.register([Library , Book])