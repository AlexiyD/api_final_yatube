from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework.viewsets import (ModelViewSet,
                                     ReadOnlyModelViewSet,
                                     GenericViewSet)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer,
                          GroupSerializer,
                          PostSerializer,
                          FollowSerializer)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ('=following__username', '=user__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
