from rest_framework.generics import CreateAPIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        data = serializer.data
        data["key"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(
            data, status=status.HTTP_201_CREATED, headers=headers
        )

# user i oluşturup sisteme kaydettik . sisteme kaydettiğimiz useri da bir token ürettik. ve o useri da tokeni ile birlikte frontende geri döndük.
