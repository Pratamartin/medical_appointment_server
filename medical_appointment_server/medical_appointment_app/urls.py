from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet, ConsultationViewSet

router = DefaultRouter()
router.register(r'professionals', ProfessionalViewSet)
router.register(r'consultations', ConsultationViewSet)

urlpatterns = router.urls
