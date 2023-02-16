from django.db import models
from core.models import BaseModel
from accounts.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator

class Team(BaseModel):

    '''
    チーム属性クラス
    '''
    class Attributes(models.IntegerChoices):
        成人 = 1
        大学 = 2
        高校 = 3
        中学 = 4
        少年 = 5

    '''
    チーム種別クラス
    '''
    class Types(models.IntegerChoices):
        硬式         = 1
        軟式         = 2
        準硬式       = 3
        ソフトボール = 4
    
    '''
    チームレベルクラス
    '''
    class Levels(models.IntegerChoices):
        全国大会出場レベル     = 1
        都道府県大会出場レベル = 2
        地区大会出場レベル     = 3
        初心者レベル           = 4
    
    manager = models.ForeignKey(
        User,
        verbose_name='管理者',
        on_delete=models.DO_NOTHING
    )
    
    attribute = models.PositiveSmallIntegerField(
        verbose_name='属性',
        choices=Attributes.choices
    )
    
    team_type = models.PositiveSmallIntegerField(
        verbose_name='種別',
        choices=Types.choices
    )
    
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
    
    started_date = models.DateField(
        verbose_name='結成日',
    )