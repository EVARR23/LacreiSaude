from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Profissional

class ProfissionalAPITests(APITestCase):

    def test_criar_profissional(self):
        url = reverse('profissional-list')  # Ajuste se necessário
        data = {
            "nome_social": "Dra. Eva",
            "profissional": "Psicologia",
            "endereco": "Rua das Flores, 123",
            "contato": "1234567890"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   

    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome_social="Ana Souza",
            profissional="Psicóloga",
            endereco="Rua A, 123",
            contato="99999-9999"
        )
        self.list_url = reverse("profissional-list")

    def test_listar_profissionais(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
        self.assertIn("nome_social", response.data[0])
        self.assertIn("profissional", response.data[0])
        self.assertIn("endereco", response.data[0])
        self.assertIn("contato", response.data[0])

    def test_detalhar_profissional(self):
        detail_url = reverse("profissional-detail", args=[self.profissional.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome_social"], self.profissional.nome_social)
        self.assertEqual(response.data["profissional"], self.profissional.profissional)
        self.assertEqual(response.data["endereco"], self.profissional.endereco)
        self.assertEqual(response.data["contato"], self.profissional.contato)

    def test_criar_profissional_falha(self):
        data = {}  # sem dados, deve falhar
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nome_social", response.data)
        self.assertIn("profissional", response.data)
        self.assertIn("endereco", response.data)
        self.assertIn("contato", response.data)

    def test_atualizar_profissional(self):
        detail_url = reverse("profissional-detail", args=[self.profissional.id])
        payload = {
            "nome_social": "Ana Souza Atualizada",
            "profissional": "Psiquiatra",
            "endereco": "Rua Nova, 321",
            "contato": "97777-6666"
        }
        response = self.client.put(detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profissional.refresh_from_db()
        self.assertEqual(self.profissional.nome_social, payload["nome_social"])
        self.assertEqual(self.profissional.profissional, payload["profissional"])

    def test_atualizar_profissional_falha(self):
        detail_url = reverse("profissional-detail", args=[self.profissional.id])
        payload = {
            "nome_social": "",
            "profissional": "",
            "endereco": "",
            "contato": ""
        }
        response = self.client.put(detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nome_social", response.data)
        self.assertIn("profissional", response.data)
        self.assertIn("endereco", response.data)
        self.assertIn("contato", response.data)

    def test_deletar_profissional(self):
        detail_url = reverse("profissional-detail", args=[self.profissional.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profissional.objects.count(), 0)
