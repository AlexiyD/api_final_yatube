from rest_framework.serializers import (ModelSerializer,
                                        SlugRelatedField,
                                        CurrentUserDefault,
                                        ValidationError)
from posts.models import Comment, Group, Post, User, Follow
from rest_framework.validators import UniqueTogetherValidator

class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = fields = '__all__'


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        read_only=True, slug_field='username',
        default = CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('following', 'user')
            )
        ]
    
    def validate_following(self, value):
        if value == self.context['request'].user:
            raise ValidationError('подписка на себя не возможна')
        return value