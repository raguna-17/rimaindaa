from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# API用
from rest_framework.routers import DefaultRouter
from memo.views import NoteViewSet, ReminderViewSet, NotificationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ルーター登録
router = DefaultRouter()
router.register(r'memos', NoteViewSet, basename='memo')
router.register(r'reminders', ReminderViewSet, basename='reminder')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # SPA用（React/Vueのビルド成果物を返す）
    path('', TemplateView.as_view(template_name='index.html'), name='spa_entry'),
]
