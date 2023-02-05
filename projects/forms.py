from typing import List, Mapping, Any
from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields: List[str] = [
            "title",
            "featured_image",
            "description",
            "demo_link",
            "source_link",
            "tags",
        ]
        widgets: Mapping[str, Any] = {"tags": forms.CheckboxSelectMultiple()}

    def __init__(self, *arg, **kwargs):
        super(ProjectForm, self).__init__(*arg, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
