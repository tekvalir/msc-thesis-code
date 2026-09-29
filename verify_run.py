import subprocess
from run_benchmark import list_binaries

if __name__ == "__main__":
    for folder, filename in list_binaries("./bin", "*AES*"):
        print(filename)
        subprocess.run(f"{folder}/{filename}")
