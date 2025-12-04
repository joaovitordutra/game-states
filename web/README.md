# Jogo dos Estados e Capitais — Front-end

Arquivos criados para um layout web standalone (sem backend):

- `index.html` — interface do jogo
- `styles.css` — estilos
- `app.js` — lógica do jogo (dados embutidos)

Como testar localmente

1. Abra `web/index.html` no seu navegador (duplo clique ou `open web/index.html` no macOS).
2. O jogo roda no front-end e não precisa de servidor.

Opções futuras

- Integrar a `jogo_estados.py` via uma API Flask para usar a lógica do Python.
- Adicionar persistência de placares (localStorage ou backend).

Rodando com o backend Flask (opcional)

1. Crie um ambiente virtual e instale dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Rode o servidor (irá servir `web/` e expor `/api/states` e `/api/check`):

```bash
python3 server.py
```

3. Abra `http://127.0.0.1:5000/` no navegador.
