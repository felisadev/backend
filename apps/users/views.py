from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import AssistanceCentre, PersonaParaAsistencia, UsuariosDeApp
from .serializers import AssistanceCentreSerializer, PromotoraSerializer, UsuariosDeAppSerializer


class AssistanceCentreViewSet(ModelViewSet):
    queryset = AssistanceCentre.objects.all()
    serializer_class = AssistanceCentreSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()


class PromotoraViewSet(ModelViewSet):
    queryset = PersonaParaAsistencia.objects.all()
    serializer_class = PromotoraSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()


class UsuarioAppViewSet(ModelViewSet):
    queryset = UsuariosDeApp.objects.all()
    serializer_class = UsuariosDeAppSerializer
    # todo: increase security here
    permission_classes = (AllowAny,)
