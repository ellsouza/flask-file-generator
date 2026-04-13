from flask import Flask, send_file

app = Flask(__name__)

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
 body{margin: 0; font-family: Arial, sans-serif; background: linear-gradient(135deg, #dbeafe, #eff6ff); display: flex; justify-content: center; align-items: center; height: 100vh}
.caixa{ background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12); text-align: center; width: 360px;}
h1{color: #1d4ed8; margin-bottom: 10px}
p{color: #475569}
button{background: #2563eb; color: white; border: none; padding: 12px 18px; border-radius: 10px; cursor: pointer; font-size: 16px; margin-top: 15px;}
   button:hover {
                background: #1e40af;
            }

            #resultado {
                margin-top: 20px;
                font-weight: bold;
                color: #0f172a;
            }
        </style>
    </head>
    <body>
    <div class="caixa"><h1>Automação com Python</h1>
    <p>Clique aqui para criar um arquivo .txt</p>
    <a href="/criar-arquivo"><button onclick="window.location.href='/criar-arquivo'">Criar Arquivo</button></a>
    <p id="resultado"></p>
    </div>
    </body>
    </html>
"""

@app.route("/criar-arquivo")
def criar_arquivo():
    with open("arquivo_criado_pelo_python.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Este arquivo foi criado por uma automação em Python.")

    return send_file("arquivo_criado_pelo_python.txt", as_attachment=True)

app.run(debug=True)
