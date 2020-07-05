from rest_framework import serializers
from ..models import News
import datetime


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'summary',
            'link',
            'comment',
            'published',
        ]

    def create(self, validated_data):
        # auto add time publish when create Item
        validated_data["published"] = datetime.datetime.now()
        return News.objects.create(**validated_data)
