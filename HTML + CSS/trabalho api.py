from flask import flask

app = Flask('Piadas')

app.route('/piadas', methods={'GET'})
def piada():
    return {'piada' : 'O que o pato disse para a pata?R.: Vem Quá!'}

app.run