from django.db import models

# Create your models here.

class User(models.Model):
    User_nickname=models.CharField(max_length=150,primary_key=True,default='')
    user_name=models.CharField(max_length=150,default='')
    user_email=models.EmailField(default='')
    user_age=models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname : {self.User_nickname} | E-mail: {self.user_email}'