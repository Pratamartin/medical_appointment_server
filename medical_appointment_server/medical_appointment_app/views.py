from rest_framework import viewsets
from .models import Professional, Consultation
from .serializers import ProfessionalSerializer, ConsultationSerializer


class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        professional_id = self.request.query_params.get('professional_id')
        if professional_id:
            return Consultation.objects.filter(professional_id=professional_id)
        return super().get_queryset()
