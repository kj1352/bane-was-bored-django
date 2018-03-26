from rest_framework import serializers
from bane_was_bored.models import Post
from torrent.models import Tors

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text','img', 'created_date', 'published_date')

class TorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tors
        fields = ('author', 'text', 'link', 'published_date')
