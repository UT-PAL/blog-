from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#built-in user model
class User_profile(models.Model):
    user=models.OneToOneField(User,primary_key=True, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics')
