import subprocess

p = subprocess.Popen(["ls", "-la"])
p.wait()
print("result:", p)
