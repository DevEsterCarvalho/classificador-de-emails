# Classificador de E-mails

## Descrição

Esta é uma aplicação simples de classificação de e-mails, desenvolvida para um case prático de trainee/dev júnior.  
Ela permite que o usuário insira o corpo de um e-mail e receba a classificação da mensagem (produtivo ou improdutivo), além de uma resposta sugerida.

> **Observação:** Todos os e-mails usados como exemplos são **fictícios**.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask** (microframework web)
- **Hugging Face Transformers** (para classificação de e-mails via IA)
- **HTML5** e **Jinja2** para template
- **CSS puro** para estilização
- Estrutura de pastas organizada (`src/`, `templates/`, `static/`, `data/`)

---

## Abordagem de Classificação

Este projeto classifica e-mails em duas categorias:

1. Regras por palavra-chave

- **Produtivo** : relacionados a tarefas, solicitações, relatórios, reuniões.
- **Improdutivo**: mensagens sociais, saudações, felicitações, ou de pouco valor prático.

2. **Classificação por IA (sentimento):**  
   Caso não haja palavras-chave, a aplicação utiliza o modelo `lipaoMai/bert-sentiment-model-portuguese` da Hugging Face para analisar o sentimento do texto.  
   `positive` ou `neutral` = **Produtivo**
   `negative` = **Improdutivo**

---

## Estrutura do Projeto

src/  
├─ app.py
├─ templates/  
│ └─ index.html # Template HTML  
└─ static/  
└─ css/  
└─ style.css  
data/  
└─ exemplos_emails.txt
README.md
requirements.txt

## Pré-requisitos

- Python 3.8 ou superior
- Pip instalado
- Arquivo `requirements.txt` com as dependências principais

---

## Dependências principais

- Flask
- Transformers
- Torch

As dependências podem ser instaladas via:

`pip install -r requirements.txt`

## Como Executar Localmente

1. Clone este repositório:

```bash
git clone <https://github.com/DevEsterCarvalho/classificador-de-emails.git>
```

2. Entre na pasta do projeto (o nome pode variar dependendo de como você clonou o repositório)
   Por exemplo:

```
cd classificador-de-emails
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
python src/app.py
```

5. Abra seu navegador e acesse:

```
http://127.0.0.1:5000/
```

---

## Observações

- A classificação é realizada **via IA**, usando o modelo `lipaoMai/bert-sentiment-model-portuguese` da Hugging Face.
- A aplicação sugere respostas automáticas de acordo com a categoria do e-mail.
- O CSS está localizado em `src/static/css/style.css` e é referenciado corretamente via Flask usando `url_for('static', filename='css/style.css')`.

- Esta aplicação é uma demonstração de boas práticas de estrutura de projeto, separação de código e organização de arquivos estáticos/templates.

---

## Demonstração visual

![Demonstração geral da aplicação](https://drive.google.com/uc?export=view&id=1pSOcqTaRYUJ_bD1wi5yFa7Fwwiix0omi)

![Demonstração com e-mail produtivo](https://drive.google.com/uc?export=view&id=1wcgPkC84eAF4PN9WGUlFmuOnOCimMsNV)

![Demonstração com e-mail improdutivo](https://drive.google.com/uc?export=view&id=1v35aLj3vquE_Vkk_uAC0LmYZAMsUdKyR)

---

## Contato

- Desenvolvido por: **[Ester Carvalho Dias]**

- Email: **[estercarvalho205@gmail.com]**
- GitHub: **[https://github.com/DevEsterCarvalho]**
- Linkedin: **[https://www.linkedin.com/in/estercarvalho/]**
