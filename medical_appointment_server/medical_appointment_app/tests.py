from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Professional


class ProfessionalTests(APITestCase):
    def setUp(self):
        self.professional_data = {
            "name": "Dr  João Silva",
            "profession": "Médico",
            "address": "Rua X, 123",
            "contact": "(11) 99999-9999",
            "social_name": "João",
        }
        self.professional = Professional.objects.create(**self.professional_data)

    def test_create_professional(self):
        url = reverse("professional-list")
        data = {
            "name": "Dra Maria Souza",
            "profession": "Fisioterapeuta",
            "address": "Av. Y, 456",
            "contact": "(11) 88888-8888",
            "social_name": "Maria",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Dra Maria Souza")

    def test_get_professionals(self):
        url = reverse("professional-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_professional(self):
        url = reverse("professional-detail", args=[self.professional.id])
        data = {"name": "Dr João Pedro"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.professional.refresh_from_db()
        self.assertEqual(self.professional.name, "Dr João Pedro")

    def test_delete_professional(self):
        url = reverse("professional-detail", args=[self.professional.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Professional.objects.count(), 0)


