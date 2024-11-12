from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from post.models import Post

class ListPostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

