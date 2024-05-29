import subprocess

gitversion = subprocess.check_output("git describe --tags --abbrev=0".split()).decode().strip()

print(f"Setting version to {gitversion}...")

path = "{{packageName}}/_versions.py"

with open(path, "r") as f:
    content = f.read()

content = content.replace('__version__ = "0.0.0"', f'__version__ = "{gitversion}"')

with open(path, "w") as f:
    f.write(content)

print("Done!")
