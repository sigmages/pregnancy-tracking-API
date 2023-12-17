# pregnancy-tracking-API

API que oferece suporte para o acompanhamento da gravidez para profissionais da área da saúde, fornecendo informações sobre marcos do desenvolvimento fetal, cuidados pré-natais, entre outros aspectos relacionados à gestação das pacientes. Este projeto utilizou como base a [Caderneta da Gestante](<https://www.mds.gov.br/webarquivos/arquivo/crianca_feliz/Treinamento_Multiplicadores_Coordenadores/Caderneta-Gest-Internet(1).pdf>) (criada pelo Ministério da Saúde).

Com essa API será possível:

- Permitir que os profissionais de saúde possam cadastrar as gestantes, gerenciar as consultas de pré-natal, bem como exames, vacinas e outras informações inerentes à saúde gestacional;
- Permitir que os profissionais visualizem o histórico de consultas das gestantes, bem como os demais dados e informações;
- Permitir a discussão entre os profissionais da área da saúde a cerca do quadro clínico da gestante, entre outras observações;
- Utilizar os dados coletados para análises estatísticas e estudos de pesquisa sobre tendências de saúde materna, incidência de complicações durante a gravidez, eficácia de diferentes cuidados pré e pós-natais, entre outros;

## Tecnologias

- Python 3.11
- Django 5.0
- Django REST Framework 3.14
- PostgreSQL 16.1
- Redis 7.2

## Primeiros passos

Todas as dependências externas (banco de dados e cache) deste projeto estão conteinerizadas no Docker. Deste modo, é interessante que o mesmo esteja instalado e configurado em sua máquina. Abaixo segue os links para as documentações e guias de instalação do Docker e Docker Compose:

_Documentação do Docker e Docker Compose:_

- [Get Started with Docker](https://www.docker.com/get-started)
- [Overview of Docker Compose](https://docs.docker.com/compose/)

_Guia de instalação do Docker e Docker Compose (Ubuntu):_

- [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Executando o sistema localmente

Novamente, é reforçado a utilização do **Docker** e do **Docker Compose** para a execução dos sistemas. Abaixo seguem os comandos que deverão ser executados, em sequência, para que tudo funcione corretamente.

Inicializando as dependências (PostgreSQL, Redis):

```bash
make run/infra/start
```

Executando as migrações do banco de dados:

```bash
make run/infra/database/migrate
```

Criando um superusuário (Opcional):

```bash
make run/api/createsuperuser
```

Iniciando a API (via Docker):

```bash
make run/api/start
```

Caso você queira iniciar a API sem utilizar o Docker, execute os passos abaixo:

```bash
python -m venv env # Criação de uma virtualenv
source env/bin/activate # Ativação da virtualenv
make poetry/setup # Instala o poetry
make poetry/install-dependencies # Instala as bibliotecas
poetry run python app/manage.py runserver # Inicia a API
```
