from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here

class UserManager(models.Manager):
    def validate_user(self, post):
        isValid = True
        if len(post.get('name')) == 0:
            isValid = False
        if len(post.get('email')) == 0:
            isValid = False
        if len(post.get('password')) < 8:
            isValid = False
        if post.get('password') != post.get('password2'):
            isValid = False
        return isValid

    def login_user(self, post):
        user = self.filter(email = post.get('email')).first()
        if user.password == bcrypt.hashpw(post['password'].encode(), user.password.encode()):
            return (True, user)
        return (False, 'notuser')

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class QuoteManager(models.Manager):
    def validate_quote(self, post):
        isValid = True
        if len(post.get('author')) == 0:
            isValid = False
        if len(post.get('message')) == 0:
            isValid = False
        return isValid

class Quote(models.Model):
    author = models.CharField(max_length=255)
    message = models.CharField(max_length=1500)
    user = models.ForeignKey(User, related_name = "creator")
    objects = QuoteManager()
