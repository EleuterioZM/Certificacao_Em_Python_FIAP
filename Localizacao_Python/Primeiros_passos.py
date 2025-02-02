import requests

# Endereço para geocodificar
endereco = "1600 Amphitheatre Parkway, Mountain View, CA"

# URL da API do Nominatim
url = "https://nominatim.openstreetmap.org/search"
params = {
    'q': endereco,
    'format': 'json'
}

# Cabeçalho personalizado
headers = {
    'User-Agent': 'MeuApp/1.0'  # Substitua por um nome único para seu aplicativo
}

# Fazendo a requisição
response = requests.get(url, params=params, headers=headers)

# Processando a resposta
if response.status_code == 200:
    dados = response.json()
    if dados:
        latitude = dados[0]['lat']
        longitude = dados[0]['lon']
        print(f"Endereço: {endereco}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Endereço não encontrado.")
else:
    print("Erro ao acessar a API:", response.status_code)