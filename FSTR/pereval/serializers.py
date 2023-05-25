from rest_framework import serializers

from .models import PerevalAdded, Coords, Image


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    img = serializers.CharField()

    class Meta:
        model=Image
        fields = '__all__'


class PerevalAddedSerializer(serializers.ModelSerializer):
    status = serializers.CharField(initial='new')
    coord = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        coord_data = validated_data.pop('coord')
        coord = Coords.objects.create(**coord_data)
        pereval_added = PerevalAdded.objects.create(coord=coord, **validated_data)

        images_data = validated_data.pop('images')
        for image_data in images_data:
            Image.objects.create(pereval=pereval_added, **image_data)
        return pereval_added
