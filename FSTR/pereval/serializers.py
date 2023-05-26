from django.utils import timezone
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

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


# class ImagesSerializer(serializers.ModelSerializer):
#     data = serializers.CharField()
#
#     class Meta:
#         model = Image
#         fields = ['title', 'date_added', 'data']


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(initial=timezone.now())
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    # images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        depth = 1
        fields = ['beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'user', 'coords', 'level']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.filter(email=user_data['email'])
        if user.exists():
            user_serializer = UserSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
        else:
            user = User.objects.create(**user_data)

        coords_data = validated_data.pop('coords')
        coords = Coords.objects.create(**coords_data)

        level_data = validated_data.pop('level')
        level = Level.objects.create(**level_data)

        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level)

        return pereval
