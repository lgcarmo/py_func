import requests

def faz_get(url: str):
    """
    Faz um GET simples na URL e retorna o conteúdo da resposta.
    """
    try:
        response = requests.get(url)
        return response.text  # ou response.json() se for JSON
    except requests.RequestException as e:
        return f"Erro ao fazer GET: {e}"
