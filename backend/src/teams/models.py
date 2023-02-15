from django.db import models
from core.mdoels import BaseModel
# from django.core.validators import MaxValueValidator, MinValueValidator

class Team(BaseModel):

    prefecture_code = models.CharField(
        verbose_name='都道府県コード',
        max_length=30
    )
    
    prefecture_name = models.CharField(
        verbose_name='都道府県名',
        max_length=10
    )
    
    city_code = models.CharField(
        verbose_name='市区町村コード',
        max_length=50
    )
    
    city_name = models.CharField(
        verbose_name='市区町村名',
        max_length=50
    )
    
    name_ja = models.CharField(
        verbose_name='チーム名：日本語',
        max_length=250
    )
    
    name_en = models.CharField(
        verbose_name='チーム名：英名',
        max_length=250
    )
    
    name_kana = models.CharField(
        verbose_name='チーム名：カナ',
        max_length=250
    )
    
    home_ground = models.CharField(
        verbose_name='ホームグラウンド',
        blank=True,
        null=True,
        max_length=250
    )
    
    slogan = models.CharField(
        verbose_name='スローガン',
        blank=True,
        null=True,
        max_length=100
    )
    
    introduction = models.TextField(
        verbose_name='チーム紹介文',
        blank=True,
        null=True,
        max_length=1000
    )
    
    deleted_at = models.DateTimeField(verbose_name='削除日時', blank=True, null=True)