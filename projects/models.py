from typing import Tuple
from uuid import uuid4
from django.db import models
from users.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(
        to=Profile, null=True, blank=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField(to="Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "title"]

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list("owner__id", flat=True)
        return queryset

    @property
    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes: int = reviews.filter(value="up").count()
        total_votes: int = reviews.count()
        ratio: float = (up_votes / total_votes) * 100
        self.vote_total = total_votes
        self.vote_ratio = ratio
        self.save()

    @property
    def imageURL(self):
      try:
        url: str = self.featured_image.url   
      except:
        setattr(self, "featured_image", 'default.jpg')
        self.save()
        url: str = self.featured_image.url
      return url

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_TYPE: Tuple[Tuple[str]] = (("up", "Up Vote"), ("down", "Down Vote"))
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [["owner", "project"]]
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
