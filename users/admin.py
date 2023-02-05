from django.contrib import admin

# Register your models here.

from users.models import Profile

admin.site.register(model_or_iterable=Profile)
