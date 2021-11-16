from rest_framework import serializers
from snippets.models import UploadImageTest
from easy_thumbnails_rest.serializers import ThumbnailerSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = ThumbnailerSerializer(alias='avatar')

    class Meta:
        model = UploadImageTest
        fields = ('name', 'image', 'owner')

