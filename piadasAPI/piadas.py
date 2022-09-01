from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def piadaAPI():
    with open('piadas.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)

    print(dados)