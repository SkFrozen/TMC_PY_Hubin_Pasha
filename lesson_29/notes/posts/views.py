from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Post, Tag
from .permissions import IsOwnerOrReadOnly
from .serializers import post_serializer, tag_serializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = post_serializer.PostCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = post_serializer.PostListSerializer(queryset, many=True)
        return Response(serializer.data)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = post_serializer.PostDetailSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = tag_serializer.TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
