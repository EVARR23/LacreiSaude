- Setup do ambiente local e com Docker

git clone <https://github.com/EVARR23/LacreiSaude>
cd LacreiSaude
docker-compose build
docker-compose up -d
docker-compose exec web python src/manage.py migrate
docker-compose exec web python src/manage.py createsuperuser

- Instruções para rodar o projeto

    python manage.py runserver
    URL: <http://localhost:8000/admin/>
    Login: LacreiSaude
    Senha: admin

- Comando roda sugger

    <http://127.0.0.1:8000/api/usuario/>
    <http://127.0.0.1:8000/api/profissional/>
    <http://127.0.0.1:8000/api/consulta/>

- Instruções para rodar os testes com `APITestCase`

    python manage.py test api.tests.test_profissionais
    python manage.py test api.tests.test_consultas

- Explicações sobre decisões técnicas
- Instruções de como foi feito o deploy (ambientes, ferramentas, fluxo CI/CD)

    github: <https://github.com/EVARR23/LacreiSaude>
