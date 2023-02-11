from typing import List, Mapping, Any
from django import forms
from projects.models import Project, Review


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
        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields: List[str] = ["value", "body"]
        labels = {"value": "Place your vote", "body": "Add a comment with your vote"}

    def __init__(self, *arg, **kwargs):
        super(ReviewForm, self).__init__(*arg, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
