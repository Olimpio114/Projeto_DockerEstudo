=========================================================================================
Projetos_DockerEstudo
=========================================================================================

Uma POC para gerenciamento de tarefas utilizando Docker, Python e Django, com controle de versão via **pyenv**.

.. image:: https://img.shields.io/badge/status-POC%20em%20desenvolvimento-blue.svg
    :target: https://github.com/usuario/seu-repositorio
    
------------------------------------------------------------------------------------------

Tecnologias Utilizadas
======================

* **Python** (gerenciado com pyenv)
* **Docker**
* **Docker Compose**
* **Django** (deduzido pela estrutura de arquivos)

------------------------------------------------------------------------------------------

Pré-requisitos
==============

Certifique-se de que as seguintes ferramentas estão instaladas e configuradas na sua máquina:

* **Python**: Recomendamos usar o `pyenv` para gerenciar as versões.
* **Docker**: Motor de contêineres.
* **Docker Compose**: Ferramenta para gerenciar contêineres multi-serviços.
* **Git**: Para clonar o repositório.

------------------------------------------------------------------------------------------

Configuração e Execução
=======================

Siga os passos abaixo para colocar o projeto em funcionamento.

1.  **Configuração do Ambiente Python**
    
    Use `pyenv` para instalar a versão do Python desejada:
    
    .. code-block:: bash
    
        $ pyenv install 3.12.2
        $ pyenv local 3.12.2
    
2.  **Executando com Docker Compose**
    
    Na pasta raiz do projeto, execute um dos comandos abaixo:
    
    .. code-block:: bash
    
        # Rodar o programa em primeiro plano (os logs aparecem no terminal)
        $ docker-compose up
    
        # Rodar em segundo plano (libera o terminal)
        $ docker-compose up -d
    
    Para verificar o status dos contêineres:
    
    .. code-block:: bash
    
        $ docker-compose ps
    
------------------------------------------------------------------------------------------

Acesso à Aplicação
==================

Após a execução bem-sucedida, a aplicação estará disponível nos seguintes endereços:

* **Página Principal (Lista de Tarefas):**
    
    Acesse no seu navegador: `http://localhost:8000/`

* **Painel de Administração:**
    
    Acesse no seu navegador: `http://localhost:8000/admin/`
    
    Se o painel de administração não funcionar imediatamente (devido a migrações pendentes), execute o comando de migração em um novo terminal:
    
    .. code-block:: bash
    
        $ docker-compose exec web python manage.py migrate

------------------------------------------------------------------------------------------