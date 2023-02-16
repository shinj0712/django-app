from django.contrib.auth import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractBaseUser, PermissionsMixin):
    username_validators = UnicodeUsernameValidator()
    username = models.CharField(
        verbose_name='ユーザーネーム',
        max_length=150,
        unique=True,
        help_text='※150文字以下の英数字、一部の記号で入力してください。',
        validators=[ username_validators ],
        error_messages={ 'unique': 'このユーザー名は既に使用されています。' },
    )
    
    is_staff = models.BooleanField(
        verbose_name='ユーザーステータス',
        help_text='ユーザーがこの管理サイトにログインできるかどうかを判別します。',
        default=False
    )
    
    is_active = models.BooleanField(
        "アクティブユーザ",
        help_text="このユーザーをアクティブとして扱うかどうかを指定します。アカウントを削除する代わりに、この選択状態を切り替えてください。",
        default=True,
    )
    
    email = models.EmailField(
        verbose_name='メールアドレス',
        blank=True,
        null=True,
        max_length=254,
    )
    
    first_name = models.CharField(
        verbose_name='名前',
        max_length=100,
    )
    
    last_name = models.CharField(
        verbose_name='苗字',
        max_length=100,
    )
    
    first_name_kana = models.CharField(
        verbose_name='名前：カナ',
        max_length=100,
    )
    
    last_name_kana = models.CharField(
        verbose_name='苗字：カナ',
        max_length=100,
    )
    
    first_name_en = models.CharField(
        verbose_name='名前：英語',
        max_length=200,
    )
    
    last_name_en = models.CharField(
        verbose_name='苗字：英語',
        max_length=200,
    )
    
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True, editable=True)
    # deleted_at = models.DateTimeField(verbose_name='削除日時', blank=True, null=True)
    
    objects = UserManager()

    # EMAIL_FIELD     = 'email'
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = [
        # 'email',
        'last_name',
        'first_name',
        'last_name_kana',
        'first_name_kana',
        'first_name_en',
        'last_name_en',
    ]

    class Meta:
        verbose_name        = 'user'
        verbose_name_plural = 'users'
    
    def clean(self) -> None:
        return super().clean()
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def get_short_name(self):
        return self.first_name
    
    def get_full_name_kana(self):
        return f"{self.last_name_kana} {self.first_name_kana}"
    
    def get_full_name_en(self):
        return f"{self.first_name_en} {self.last_name_en}"
