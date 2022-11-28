from django.db import models
from blog_sign_in_app.forms import User
# Create your models here.
class category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField()
    add_date = models.DateTimeField(auto_now_add=True,null=True)



class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')

    