
# 🚀 Lacrei Saúde - 

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework, voltada para a gestão de usuários, profissionais e consultas na plataforma Lacrei Saúde.

---

Acesse o painel administrativo:  
AWS: <http://56.124.57.201:8000/admin/>

**Login:** `LacreiSaude`  
**Senha:** `admin`

Swagger
http://56.124.57.201:8000/api/swagger/
### 🔽 Clonando o Repositório

git clone <https://github.com/EVARR23/LacreiSaude.git>
cd LacreiSaude

### ▶️ Rodando Localmente com Django

Crie e ative um ambiente virtual, depois instale as dependências:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

poetry install -r requirements.txt
python manage.py migrate
python manage.py runserver

```


Após a aplicação subir, acesse:

- API de Profissionais: [http://127.0.0.1:8000/api/profissional/](http://127.0.0.1:8000/api/profissional/)
- API de Consultas: [http://127.0.0.1:8000/api/consulta/](http://127.0.0.1:8000/api/consulta/)


## 🧪 Executando os Testes

Para rodar os testes unitários com `APITestCase`:

python manage.py test api.tests.test_profissionais
python manage.py test api.tests.test_consultas



## 🧠 Decisões Técnicas

- **Framework principal:** Django Rest Framework
- **Banco de dados:** PostgreSQL
- **Autenticação:** JWT
- **Documentação da API:** drf-spectacular (Swagger/OpenAPI)
- **Containerização:** Docker + Docker Compose
- **Versionamento:** Git
- **Testes automatizados:** APITestCase com Django Test

---

## 🚀 Deploy (CI/CD e Ambiente de Produção)

- **Ambiente:** AWS (EC2)
- **Banco de dados:** PostgreSQL
- **CI/CD:** GitHub Actions
  - Lint e testes automatizados em cada push
  - Deploy automatizado via SSH

---

## 📋 Pontos de Melhoria e Recomendações

Durante a análise técnica do projeto, foram identificados os seguintes pontos:

### ✅ Já Implementados

- **Segurança:** Medidas básicas como autenticação JWT e validações nos dados foram incluídas.
- **Sanitização:** Entradas protegidas contra ataques como SQL Injection.
- **Testes Automatizados:** Utilização de `APITestCase`. Arquivos de teste estão no repositório.
- **Rollback:** Estratégia de rollback documentada (via Docker ou GitHub Actions).

### 🟨 Recomendado para Melhorar

- **Documentação da API:** Garantir que o Swagger (drf-spectacular) esteja acessível, por exemplo em `/api/schema/swagger-ui/`.
- **Ambientes Separados:** Documentar claramente a separação entre ambientes de staging e produção.



Desenvolvido  por Eva Rebouças Rodrigues.
