from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag

admin.site.register(model_or_iterable=Project)
admin.site.register(model_or_iterable=Review)
admin.site.register(model_or_iterable=Tag)
