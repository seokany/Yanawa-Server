from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator
    username_length = MinLengthValidator(5, "유저명을 5글자 이상 입력해주세요")

    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        "username",
        max_length=10,
        blank=False,
        unique=True,
        help_text=(
            "Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator, username_length],
    )
    user_image = models.ImageField(blank=True, upload_to="accounts/images/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        ordering = ("-id",)
        verbose_name = "사용자"
        verbose_name_plural = verbose_name
