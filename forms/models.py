from django.db import models
from django.contrib.auth.models import User


class Form(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=200,
        default="Student Registration Form"
    )

    def __str__(self):
        return self.title


class Response(models.Model):

    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name