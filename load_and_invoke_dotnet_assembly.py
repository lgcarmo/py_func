import base64
import clr  # pythonnet
from System.IO import MemoryStream
from System.Reflection import Assembly
from System import Array, String

def load_and_invoke_dotnet_assembly(b64_string, full_class_name, method_name, args=[]):
    """
    Carrega um assembly .NET em memória a partir de uma string base64 e executa um método estático.
    
    :param b64_string: string Base64 com o conteúdo do assembly .NET (DLL)
    :param full_class_name: nome completo da classe, ex: "Rubeus.Program"
    :param method_name: nome do método a ser invocado, ex: "Main"
    :param args: lista de argumentos como strings
    """
    try:
        print("[+] Decodificando Base64...")
        assembly_bytes = base64.b64decode(b64_string)

        print("[+] Carregando assembly em memória...")
        stream = MemoryStream(assembly_bytes)
        assembly = Assembly.Load(stream.ToArray())

        print(f"[+] Obtendo tipo: {full_class_name}")
        tipo = assembly.GetType(full_class_name)

        print(f"[+] Invocando método: {method_name} com argumentos: {args}")
        metodo = tipo.GetMethod(method_name)

        # Converter lista de argumentos Python para System.String[]
        net_args = Array[String](args)
        metodo.Invoke(None, [net_args])

    except Exception as e:
        print(f"[-] Erro ao executar assembly .NET: {e}")
