# 🏥 Lacrei Saúde - API com Django e Docker

Este projeto é uma API para gerenciamento de usuários, profissionais e consultas, construída com Django e PostgreSQL, utilizando Docker para facilitar o setup do ambiente.

---
🚀 Acesso a aplicação na AWS

http://56.124.57.201:8000/admin
Login: LacreiSaude
Senha: admin

## ⚙️ Setup do Ambiente Local com Docker

```bash
git clone https://github.com/EVARR23/LacreiSaude
cd LacreiSaude
docker-compose up -d
docker-compose build
docker-compose exec web python src/manage.py migrate
docker-compose exec web python src/manage.py createsuperuser


🚀 Como rodar o projeto (modo local)

python src/manage.py runserver
Acesse: http://localhost:8000/admin/

Login: LacreiSaude
Senha: admin


🔗 Endpoints da API (Sugger)

http://localhost:8000/api/profissional/

http://localhost:8000/api/consulta/


🧪 Testes Automatizados com APITestCase

python src/manage.py test api.tests.test_profissionais
python src/manage.py test api.tests.test_consultas


🧠 Decisões Técnicas

Utilização de Django REST Framework para criar uma API RESTful.
Banco de dados PostgreSQL com persistência de dados via volume Docker.
Painel administrativo personalizado com django-jazzmin.
Estrutura de pastas organizada por app.



🚢 Deploy, CI/CD e Versionamento

Versionamento no GitHub: https://github.com/EVARR23/LacreiSaude
CI/CD via GitHub Actions 
Docker usado para build e deploy local
Criação de uma instância EC2 e configuração do docker na AWS. 



👤 Autora
Eva Rebouças Rodrigues
GitHub · São José dos Campos – SP · Desenvolvedora e QA
