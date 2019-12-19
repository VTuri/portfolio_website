from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    body = RichTextUploadingField(default="")
    technology = models.CharField(max_length=20)
    image_path = models.CharField(max_length=30, default="img/default_img.png")

    def __str__(self):
        return self.title
