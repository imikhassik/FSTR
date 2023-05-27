from django.utils import timezone
from rest_framework import serializers

from .models import Pereval, Coords, Image, User, Level


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'data']


class PerevalSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(initial=timezone.now())
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'user', 'coords', 'level', 'images']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create(**user_data)

        coords_data = validated_data.pop('coords')
        coords = Coords.objects.create(**coords_data)

        level_data = validated_data.pop('level')
        level = Level.objects.create(**level_data)

        images_data = validated_data.pop('images', [])
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level)

        for image_data in images_data:
            Image.objects.create(pereval=pereval, **image_data)

        return pereval
