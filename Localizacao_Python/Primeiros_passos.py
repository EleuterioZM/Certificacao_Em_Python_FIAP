import requests

class Geocodificador:
    def __init__(self, api_key):
        self.api_key = api_key  # Sua chave de API do LocationIQ

    def geocodificar(self, endereco):
        """
        Geocodifica um endereço usando a API do LocationIQ.
        Retorna a latitude e longitude se o endereço for encontrado.
        Caso contrário, retorna None.
        """
        url = "https://us1.locationiq.com/v1/search.php"
        params = {
            'key': self.api_key,
            'q': endereco,
            'format': 'json'
        }

        # Fazendo a requisição
        response = requests.get(url, params=params)

        # Processando a resposta
        if response.status_code == 200:
            dados = response.json()
            if dados:
                latitude = dados[0]['lat']
                longitude = dados[0]['lon']
                return latitude, longitude
            else:
                print("Endereço não encontrado.")
                return None, None
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None, None

    def geocodificar_reverso(self, latitude, longitude):
        """
        Faz a geocodificação reversa (coordenadas para endereço) usando a API do LocationIQ.
        Retorna o endereço correspondente às coordenadas.
        Caso contrário, retorna None.
        """
        url = "https://us1.locationiq.com/v1/reverse.php"
        params = {
            'key': self.api_key,
            'lat': latitude,
            'lon': longitude,
            'format': 'json'
        }

        # Fazendo a requisição
        response = requests.get(url, params=params)

        # Processando a resposta
        if response.status_code == 200:
            dados = response.json()
            if 'display_name' in dados:
                endereco = dados['display_name']
                return endereco
            else:
                print("Coordenadas não encontradas.")
                return None
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None

# Exemplo de uso
if __name__ == "__main__":
    # Substitua pela sua chave de API do LocationIQ
    api_key = "pk.5b812edfd9e6dd013bbc390f439a1f24"
    geocodificador = Geocodificador(api_key)

    # Geocodificar um endereço
    endereco = "Museu de História Natural, Maputo, Moçambique"
    latitude, longitude = geocodificador.geocodificar(endereco)

    if latitude and longitude:
        print(f"Endereço: {endereco}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

        # Geocodificação reversa (opcional)
        endereco_reverso = geocodificador.geocodificar_reverso(latitude, longitude)
        if endereco_reverso:
            print(f"Endereço reverso: {endereco_reverso}")
    else:
        print("Não foi possível geocodificar o endereço.")