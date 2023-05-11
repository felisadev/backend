from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

app_name = "users"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "assistance-centre/",
        views.AssistanceCentreViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "assistance-centre/<int:pk>/",
        views.AssistanceCentreViewSet.as_view(
            {"get": "retrieve", "delete": "destroy", "patch": "update"}
        ),
    ),
    path(
        "promotoras/",
        views.PromotoraViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "promotora/<int:pk>/",
        views.PromotoraViewSet.as_view(
            {"get": "retrieve", "delete": "destroy", "patch": "update"}
        ),
    ),
    path(
        "usuario-app/",
        views.UsuarioAppViewSet.as_view(
            {"post": "create", "patch": "update"}
        )
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
