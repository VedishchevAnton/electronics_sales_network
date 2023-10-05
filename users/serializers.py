from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # Сериализатор используется для сериализации и десериализации объектов User.
    password = serializers.CharField(write_only=True)  # Поле password используется только для записи.

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'is_active')

    def create(self, validated_data):
        # Метод create переопределяет стандартный метод создания объекта
        # и хеширует пароль перед сохранением пользователя в базе данных.
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
