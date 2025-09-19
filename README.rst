=========================================================================================
Projetos_DockerEstudo
=========================================================================================

Uma POC (Prova de Conceito) de lista de tarefas utilizando **Python**, **Docker**, **Django**
 e um banco de dados **PostgreSQL**.

.. image:: https://img.shields.io/badge/status-POC%20em%20desenvolvimento-blue.svg
    :target: https://github.com/usuario/seu-repositorio
    
------------------------------------------------------------------------------------------

Tecnologias Utilizadas
======================

* **Python** (gerenciado com pyenv)
* **Docker**
* **Docker Compose**
* **Django** ------------------------------------------------------------------------------------------

Pré-requisitos
==============

Certifique-se de que as seguintes ferramentas estão instaladas e configuradas na sua máquina.

1.  Python (com pyenv)
---------------------

A forma recomendada para instalar e gerenciar versões do Python é com o **pyenv**. Ele permite que você alterne facilmente entre versões sem conflitos.

**macOS (via Homebrew)**

.. code-block:: bash

    $ brew install pyenv

**Linux (via curl)**

.. code-block:: bash

    $ curl https://pyenv.run | bash

*Após a instalação, siga as instruções no terminal para adicionar o pyenv ao seu PATH.*

2.  Docker e Docker Compose
---------------------------

A maneira mais fácil de instalar o Docker e o Docker Compose é através do **Docker Desktop**. Ele é a ferramenta oficial e já inclui o Docker Engine e o Docker Compose.

* Baixe e instale o **Docker Desktop** em: `https://www.docker.com/products/docker-desktop/`

**Linux (via gerenciador de pacotes)**

*Para sistemas baseados em Debian/Ubuntu, use:*

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install docker.io docker-compose

3.  Git
-------

O **Git** é essencial para clonar o repositório.

**Windows**

* Baixe o instalador oficial em: `https://git-scm.com/download/win`

**macOS (via Homebrew)**

.. code-block:: bash

    $ brew install git

**Linux (via gerenciador de pacotes)**

*Para sistemas baseados em Debian/Ubuntu, use:*

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install git
------------------------------------------------------------------------------------------

Configuração e Execução
=======================

Siga os passos abaixo para colocar o projeto em funcionamento.

1. **Clonar o Repositório**


Primeiro, clone o projeto para sua máquina local usando o Git.

.. code-block:: bash

    $ git clone https://github.com/seu-usuario/seu-repositorio.git
    $ cd seu-repositorio
     

2.  **Configuração do Ambiente Python**
    
    Use `pyenv` para instalar a versão do Python desejada:
    
    .. code-block:: bash
    
        $ pyenv install 3.13.7
        $ pyenv local 3.13.7
        # Instale as dependências a partir do arquivo requirements.txt
        $ pip install -r requirements.txt
    
3.  **Executando com Docker Compose**
    
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