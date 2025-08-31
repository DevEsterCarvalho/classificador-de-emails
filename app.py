from transformers import pipeline
from flask import Flask, render_template, request

app = Flask(__name__)

classifier = pipeline(
    "text-classification",
    model="pysentimiento/robertuito-base-uncased",
    device=-1
)
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
    
    resultado = classifier(texto)[0]
    label = resultado['label'].lower()
    # label pode ser 'POS', 'NEG' ou 'NEU'
    if label in ["pos", "positive"]:
        return "Produtivo"
    elif label in ["neg", "negative"]:
        return "Improdutivo"
    else:  # neutral
        return "Improdutivo"

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
        email_text = request.form["email"]
        category = classificar_email(email_text)
        response = gerar_resposta(category)
    
    return render_template("index.html", email=email_text, category=category, response=response)

# inicialização do Flask
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
