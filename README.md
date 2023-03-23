# Documentação Py-Card
Este projeto é um desafio proposto para uma vaga de tech lead com especialidade em Python

## Contexto geral do projeto
O projeto consiste em uma API REST que permite a criação, listagem e detalhamento de dados de cartão de crédito por usuários autenticados ou não.

## Documentação do projeto
Para maiores detalhes sobre a utilização, é possível consultar a documentação da API no formato SWAGGER ou REDOC. Elas podem ser encontrados no seguinte endereço:
- Swagger: http://localhost:8000/api/swagger/
- Redoc: http://localhost:8000/api/redoc/

## Requisitos
- Requisitos para instalação manual
  - Python 3.10.5
  - Poetry 1.3.1
- Requisitos para instalação com docker
  - Docker
  - Docker-compose

## Instalação com docker
- Faça o clone e acesse a pasta raiz do projeto.
- Faça uma cópia do arquivo `.env.example` e renomeie para `.env`.
  - Não precisa fazer nenhuma alteração, pois o arquivo já está pre configurado para o docker.
- Execute o comando `docker-compose up -d --build`
- Acesse o endereço http://localhost:8001/api/swagger/ para visualizar a documentação da API. (observe que está na porta 8001, diferente da 8000 padrão do django)

## Instalação manual
- Faça o clone e acesse a pasta raiz do projeto.
- Crie um ambiente virtual com o comando `python -m venv .venv`
- Ative o ambiente virtual com o comando `source .venv/bin/activate`
- Instale as dependências com o comando `poetry install`
- Faça uma cópia do arquivo `.env.example` e renomeie para `.env`.
    - O arquivo está previamente configurado para rodar com docker. Para funcionar local, é necessário comentar a linha abaixo do comentário `## Used for docker development` e descomentar a linha abaixo do comentário `## Used for local development`
    - Altere o valor da variável `DEBUG` para `True`, para que sirva os arquivos estáticos em ambiente de desenvolvimento.
- Execute as migrações com o comando `python manage.py migrate`
- Execute o servidor com o comando `python manage.py runserver`
- Acesse o endereço http://localhost:8000/api/swagger/ para visualizar a documentação da API.


## Como testar os requisitos

**Observação**: Caso precise de gerar mais cartões, pode utilizar o site [https://www.4devs.com.br/gerador_de_numero_cartao_credito](https://www.4devs.com.br/gerador_de_numero_cartao_credito)

### Usuário não autenticado
Neste cenário, o usuário não está autenticado.

Ele Consegue executar todas as operações normalmente, porém, os dados de cartão de crédito são exibidos de forma ofuscada.

- Acesse o endereço `/api/swagger/` para visualizar a documentação da API.
- Crie um cartão de crédito com o endpoint POST `/api/v1/cards/` e o seguinte payload:
    ```json
    {
        "number": "4164885674522584",
        "holder": "John Doe",
        "exp_date": "06/2025",
        "cvv": "0829"
    }
    ```
- Liste todos os cartões de crédito com o endpoint GET `/api/v1/cards/`
- Obtenha os detalhes de um cartão de crédito com o endpoint GET `/api/v1/cards/{id}/`

### Usuário autenticado
Neste cenário, o usuário está autenticado.

Ele Consegue executar todas as operações normalmente, porém, os dados de cartão de crédito são exibidos de forma completa.

- Acesse o endereço `/api/swagger/` para visualizar a documentação da API.
- Registre um usuário no endpoint POST `/api/v1/users/` com o seguinte payload:
    ```json
    {
      "email": "user@example.com",
      "password": "strong_password"
    }
  ```
- Faça login no endpoint POST `/api/v1/token/` com o seguinte payload:
    ```json
    {
      "email": "user@example.com",
      "password": "strong_password"
    }
  ```
- Copie o token retornado no campo `access`.
- Clique no campo `Authorize` no canto superior direito e cole o valor no campo `jwtAuth  (http, Bearer)`, clique em `Authorize` e feche a janela.
- Crie um cartão de crédito com o endpoint POST `/api/v1/cards/` e o seguinte payload:
    ```json
    {
        "number": "4652465640157705",
        "holder": "John Doe",
        "exp_date": "12/2024",
        "cvv": "785"
    }
    ```
- Liste todos os cartões de crédito com o endpoint GET `/api/v1/cards/`
- Obtenha os detalhes de um cartão de crédito com o endpoint GET `/api/v1/cards/{id}/`


## Detalhes técnicos interessantes

### Validações
Conforme documentação fornecida, o projeto utiliza a lib [python-creditcard](https://github.com/MaisTodos/python-creditcard) para fazer a validação do número e também descobrir a bandeira do cartão.

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

A cobertura de código está em **99%** e é possível verificar essa infomação executando o comando `pytest --cov --cov-report=html` na raiz do projeto. E em seguida, abir o arquivo `index.html` gerado na pasta `htmlcov`.

### Desacoplamento de variáveis de ambiente
O projeto utiliza uma lib chamada [python-decouple](https://pypi.org/project/python-decouple/) para garantir que as variáveis de ambientes estão isoladas.

Além de que podem ser manipuladas tanto no arquivo `.env` quanto diretamente nas variáveis de ambiente.

### Versionamento de API
A aplicação já está preparada para futuras evoluções onde pode ser necessário criar outras versões da API em caso de "quebra de contrato".

### Interface web para utilização e documentação dos endpoints
O projeto possui duas interfaces, uma com swagger e outra com redoc, para facilitar a utilização e documentação dos endpoints.





