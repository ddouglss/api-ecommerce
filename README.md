
# 🛒 E-commerce API (Flask)

API REST para gerenciamento de produtos de um e-commerce, construída com Flask, SQLAlchemy, Flask-Login, Flask-CORS e documentada com Swagger (Flasgger).
Suporta autenticação de usuários e CRUD completo de produtos.


## ⚙️ Tecnologias utilizadas

- Python 3

- Flask

- Flask-SQLAlchemy

- Flask-Login

- Flask-CORS

- Flasgger (Swagger UI)



## 🚀 Como rodar o projeto

#### Clonar o repositório

```bash
  git clone https://github.com/seu-usuario/api-flask-ecommerce.git
  cd api-flask-ecommerce
```

Criar e ativar ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instalar dependências
```bash
pip install -r requirements.txt
```

4. Rodar a aplicação
```bash
python app.py
```

A API estará disponível em:
👉 http://127.0.0.1:5000

Swagger UI (documentação):
👉 http://127.0.0.1:5000/apidocs

    
## 🔑 Autenticação

- Usuários devem estar logados para acessar as rotas de criação, deleção e atualização de produtos.

- O login é feito com username e password.

- Após logar, a sessão fica ativa.
## 📌 Endpoints principais

#### 👤 Autenticação

- POST /login → login de usuário

- POST /logout → logout do usuário

#### 🛒 Produtos

- POST /api/products/add → adicionar produto (login obrigatório)

- DELETE /api/products/delete/<id> → deletar produto (login obrigatório)

- PUT /api/products/update/<id> → atualizar produto (login obrigatório)

- GET /api/products/<id> → buscar detalhes de um produto

- GET /api/products → listar todos os produtos

## Autor
#### Douglas Souza Silva
- Linkedin : https://www.linkedin.com/in/ddouglss/
