# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python, praticando conceitos de rotas, métodos HTTP e manipulação de dados.

## 📝 Tasks

### 🛠️ Criar uma API de Gerenciamento de Itens

#### Description
Implemente uma API REST que permita cadastrar, listar, buscar e remover itens de uma lista em memória.

#### Requirements
Completed program should:

- Utilizar o framework FastAPI
- Permitir adicionar um novo item via método POST
- Permitir listar todos os itens via método GET
- Permitir buscar um item pelo ID via método GET
- Permitir remover um item pelo ID via método DELETE
- Utilizar uma estrutura de dados em memória (ex: lista ou dicionário)

Exemplo de endpoints:

- `POST /items` para adicionar um item
- `GET /items` para listar todos os itens
- `GET /items/{id}` para buscar um item específico
- `DELETE /items/{id}` para remover um item

### 🛠️ (Opcional) Adicionar Validação e Documentação

#### Description
Implemente validações nos dados recebidos e explore a documentação automática gerada pelo FastAPI.

#### Requirements
Completed program should:

- Validar campos obrigatórios ao cadastrar um item
- Utilizar tipos de dados do Pydantic
- Acessar a documentação automática em `/docs`
