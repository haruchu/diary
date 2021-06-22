from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

class Diary(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (str(self.title) + '(' + str(self.user) + ')' + str(self.created_date))



