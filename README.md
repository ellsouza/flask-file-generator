# Flask File Generator

Aplicação web simples desenvolvida com Python e Flask para gerar arquivos `.txt` e `.pdf` a partir de um texto inserido pelo usuário.

## Funcionalidades

- Entrada de texto pelo usuário na interface
- Geração de arquivo `.txt` com o conteúdo informado
- Geração de arquivo `.pdf` com o mesmo conteúdo
- Download automático dos arquivos

## Tecnologias utilizadas

- Python
- Flask
- HTML e CSS
- ReportLab (para geração de PDF)

## Estrutura do projeto

├── automacaoCriandoArquivoTxt.py
├── requirements.txt
└── README.md

## Como executar o projeto

1. Clone o repositório: `git clone https://github.com/ellsouza/flask-file-generator.git`
2. Entre na pasta do projeto: `cd flask-file-generator`
3. Instale as dependências: `pip install -r requirements.txt`
4. Rode o servidor: `python automacaoCriandoArquivoTxt.py`
5. Acesse no navegador: `http://127.0.0.1:5000`
