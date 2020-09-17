
from pathlib import Path

# Absolute path
# Relative path

'''path = Path("email")
print(path.exists())
path.mkdir()'''

path = Path(".")
for file in path.glob("*"):
    print(file)
