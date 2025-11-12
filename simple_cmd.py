import subprocess

def run_ls(path="."):
  result = subprocess.run(["ls", path], text=True, capture_output=True, check=True)
  print(result.stdout, end="")
