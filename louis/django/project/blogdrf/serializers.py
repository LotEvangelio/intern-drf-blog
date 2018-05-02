from rest_framework import serializers

from .models import Category, Tag, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'title'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'title'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'banner_photo', 'tags', 'category', 'body', 'status')
