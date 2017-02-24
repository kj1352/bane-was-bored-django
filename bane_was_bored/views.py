from django.shortcuts import render
from django.http import HttpResponse
from bane_was_bored.models import Post
from torrent.models import Tors
from django.utils import timezone
#rest_framework
from rest_framework.views import APIView
from bane_was_bored.serializers import PostSerializer, TorsSerializer
from rest_framework.response import Response



class PostList(APIView):
    def get(self,request):
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True)
        return Response(serializer.data)

class TorsList(APIView):
    def get(self,request):
        torlist = Tors.objects.all()
        serializer = TorsSerializer(torlist, many=True)
        return Response(serializer.data)
