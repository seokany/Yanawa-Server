from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "pk",
            "username",
            "user_image",
        ]


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def save(self, **kwargs):
        user = User.objects.create(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )

        if len(self.validated_data["password"]) >= 8:
            user.set_password(self.validated_data["password"])
            user.save()
            return user
        else:
            raise ValidationError("패스워드를 8글자 이상 입력해주세요")

    class Meta:
        model = User
        fields = [
            "pk",
            "email",
            "username",
            "user_image",
            "password",
        ]
