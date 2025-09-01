# Classificador de E-mails

## Descrição

Esta é uma aplicação simples de classificação de e-mails, desenvolvida para um case prático de dev júnior.  
Ela permite que o usuário insira o corpo de um e-mail e receba a classificação da mensagem (produtivo ou improdutivo), além de uma resposta sugerida.

> **Observação:** Todos os e-mails usados como exemplos são **fictícios**.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask** (microframework web)
- **Requests** (para comunicação com API Hugging Face)
- **Hugging Face Transformers** (para classificação de e-mails via IA)
- **HTML5** e **Jinja2** para templates
- **CSS puro** para estilização
- Estrutura de pastas organizada (`templates/`, `static/`, `data/`)

---

## Abordagem de Classificação

Este projeto classifica e-mails em duas categorias:

1. Regras por palavra-chave

- **Produtivo** : relacionados a tarefas, solicitações, relatórios, reuniões.
- **Improdutivo**: mensagens sociais, saudações, felicitações, ou de pouco valor prático.

2. **Classificação por IA (sentimento):**  
   Caso não haja palavras-chave, a aplicação utiliza o modelo `cardiffnlp/twitter-xlm-roberta-base-sentiment` via Hugging Face Inference API para analisar o sentimento do texto.

   - label_2 / positive → **Produtivo**

   - label_0 / negative → **Improdutivo**

---

## Estrutura do Projeto

app.py
templates/
└─ index.html
static/
└─ css/
└─ style.css
data/
└─ exemplos_emails.txt
Procfile
README.md
requirements.txt
uploads

## Pré-requisitos

- Python 3.8 ou superior
- Pip instalado
- Hugging Face API Token configurado como variável de ambiente HF_API_TOKEN
- Arquivo `requirements.txt` com as dependências principais

---

## Dependências principais

- Flask
- Transformers
- PyPDF2
- Werkzeug

As dependências podem ser instaladas via:

`pip install -r requirements.txt`

## Como Executar Localmente

1. Clone este repositório:

```bash
git clone https://github.com/DevEsterCarvalho/classificador-de-emails.git
```

2. Entre na pasta do projeto (o nome pode variar dependendo de como você clonou o repositório)
   Por exemplo:

```
cd classificador-de-emails
```

3. Configure a variável de ambiente HF_API_TOKEN (há um passo a passo no final do documento):

```
export HF_API_TOKEN="seu_token_aqui"  # Linux / macOS
set HF_API_TOKEN=seu_token_aqui   # Windows

```

4. Instale as dependências:

```
pip install -r requirements.txt
```

5. Execute a aplicação:

```
python app.py
```

6. Abra seu navegador e acesse:

```
http://127.0.0.1:5000/
```

---

Link Online da Aplicação

A aplicação está hospedada no Elastic Beanstalk da AWS

[Elastic Beanstalk App](http://classificado-de-email-env.eba-ziaybmem.us-east-2.elasticbeanstalk.com/)

---

## Observações

- A classificação é realizada **via IA**, usando o modelo `cardiffnlp/twitter-xlm-roberta-base-sentiment` da Hugging Face API.
- A aplicação sugere respostas automáticas de acordo com a categoria do e-mail.
- O CSS está localizado em `static/css/style.css` e é referenciado corretamente via Flask usando `url_for('static', filename='css/style.css')`.

- Esta aplicação é uma demonstração de boas práticas de estrutura de projeto, separação de código e organização de arquivos estáticos/templates.

---

## Demonstração visual

![Demonstração geral da aplicação](https://drive.google.com/uc?export=view&id=1pSOcqTaRYUJ_bD1wi5yFa7Fwwiix0omi)

![Demonstração com e-mail produtivo](https://drive.google.com/uc?export=view&id=1wcgPkC84eAF4PN9WGUlFmuOnOCimMsNV)

![Demonstração com e-mail improdutivo](https://drive.google.com/uc?export=view&id=1v35aLj3vquE_Vkk_uAC0LmYZAMsUdKyR)

---

## Configuração do Token da Hugging Face (HF_API_TOKEN)

Para que a aplicação funcione localmente usando o modelo `cardiffnlp/twitter-xlm-roberta-base-sentiment`, é necessário gerar um **token de acesso** no Hugging Face e configurá-lo como variável de ambiente.

### 1. Gerar o Token

1. Acesse [Hugging Face](https://huggingface.co/) e faça login ou crie uma conta.
2. Clique na sua foto de perfil > **Settings** > **Access Tokens**.
3. Clique em **New token**.
4. Escolha um nome (ex: `local-classificador`) e a permissão **read**.
5. Clique em **Generate** e copie o token gerado.

---

### 2️. Configurar a Variável de Ambiente

#### **Linux / macOS**

```bash
export HF_API_TOKEN="seu_token_aqui"
```

Para verificar:

```bash
echo $HF_API_TOKEN
```

**Windows (cmd)**

```bash
set HF_API_TOKEN=seu_token_aqui`
```

Para verificar:

```bash
echo %HF_API_TOKEN%`
```

**Windows (PowerShell)**

```bash
$env:HF_API_TOKEN="seu_token_aqui"
```

Para verificar:

```bash
echo $env:HF_API_TOKEN`
```

⚠️ Observação: A variável de ambiente precisa estar configurada antes de rodar a aplicação.
Após configurar a variável, instale as dependências e execute o projeto.

---

## Contato

- Desenvolvido por: **[Ester Carvalho Dias]**

- Email: **[estercarvalho205@gmail.com]**
- GitHub: **[https://github.com/DevEsterCarvalho]**
- Linkedin: **[https://www.linkedin.com/in/estercarvalho/]**
