import base64
import ctypes
import ctypes.wintypes as wintypes
import os

def test_eicar(filename="eicar.txt"):
    """
    Cria o arquivo EICAR padrão que deve ser detectado por qualquer antivírus.
    """
    eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    try:
        with open(filename, "w") as f:
            f.write(eicar_str)
        print(f"[+] Arquivo EICAR salvo como {filename}")
    except Exception as e:
        print(f"[-] Falha ao criar EICAR: {e}")

def test_suspicious_bytes(filename="nop_payload.bin"):
    """
    Cria um arquivo binário contendo 200 bytes 0x90 (NOP sled), comum em shellcode.
    """
    try:
        with open(filename, "wb") as f:
            f.write(b"\x90" * 200)
        print(f"[+] Payload suspeito salvo como {filename}")
    except Exception as e:
        print(f"[-] Falha ao criar payload: {e}")

def test_openprocess(pid=4):
    """
    Tenta abrir handle para um processo (System Idle) com ALL_ACCESS.
    Deve falhar, mas ativa heurísticas de EDR.
    """
    try:
        PROCESS_ALL_ACCESS = 0x1F0FFF
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if handle:
            print(f"[!] Sucesso inesperado: handle = {handle}")
            ctypes.windll.kernel32.CloseHandle(handle)
        else:
            print("[+] Tentativa de OpenProcess falhou (esperado).")
    except Exception as e:
        print(f"[-] Erro ao tentar OpenProcess: {e}")
