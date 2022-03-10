from django.db import models
# remember to add the user model
from django.contrib.auth import get_user_model


class Snack(models.Model):
    # title field
# purchaser field
# description field
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='enter a description here')
    
    def __str__(self):
        return self.title
