from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Professional, Consultation


class ProfessionalSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        validators=[RegexValidator(regex=r'^[a-zA-ZÀ-ÿ\s]+$', message="Nome inválido. Use apenas letras.")]
    )
    profession = serializers.CharField(
        max_length=255,
        validators=[RegexValidator(regex=r'^[a-zA-ZÀ-ÿ\s]+$', message="Profissão inválida.")]
    )
    address = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=20)

    class Meta:
        model = Professional
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    professional = ProfessionalSerializer(read_only=True)
    professional_id = serializers.PrimaryKeyRelatedField(
        queryset=Professional.objects.all(),
        source='professional',
        write_only=True
    )

    class Meta:
        model = Consultation
        fields = ['id', 'date', 'professional', 'professional_id']
