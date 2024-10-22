from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import User
from .permissions import CreateOnlyOrSuperuserPermission
from .serializers import UserSerializers


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (CreateOnlyOrSuperuserPermission,)


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAdminUser,)
