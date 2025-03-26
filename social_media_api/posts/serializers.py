from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        
        # use a creat()method to esnure  the logged_in user is the auther of thepost
        def create(self, validated_data):
            # ensure that the logged in user is the author and validating their data
            request = self.context.get('request') 
            validated_data['author'] = request.user
            return super().create(validated_data)
        
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset = Post.objects.all()) #ensure the post chosen when creating a coment, exists in the database
    author = serializers.ReadOnlyField(source = 'author.username') #This makes the author field read-only, so users cannot change the author.
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user  # ensure that the logged in user is the author and validating their data
        return super().create(validated_data)
