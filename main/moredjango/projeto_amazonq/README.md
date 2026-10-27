# 📊 Dashboard Amazon Q

Dashboard interativo com gráficos e MySQL criado pela Amazon Q.

## 🚀 Como usar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar MySQL
Edite o arquivo `dashboard_site/settings.py` na seção DATABASES:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seu_banco_aqui',     # ← SEU BANCO
        'USER': 'root',               # ← SEU USUÁRIO
        'PASSWORD': 'sua_senha',      # ← SUA SENHA
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Criar tabelas no banco
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Rodar o servidor
```bash
python manage.py runserver
```

### 5. Acessar
Abra: http://127.0.0.1:8000

## 📈 Funcionalidades

- **Dashboard Principal**: Gráficos interativos de vendas
- **Gerenciar Dados**: Tabelas com CRUD completo
- **Adicionar/Editar**: Formulários para vendas
- **API**: Endpoints JSON para gráficos

## 🎯 Páginas

- `/` - Dashboard principal com gráficos
- `/gerenciar/` - Gerenciar dados
- `/adicionar/` - Adicionar nova venda
- `/api/vendas/` - API dados de vendas
- `/api/produtos/` - API dados de produtos

## 🛠️ Tecnologias

- Django 5.0.6
- MySQL
- Chart.js (gráficos)
- Bootstrap 5 (design)
- JavaScript (interatividade)

## 📊 Estrutura do Banco

### Tabela: dados_venda
- id (auto)
- produto (varchar)
- quantidade (int)
- preco (decimal)
- data_venda (date)
- vendedor (varchar)

### Tabela: usuarios_sistema
- id (auto)
- nome (varchar)
- email (email)
- data_cadastro (datetime)
- ativo (boolean)

---
**Criado por Amazon Q** 🤖