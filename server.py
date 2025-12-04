from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import random

app = Flask(__name__, static_folder='web', static_url_path='')
CORS(app)

STATES = [
    { 'state': 'Acre', 'capital': 'Rio Branco' },
    { 'state': 'Alagoas', 'capital': 'Maceió' },
    { 'state': 'Amapá', 'capital': 'Macapá' },
    { 'state': 'Amazonas', 'capital': 'Manaus' },
    { 'state': 'Bahia', 'capital': 'Salvador' },
    { 'state': 'Ceará', 'capital': 'Fortaleza' },
    { 'state': 'Distrito Federal', 'capital': 'Brasília' },
    { 'state': 'Espírito Santo', 'capital': 'Vitória' },
    { 'state': 'Goiás', 'capital': 'Goiânia' },
    { 'state': 'Maranhão', 'capital': 'São Luís' },
    { 'state': 'Mato Grosso', 'capital': 'Cuiabá' },
    { 'state': 'Mato Grosso do Sul', 'capital': 'Campo Grande' },
    { 'state': 'Minas Gerais', 'capital': 'Belo Horizonte' },
    { 'state': 'Pará', 'capital': 'Belém' },
    { 'state': 'Paraíba', 'capital': 'João Pessoa' },
    { 'state': 'Paraná', 'capital': 'Curitiba' },
    { 'state': 'Pernambuco', 'capital': 'Recife' },
    { 'state': 'Piauí', 'capital': 'Teresina' },
    { 'state': 'Rio de Janeiro', 'capital': 'Rio de Janeiro' },
    { 'state': 'Rio Grande do Norte', 'capital': 'Natal' },
    { 'state': 'Rio Grande do Sul', 'capital': 'Porto Alegre' },
    { 'state': 'Rondônia', 'capital': 'Porto Velho' },
    { 'state': 'Roraima', 'capital': 'Boa Vista' },
    { 'state': 'Santa Catarina', 'capital': 'Florianópolis' },
    { 'state': 'São Paulo', 'capital': 'São Paulo' },
    { 'state': 'Sergipe', 'capital': 'Aracaju' },
    { 'state': 'Tocantins', 'capital': 'Palmas' }
]

def normalize(text: str) -> str:
    import unicodedata
    if text is None:
        return ''
    nfkd = unicodedata.normalize('NFKD', text)
    return nfkd.encode('ASCII', 'ignore').decode('utf-8').strip().lower()


@app.route('/')
def index():
    return send_from_directory('web', 'index.html')


@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('web', path)


@app.route('/api/states', methods=['GET'])
def api_states():
    shuffled = STATES[:]
    random.shuffle(shuffled)
    return jsonify({'ok': True, 'states': shuffled})


@app.route('/api/check', methods=['POST'])
def api_check():
    data = request.get_json() or {}
    state = data.get('state')
    answer = data.get('answer', '')
    if not state:
        return jsonify({'ok': False, 'error': 'state is required'}), 400
    capital = next((s['capital'] for s in STATES if s['state'] == state), None)
    if capital is None:
        return jsonify({'ok': False, 'error': 'unknown state'}), 404
    correct = normalize(capital)
    given = normalize(answer)
    return jsonify({'ok': True, 'correct': given == correct, 'capital': capital})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
