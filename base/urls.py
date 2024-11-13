from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from base import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all-babysitters', views.BabysitterViewSet, basename='babysitter-profile')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('', views.index),
    path('parents/', views.TheParents),
    path('kids/', views.TheKids),
    path('info/', views.TheRequests),
    path('reviews/', views.TheReviews),
    path('availability/', views.TheAvailability),
    path('message/', views.TheMeetings),
    path('login/',TokenObtainPairView.as_view()),
    path('register/', views.register),
    path('timewindow/', views.TheTimeWindow), 
    path('', include(router.urls)),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
