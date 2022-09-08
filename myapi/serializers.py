from myapi.models import Comment, Post

from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Comment.objects.all(),
        view_name='comments-detail'
    )
    """
    Serializer for Post model.
    """
    class Meta:
        model = Post
        fields = ['owner', 'title', 'text', 'created', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Post.objects.all(),
        view_name='posts-detail'
    )
    """
    Serializer for Comment model.
    """
    class Meta:
        model = Comment
        fields = ['post', 'owner', 'text', 'created']
