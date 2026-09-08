import os
import subprocess
import re
import shutil
import time

TIMEOUT = 3600

PWD = "."
OUTPUT_FOLDER = "output"
BIN_FOLDER = "bin"

ABACUS = "/abacus"

PIN_ROOT = "Intel-Pin-Archive"           # Pin archive pulled by Abacus during compilation
QIF_PATH = "QIF-new"                # Name of Abacus' binary
PIN_DIR = "Pintools/obj-ia32"            # directory containing the pintools

# Pintool output files
INST_OUT = "Inst_data.txt"
FUNC_OUT = "Function.txt"

DRY_RUN = False
DEBUG = True

def make_pin_cmd(folder: str, filename: str):
    return [os.path.join(ABACUS, PIN_ROOT, "pin"), "-t", os.path.join(ABACUS, PIN_DIR, "MyPinToolLinux.so"), "--", os.path.join(PWD, BIN_FOLDER, folder, filename)]

def make_qif_cmd(folder: str, filename: str):
    last_folder = folder.split("/")[-1]
    return [os.path.join(ABACUS, QIF_PATH), f"{INST_OUT}", "-f", f"{FUNC_OUT}", "-d", os.path.join(PWD, BIN_FOLDER, folder, filename), "-o", "result.txt"]

def analyse_file(folder: str, filename: str, summary):
    loc_summary = {}
    print(f"=> Processing {os.path.join(folder, filename)}")
    pin_cmd = make_pin_cmd(folder, filename)
    qif_cmd = make_qif_cmd(folder, filename)
    if DRY_RUN:
        print("==> Pin command")
        print(" ".join(pin_cmd))
        print("==> QIF command")
        print(" ".join(qif_cmd))
    else:
        print("==> Running pin...")
        start = time.time()
        try:
            proc = subprocess.run(pin_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, timeout=TIMEOUT)
        except subprocess.TimeoutExpired as e:
            delay = time.time() - start
            loc_summary["abacus_status"] = None
            loc_summary["abacus_time"] = None
            loc_summary["pin_status"] = 124
            loc_summary["pin_time"] = delay
            print("====> Pin timeout")
            return # Pin timeout, we can end processing
        else:
            delay = time.time() - start
            loc_summary["pin_status"] = proc.returncode
            loc_summary["pin_time"] = delay

        print("==> Running QIF...")
        start = time.time()
        try:
            proc = subprocess.run(qif_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT-delay)
        except subprocess.TimeoutExpired as e:
            delay = time.time() - start
            loc_summary["abacus_status"] = 124
            loc_summary["abacus_time"] = delay
            print("====> QIF timeout")
            shutil.move("result.txt",  os.path.join(PWD, OUTPUT_FOLDER, f"{last_folder}-{filename}-res.txt"))
        else:
            delay = time.time() - start
            loc_summary["abacus_status"] = proc.returncode
            loc_summary["abacus_time"] = delay

        if DEBUG:
            print(loc_summary)

        last_folder = folder.split("/")[-1]
        summary[f"{last_folder}-{filename}"] = loc_summary
        shutil.move(f"{FUNC_OUT}", f"{OUTPUT_FOLDER}/{last_folder}-{filename}-func.txt")
        shutil.move(f"{INST_OUT}", f"{OUTPUT_FOLDER}/{last_folder}-{filename}-inst.txt")

if __name__ == "__main__":
    summary = {}
    for folder in os.listdir(os.path.join(PWD, BIN_FOLDER)):
        fp = os.path.join(PWD, BIN_FOLDER, folder)
        if os.path.isdir(fp) == True:
            for bin_file in os.listdir(fp):
                analyse_file(folder, bin_file, summary)

    print(summary)
