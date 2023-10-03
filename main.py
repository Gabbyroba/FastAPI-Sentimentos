from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import random

app = FastAPI()

# Defina as origens permitidas
origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500/",
    "http://127.0.0.1:5500/index.html",
    "https://feelingyou.netlify.app",
]

# Configurar o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client_id = '88280c7374b446b39db78a9bd3bf3ca8'
client_secret = '72ee752dee1146e4b1c6ac80cc1947c2'

# Autenticação para obter um token de acesso
token_url = 'https://accounts.spotify.com/api/token'

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

# Faça a solicitação POST para obter o token de acesso
response = requests.post(token_url, data=data)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # O token de acesso está no campo 'access_token' na resposta JSON
    token_data = response.json()
    access_token = token_data['access_token']
    print(f'Token de acesso: {access_token}')
else:
    print('Falha ao obter o token de acesso')

# Mapeamento de sentimentos para gêneros musicais
sentimentos_para_generos = {
    "Tristeza": "sad",
    "Nostalgia": "nostalgic",
    "Canseirinha": "chill",
    "Felicidade": "happy",
    "Dançante": "dance",
    "Melancolia": "melancholic",
    "K-poper": "k-pop",
}

@app.get("/")
async def definir_home():
    return('Boas vindas à API feeling you!')

@app.post("/analisar-sentimento")
async def analisar_sentimento(data: dict):
    sentimentos = data.get("sentimento", "").split(', ')
    musicas_sugeridas = []

    for sentimento in sentimentos:
        genero = sentimentos_para_generos.get(sentimento, "pop")  # Use "pop" como gênero padrão se não estiver mapeado
        params = {
            'q': f"genre:{genero}",
            'type': 'track',
            'limit': 50  # Aumente o limite para obter mais resultados
        }

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(search_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            tracks = data['tracks']['items']
            if tracks:
                # Selecionar aleatoriamente uma música entre os resultados
                musica_sugerida = random.choice(tracks)['name']
                musicas_sugeridas.append(f"{sentimento}: {musica_sugerida}")
            else:
                musicas_sugeridas.append(f"Não foi encontrada uma música para {sentimento}")
        else:
            musicas_sugeridas.append(f"Erro ao buscar música para {sentimento}")

    if musicas_sugeridas:
        return {"sentimentos": sentimentos, "musicas_sugeridas": musicas_sugeridas}
    else:
        return {"erro": "Não foi possível encontrar músicas para os sentimentos especificados"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
