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

================================================================================
<<<<<Rodar o programa na pasta raiz do projeto>>>> 
-------------------------------------------------
docker-compose up    >. rodar 
docker-compose up -d   >>rodar em segundo plano
docker-compose ps  >> verificar os contêiners

cole em uma página>>> http://0.0.0.0:8000/

Acessar a Segunda Tela (o Painel de Administração) >>>  http://localhost:8000/admin/
se não funcionar siga>>
depois abra um terminal diferente veja exemplo e rode o código:
olimpio@olimpio:~/Documentos/Projeto_DockerEstudo$ docker-compose exec web python manage.py migrate

