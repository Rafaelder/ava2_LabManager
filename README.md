# ⚗️ LabManager

> Sistema de Gerenciamento de Laboratórios Acadêmicos, Equipamentos e Reservas.

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-5.0+-green)
![Poetry](https://img.shields.io/badge/Poetry-Manager-blueviolet)

## 📖 Sobre o Projeto

O **LabManager** é uma aplicação web desenvolvida em Django para facilitar a administração de laboratórios em ambientes acadêmicos ou de pesquisa. O sistema permite o controle de inventário de equipamentos, gestão de status (ativo/manutenção) e agendamento de uso dos espaços.

O projeto utiliza uma arquitetura MVT (Model-View-Template) e implementa um banco de dados relacional (SQL) para garantir a integridade das informações.

## ✨ Funcionalidades

-   **Dashboard Interativo:** Visão geral com métricas de laboratórios ativos, total de equipamentos e reservas do dia.
-   **Gestão de Laboratórios:** Cadastro e listagem de salas e laboratórios.
-   **Inventário de Equipamentos:** Controle de status (`Ativo`, `Em Manutenção`, `Inativo`) e histórico de calibragem.
-   **Sistema de Reservas:** Agendamento de horários por usuários vinculados a laboratórios específicos.
-   **Autenticação:** Sistema de Login/Logout seguro.
-   **População Automática:** Script para gerar dados fictícios para testes e visualização rápida.

## 🛠 Tecnologias Utilizadas

-   **Backend:** Python, Django
-   **Frontend:** HTML5, Tailwind CSS (via CDN)
-   **Banco de Dados:** SQLite (padrão de desenvolvimento, compatível com PostgreSQL/MySQL)
-   **Gerenciamento de Pacotes:** Poetry

## 🗂 Estrutura do Banco de Dados (DER Simplificado)

O projeto segue uma modelagem relacional rigorosa:

-   **Laboratorio** (1) <---> (N) **Equipamento**
    -   *Um laboratório possui vários equipamentos, mas um equipamento pertence a apenas um laboratório.*
-   **Usuario** (1) <---> (N) **Reserva**
    -   *Um usuário pode fazer várias reservas.*
-   **Laboratorio** (1) <---> (N) **Reserva**
    -   *Um laboratório pode ter várias reservas agendadas.*

## 🚀 Como Executar o Projeto

### Pré-requisitos

-   Python 3.x instalado.
-   [Poetry](https://python-poetry.org/) instalado.

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/seu-usuario/labmanager.git](https://github.com/seu-usuario/labmanager.git)
    cd labmanager
    ```

2.  **Instale as dependências**
    ```bash
    poetry install
    ```

3.  **Ative o ambiente virtual**
    ```bash
    poetry shell
    ```

4.  **Execute as migrações do banco de dados**
    Isso criará o arquivo `db.sqlite3` e as tabelas necessárias.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um Superusuário (Admin)**
    Para acessar o painel administrativo e o dashboard inicial.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Popule o banco com dados de teste (Opcional)**
    O projeto conta com um comando personalizado para criar laboratórios, equipamentos e reservas fictícias automaticamente.
    ```bash
    python manage.py populate_db
    ```
    *> Nota: Este script cria usuários fictícios com a senha padrão `senha123`.*

7.  **Inicie o Servidor**
    ```bash
    python manage.py runserver
    ```

8.  **Acesse o Sistema**
    -   **Dashboard:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    -   **Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📸 Screenshots

*(Adicione aqui prints do seu Dashboard e da Tela de Login para ilustrar o projeto)*

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.
