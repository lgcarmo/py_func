import socket
from urllib.parse import urlparse

def resolver_nome(url: str) -> str:
    """
    Recebe uma URL e retorna o endereço IP correspondente.
    """
    try:
        # Extrai o hostname do URL
        parsed = urlparse(url)
        hostname = parsed.hostname or url  # fallback se não tiver esquema (http://)
        
        # Realiza a resolução de nome
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror as e:
        return f"Erro ao resolver o nome: {e}"

