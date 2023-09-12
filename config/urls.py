from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from config import settings
from core.views import ClienteViewSet, ServicoViewSet
from rest_framework import routers
from auth.views import UserInfoView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'servicos', ServicoViewSet)


urlpatterns = [
    path('lavajato/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user-info/', UserInfoView.as_view(), name='user_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
