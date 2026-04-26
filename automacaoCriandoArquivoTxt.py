from flask import Flask, send_file, request
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth

app = Flask(__name__)

def _wrap_text(texto: str, *, font_name: str, font_size: int, max_width: float) -> list[str]:
    linhas: list[str] = []

    for linha in (texto or "").splitlines() or [""]:
        if not linha.strip():
            linhas.append("")
            continue

        palavras = linha.split()
        atual = ""

        for palavra in palavras:
            tentativa = palavra if not atual else f"{atual} {palavra}"
            if stringWidth(tentativa, font_name, font_size) <= max_width:
                atual = tentativa
                continue

            if atual:
                linhas.append(atual)
                atual = palavra
                continue

            # Palavra maior que a largura: quebra por caracteres
            pedaco = ""
            for ch in palavra:
                tentativa_ch = pedaco + ch
                if stringWidth(tentativa_ch, font_name, font_size) <= max_width:
                    pedaco = tentativa_ch
                else:
                    if pedaco:
                        linhas.append(pedaco)
                    pedaco = ch
            if pedaco:
                atual = pedaco

        if atual:
            linhas.append(atual)

    return linhas


@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Criar Arquivo com Python</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
    min-height: 100vh;
}
.pagina {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 24px;
    box-sizing: border-box;
}
.caixa {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
    text-align: center;
    width: 360px;
}
h1 {
    color: #1d4ed8;
    margin-bottom: 10px;
}
p {
    color: #475569;
}
input, textarea {
    width: 300px;
    max-width: 100%;
    padding: 10px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 15px;
    box-sizing: border-box;
    resize: vertical;
}
button {
    display: block;
    background: #2563eb;
    color: white;
    border: none;
    padding: 12px 18px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 16px;
    margin: 15px auto 0;
    width: 200px;
    max-width: 100%;
}
button:hover {
    background: #1e40af;
}
#resultado {
    margin-top: 20px;
    font-weight: bold;
    color: #0f172a;
}
footer {
    margin-top: 20px;
    text-align: center;
    color: #475569;
    font-size: 14px;
}
footer a {
    color: #1d4ed8;
    text-decoration: none;
    font-weight: bold;
}
</style>
</head>

<body>
<div class="pagina">
    <div class="caixa">
        <h1>Automação com Python</h1>
        <p>Digite um texto para o seu arquivo (.txt):</p>

        <textarea id="texto_usuario" placeholder="Digite aqui" rows="5"></textarea>

        <button onclick="baixarTxt()">Baixar TXT</button>
        <button onclick="baixarPdf()">Baixar PDF</button>

        <p id="resultado"></p>
    </div>

    <footer>
        Feito por <a href="https://ellsouza.github.io/ellen-portfolio/" target="_blank">Ellen Souza</a>
    </footer>
</div>

<script>
function baixarTxt() {
    const texto = document.getElementById("texto_usuario").value;
    window.location.href = "/criar-arquivo?texto=" + encodeURIComponent(texto);
}

function baixarPdf() {
    const texto = document.getElementById("texto_usuario").value;
    window.location.href = "/criar-pdf?texto=" + encodeURIComponent(texto);
}
</script>

</body>
</html>
"""


@app.route("/criar-arquivo")
def criar_arquivo():
    texto = request.args.get("texto", "")

    with open("arquivo_criado_pelo_python.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

    return send_file("arquivo_criado_pelo_python.txt", as_attachment=True)


@app.route("/criar-pdf")
def criar_pdf():
    texto = request.args.get("texto", "")

    page_width, page_height = A4
    margin = 50
    font_name = "Helvetica"
    font_size = 12
    line_height = 16

    pdf = canvas.Canvas("arquivo_criado_pelo_python.pdf", pagesize=A4)
    pdf.setFont(font_name, font_size)

    max_width = page_width - (2 * margin)
    x = margin
    y = page_height - margin

    for linha in _wrap_text(texto, font_name=font_name, font_size=font_size, max_width=max_width):
        if y < margin:
            pdf.showPage()
            pdf.setFont(font_name, font_size)
            y = page_height - margin

        if linha == "":
            y -= line_height
            continue

        pdf.drawString(x, y, linha)
        y -= line_height
    pdf.save()

    return send_file("arquivo_criado_pelo_python.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

