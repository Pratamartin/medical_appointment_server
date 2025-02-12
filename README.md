# medical appointment server

## Índice

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Testes](#testes)

## Instalação

### Clonando o Repositório

```bash
https://github.com/Pratamartin/medical_appointment_server.git
cd .\medical_appointment_server\
```
## Configuração

### Variáveis de Ambiente

Crie uma pasta chamada dotenv_files e dentro dessa pasta criar um arquivo`.env` na raiz do projeto com as seguintes variáveis
```bash
SECRET_KEY="change-me"

# 0 False, 1 True
DEBUG="1"

# Comma Separated values
ALLOWED_HOSTS="127.0.0.1, localhost"

DB_ENGINE="django.db.backends.postgresql"
POSTGRES_DB="medical_database"
POSTGRES_USER="medical_user"
POSTGRES_PASSWORD="medical_user_password"
POSTGRES_HOST="psql"
POSTGRES_PORT="5432"
```
## Execução

### Buildando e Iniciando os Contêineres

Para construir as imagens Docker e iniciar a aplicação, execute:
```bash
docker-compose up --build
```
### Acessando a aplicação

Após inicializar, a aplicação estará disponível em:
- API: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Acessando os endpoints

- API: [http://127.0.0.1:8000/api/professionals/](http://127.0.0.1:8000/api/professionals/)

- API: [http://127.0.0.1:8000/api/consultations/](http://127.0.0.1:8000/api/consultations/)

## Testes
### Executando os testes

1. Acesse o container da aplicação:
```bash
docker-compose up -d  # executa os contêineres em segundo plano
```
2. Execute os testes 
```bash
docker-compose exec medical_appointment_server  python manage.py test medical_appointment_app
```
