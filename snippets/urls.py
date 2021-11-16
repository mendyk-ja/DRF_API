from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'images', views.ImageViewSet)

# The API ULRs are now determined automatically  by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('media/<image>', views.ImageViewSet),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
