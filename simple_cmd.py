import subprocess

def listar_arquivos(caminho="."):
    try:
        resultado = subprocess.run(["ls", caminho], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar arquivos: {e}")
