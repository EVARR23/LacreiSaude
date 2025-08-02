from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Profissional, Consulta


class ConsultaAPITests(APITestCase):

    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome_social="Dra. Gabriela",
            profissional="Psicóloga",
            endereco="Rua das Flores, 123",
            contato="11999999999"
        )

    def test_criar_consulta(self):
        url = reverse('consulta-list')  # ou '/api/consultas/'
        data = {
            "profissional": self.profissional.id,
            "data": "2025-08-01T14:42:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consulta.objects.count(), 1)

    def test_erro_campo_obrigatorio(self):
        url = reverse('consulta-list')
        data = {}  # Nenhum campo enviado
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('profissional', response.data)
        self.assertIn('data', response.data)

    def test_erro_formato_data_invalido(self):
        url = reverse('consulta-list')
        data = {
            "profissional": self.profissional.id,
            "data": "31-08-2025"  # Formato inválido para DateTimeField
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('data', response.data)

    def test_erro_data_formato_invalido(self):
        url = reverse('consulta-list')
        data = {
            "profissional": self.profissional.id,
            "data": "31-08-2025 14:00"  # formato errado
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('data', response.data)