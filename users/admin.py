from django.contrib import admin

# Register your models here.

from users.models import Profile, Skill

admin.site.register(model_or_iterable=Profile)
admin.site.register(model_or_iterable=Skill)
