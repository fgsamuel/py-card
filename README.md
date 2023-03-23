# Documentação Py-Card
Este projeto é um desafio proposto para uma vaga de tech lead com especialidade em Python

## Contexto geral do projeto
O projeto consiste em uma API REST que permite a criação, listagem e detalhamento de dados de cartão de crédito por usuários autenticados ou não.

## Documentação do projeto
Para maiores detalhes sobre a utilização, é possível consultar a documentação da API no formato SWAGGER ou REDOC. Elas podem ser encontrados no seguinte endereço:
- Swagger: http://localhost:8000/api/swagger/
- Redoc: http://localhost:8000/api/redoc/

## Requisitos
### Instalação manual
- Python 3.10.5
- Poetry 1.3.1
## Instalação com docker
- Docker
- Docker-compose

## Instalação com docker
- Faça o cone do projeto e acesse a pasta raiz do projeto.
- Faça uma cópia do arquivo `.env.example` e renomeie para `.env`. O arquivo já está pre configurado para o docker.
- Execute o comando `docker-compose up -d --build`

## Instalação manual
- Faça o clone do projeto e acesse a pasta raiz do projeto.
- Crie um ambiente virtual com o comando `python -m venv .venv`
- Ative o ambiente virtual com o comando `source .venv/bin/activate`
- Instale as dependências com o comando `poetry install`
- Faça uma cópia do arquivo `.env.example` e renomeie para `.env`. Em seguida, altere as variáveis que julgar necessário.
- Altere o apontamento do banco de dados para um arquivo local. Está comentado lá no arquivo `.env`.
- Execute as migrações com o comando `python manage.py migrate`
- Crie um usuário administrador com o comando `python manage.py createsuperuser`
- Execute o servidor com o comando `python manage.py runserver`
- Acesse o endereço http://localhost:8000/api/swagger/ para visualizar a documentação da API.
- Acesse o endereço http://localhost:8000/admin/ para acessar a interface administrativa. 


## Detalhes técnicos

### Autenticação
O projeto utiliza autenticação com JWT.

Diferente do convencional do framework django, o projeto faz autenticação com um modelo customizado que utiliza o **email** ao invés de **username**.

### Proteção de dados sensíveis
O projeto é uma biblioteca pública que exibe os dados de forma ofuscada para usuários não autenticados, e exibe todos os dados para os usuários autenticados.

### Padrão e qualidade de código
O projeto utiliza bibliotecas como pre-commit, mypy, black, flake8, isort e pydocstyle para garantir a qualidade e estilo padronizado código.

Isto facilita a leitura, manutenção, evolução e também resolução de conflitos em equipes maiores.

### Testes
O projeto utiliza a biblioteca pytest e pytest-django para garantir a qualidade do código.

A cobertura de código está **acima dos 95%** e é possível verificar os resultados executando o comando `pytest --cov --cov-report=html` na raiz do projeto. E em seguida, abir o arquivo `index.html` gerado na pasta `htmlcov`.

### Desacoplamento de variáveis de ambiente
O projeto utiliza uma lib para garantir que as variáveis de ambientes estão isoladas.

Além de que podems ser manipuladas tanto no arquivo `.env` quanto diretamente nas variáveis de ambiente.

### Versionamento de API
A aplicação já está preparada para futuras evoluções onde pode ser necessário criar outras versões da API em caso de "quebra de contrato".

### Interface web para utilização e documentação dos endpoints
O projeto possui duas interfaces, uma com swagger e outra com redoc, para facilitar a utilização e documentação dos endpoints.





