from rest_framework import serializers
from .models import Professional, Consultation

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
    professional_id = serializers.PrimaryKeyRelatedField(
        queryset=Professional.objects.all(),
        source='professional',
        write_only=True
    )


class ConsultationSerializer(serializers.ModelSerializer):
    professional = ProfessionalSerializer(read_only=True)
class Meta:
    model = Consultation
    fields = ['id', 'date', 'professional', 'professional_id']
