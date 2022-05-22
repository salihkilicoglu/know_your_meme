from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'pk',
            'user',
            'title',
            'body',
            'tags',
            'make_public',
            'publish_date',
            'path',
            'endpoint',
        ]
        required_fields = ['title','body']
        unique_fields = ['title',]
        read_only_fields = ['user',]
