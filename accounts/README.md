# Django-Quiz

## Descrição

O Django Quiz é um sistema web desenvolvido em Django para a disciplina de Desenvolvimento Web do curso de ADS- Senac Palhoça. 
O sistema permite aos usuários criar, visualizar e votar em enquetes após fazerem login na plataforma.

## Funcionalidades

- Autenticação de Usuário: Os usuários podem se cadastrar, fazer login e logout.
- Criar Enquetes: Os usuários autenticados podem criar suas próprias enquetes, definindo perguntas e opções de resposta.
- Votar em Enquetes: Os usuários podem votar em enquetes existentes.
- Fechar Enquetes: Após o fechamento da enquete, todos os votantes recebem um email informando o resultado final da mesma.

## Tecnologias Utilizadas

- Django 3.2: Framework web em Python para desenvolvimento rápido.
- SQLite: Banco de dados utilizado para armazenamento de dados.
- Python 3.8: Linguagem de programação utilizada para desenvolver a lógica do aplicativo.

## Requisitos de Instalação

- Python 3.8 ou superior
- Django 3.2
- Navegador web moderno (Chrome, Firefox, Safari, etc.)

## Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/django-Quiz.git

Acesse o diretório do projeto:

bash
Copy code
cd django-Quiz
Crie um ambiente virtual (recomendado):

bash
Copy code
python3 -m venv myenv
Ative o ambiente virtual:

bash
Copy code
# No Windows
myenv\Scripts\activate

# No macOS e Linux
source myenv/bin/activate
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute as migrações do Django:

bash
Copy code
python manage.py migrate
Inicie o servidor:

bash
Copy code
python manage.py runserver
Acesse o sistema em seu navegador através do link:

arduino
Copy code
http://localhost:8000/
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request para melhorias, correções de bugs ou novas funcionalidades.

## Autores
Ana Carolina Schmitz da Silva
Gabriel Dutra
Leonardo Vieira Spinosa
João Vinicíus de Aguiar
