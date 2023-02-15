from django.db import models
from unicodedata import category, name

class Account(models.Model):
    login_account = models.CharField(verbose_name='ログインアカウント', max_length=50)