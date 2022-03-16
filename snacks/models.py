from django.db import models
# remember to add the user model
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    # title field
# purchaser field
# description field
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='enter a description here')
    
    def __str__(self):
        return self.title, self.purchaser, self.description
    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])
