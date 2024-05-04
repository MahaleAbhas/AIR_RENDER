from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, UserRoleViewSet, credential_mail

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'user-roles', UserRoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-mail/', credential_mail)
]