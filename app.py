from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import PyPDF2
import requests

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf"}

HF_API_TOKEN = os.environ.get("HF_API_TOKEN") 
HF_MODEL = "cardiffnlp/twitter-xlm-roberta-base-sentiment"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Funções auxiliares
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def read_file(filepath):
    ext = filepath.rsplit(".", 1)[1].lower()
    text = ""
    if ext == "txt":
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    elif ext == "pdf":
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = "\n".join(page.extract_text() for page in reader.pages)
    return text

def classify_text_hf(text):
    if not HF_API_TOKEN:
        return "Erro: HF_API_TOKEN não definido"

    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": text}
    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL}",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()

        # tratamento para o formato do retorno
        if isinstance(result, list) and len(result) > 0:
            if isinstance(result[0], list):  # [[{...}, {...}]]
                best = max(result[0], key=lambda x: x["score"])
                label = best["label"].lower()
            elif isinstance(result[0], dict):  # [{...}, {...}]
                best = max(result, key=lambda x: x["score"])
                label = best["label"].lower()
            else:
                label = "unknown"
        else:
            label = "unknown"

        if label in ["label_2", "positive"]:
            return "Produtivo"
        elif label in ["label_0", "negative"]:
            return "Improdutivo"
        else:
            return "Improdutivo"

    except Exception as e:
        return f"Erro na classificação: {str(e)}"


# função de classificação por palavras-chave + IA
def classificar_email(texto):
    texto_lower = texto.lower() 
    
    # exemplos de palavras-chave produtivas e  improdutivas
    palavras_produtivas = ["solicitação", "relatório", "atualização", "aprovação", "orçamento", "cadastro",
    "feedback", "corrigir", "documentos", "prazo", "pendência", "atividade"]
    palavras_improdutivas = ["feliz natal", "boas festas", "agradecimento", "happy hour"]
    
    if any(p in texto_lower for p in palavras_produtivas):
        return "Produtivo"
    if any(p in texto_lower for p in palavras_improdutivas):
        return "Improdutivo"

    return classify_text_hf(texto)

def gerar_resposta(categoria):
    respostas = {
        "Produtivo": "Recebido! Vamos processar sua solicitação em breve.",
        "Improdutivo": "Obrigado pelo contato. Desejamos um ótimo dia!"
    }
    return respostas.get(categoria, "")

@app.route("/", methods=["GET", "POST"])
def index():
    category = None
    response = None
    email_text = ""
    
    if request.method == "POST": #se o usuário enviar o formulário...
        #verificando se o arquivo foi enviado ou nao
        if "file" in request.files:
            file = request.files["file"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                email_text = read_file(filepath)

        form_text = request.form.get("email")
        if form_text:
            email_text = form_text
            
        if email_text:
            category = classificar_email(email_text)
            response = gerar_resposta(category)

    return render_template("index.html", email=email_text, category=category, response=response)

# inicialização do Flask
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
