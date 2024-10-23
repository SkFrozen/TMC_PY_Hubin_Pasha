from rest_framework import serializers
from users.models import User

from ..models import Post, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
        read_only_fields = ("id", "username")


class PostListSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = ("uuid", "title", "created_at", "image", "tags", "owner")
        read_only_fields = ("uuid", "title", "created_at", "image", "tags", "owner")


class PostCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = serializers.ListField(write_only=True, child=serializers.CharField())

    class Meta:
        model = Post
        fields = ("title", "content", "image", "tags", "owner")

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        post = Post.objects.create(**validated_data)
        for tag_name in tags:
            tag, create = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return post


class PostDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = ("uuid", "title", "content", "created_at", "image", "tags", "owner")
        read_only_fields = ("uuid", "created_at", "owner")
