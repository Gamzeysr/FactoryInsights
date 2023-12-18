from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(User.objects.all())]

    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input": "password"}
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True,
        style={"input": "password"}
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name",
                  "last_name", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"error massage": "passwords didn't match"})
        return attrs

    def create(self, validated_data):
        password = validated_data["password"]
        validated_data.pop("password2")
        # veritabanına kaydolmaması için yaptık bu pop methodunu

        user = User.objects.create(**validated_data)
        # 👆user objesini veritabanına create ettik.

        user.set_password(password)
        # 👆passwordu açıkca kaydetmek yerine şifreyip kaydettik

        user.save()
        # password u sifreledikten sonra tekrardan kayıt yaptık
        return user


class UserForToken(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CustomTokenSerializer(TokenSerializer):
    user = UserForToken()
# tokenin hangi kullanıcıya ait olduğunu görebilmek için eklediğimiz field Yukarıdaki serializer ı da userin hangi fieldsları görülsün diye yazdık.

    class Meta:
        fields = ("key", "user")
