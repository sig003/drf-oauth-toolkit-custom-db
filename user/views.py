#from http.client import HTTPResponse
from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics #, permissions, serializers
from .permissions import IsAuthenticatedOrCreate
#from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
#from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# class RegisterView(APIView):
#     def post(self, request):
#         print(11)
#         return HTTPResponse("Hello, World!")