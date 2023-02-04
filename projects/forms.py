from typing import List
from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields: List[str] = ["title", "description", "demo_link", "source_link", "tags"]
