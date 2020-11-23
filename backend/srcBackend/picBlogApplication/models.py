from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    upload = models.ImageField(upload_to ='picBlogApplication/images/') 
    like = models.BooleanField()
    comment = models.CharField(max_length=100)
    re_share = models.BooleanField()
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)


# Create your models here.
