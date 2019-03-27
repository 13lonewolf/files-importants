from rest_framework.routers import DefaultRouter
from backend_web.cookie import views as cookie_views


mobile_router = DefaultRouter()
mobile_router.register('cke', cookie_views.CookieViewSet)