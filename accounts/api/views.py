from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializers, UserSerializer

User = get_user_model()

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
        'User':{
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }, 'message': 'Usuário cadastrado com sucesso.'}, status=status.HTTP_201_CREATED)

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user
