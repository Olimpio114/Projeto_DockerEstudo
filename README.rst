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
