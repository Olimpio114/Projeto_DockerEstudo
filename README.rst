Documentos-Projetos_Docker_PY
==================================================================================== 
Projeto de exemplo utilizando Python , Docker e pyenv para gerenciamento de versões.
===================================================================================
Tecnologias Utilizadas
Python (gerenciado com pyenv)
Docker
Docker Compose
Virtualenv (venv)
Pré-requisitos
Python instalado (recomenda-se usar pyenv)
Docker
Docker Compose
Git
================================================================================
Configuração do Ambiente Python
Instale a versão do Python desejada usando pyenv :
pyenv install 3.12.2
pyenv local 3.12.2
==============================================================================
Reconstrua a imagem Docker 
docker build -t minha-primeira-imagem .

Execute o contêiner   
docker run -p 8000:8000 minha-primeira-imagem
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Executando o Docker Compose
Acesse a aplicação no navegador:
Abra seu navegador e digite o seguinte endereço: 
http://localhost:8000.

Pare os serviços:
Quando você terminar, volte para o terminal e pressione 
Ctrl + C.

Para reativar os serviços:
docker compose up

=============================================================================
1. Rodar Migrações e Criar um Superusuário: Como o banco de dados está vazio, 
você precisará aplicar as migrações do Django e criar um usuário administrador 
para acessar o painel de administração.

2. Conectar-se ao Banco de Dados: Acessar o banco de dados do seu computador 
local, usando uma ferramenta como o DBeaver ou psql, para gerenciar os dados
 diretamente.

3. Configurar um Servidor de Produção: Mudar do servidor de desenvolvimento 
do Django para um servidor de produção como o Gunicorn para se preparar para 
o deploy.
==============================================================================
Para adquirir secret-key
Execute o comando shell 
PYTHONPATH=./src python manage.py shell

Gerar a chave: Dentro do console do Django, execute as seguintes linhas:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
============================================================================
1. Fazer as Migrações do Banco de Dados: Aplicar as tabelas do Django no seu banco 
de dados PostgreSQL.
docker compose up -d

2. Criar uma Aplicação Django: Iniciar a criação de uma nova aplicação (startapp) 
para começar a construir as funcionalidades do seu projeto.
docker compose exec web python manage.py migrate
3. Criar um Superusuário: Criar uma conta de administrador para acessar o painel 
de administração do Django.
=================================================================================

Ver os contêineres em execução
Este é o comando mais comum para verificar se algo está ativo no Docker.

docker ps

Verificar os logs do contêiner
O servidor Django já imprime os logs diretamente no seu terminal, mas e se você tivesse rodado o contêiner em segundo plano? Você pode ver os logs de um contêiner específico com este comando:

docker logs <nome_do_seu_contêiner