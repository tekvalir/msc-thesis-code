import os
import subprocess
import shutil
import time
import csv
import fnmatch

TIMEOUT = 3600

PWD = "."
OUTPUT_FOLDER = "output"
BIN_FOLDER = "bin"

ABACUS = "./Abacus"

PIN_ROOT = "Intel-Pin-Archive"           # Pin archive pulled by Abacus during compilation
QIF_PATH = "QIF-new"                # Name of Abacus' binary
PIN_DIR = "./pintools/obj-ia32"            # directory containing the pintools
PINTOOL = "MI-pintool.so"

# Pintool output files
INST_OUT = "Inst_data.txt"
FUNC_OUT = "Function.txt"

DRY_RUN = False
DEBUG = True

def make_pin_cmd(folder: str, filename: str):
    return [os.path.join(ABACUS, PIN_ROOT, "pin"), "-t", os.path.join(PIN_DIR, PINTOOL), "--", os.path.join(folder, filename)]

def make_qif_cmd(folder: str, filename: str):
    last_folder = folder.split("/")[-1]
    return [os.path.join(ABACUS, QIF_PATH), f"./{INST_OUT}", "-f", f"{FUNC_OUT}", "-o", os.path.join(PWD, OUTPUT_FOLDER, f"{last_folder}-{filename}-res.txt")]

def analyse_file(folder: str, filename: str, summary):
    last_folder = folder.split("/")[-1]
    loc_summary = {}
    print(f"=> Processing {os.path.join(folder, filename)}")
    pin_cmd = make_pin_cmd(folder, filename)
    qif_cmd = make_qif_cmd(folder, filename)
    if DRY_RUN:
        print("==> Pin command")
        print(" ".join(pin_cmd))
        print("==> QIF command")
        print(" ".join(qif_cmd))
        loc_summary["pin-cmd"] = pin_cmd
        loc_summary["qif-cmd"] = qif_cmd
    else:
        print("==> Running pin...")
        start = time.time()
        try:
            proc = subprocess.run(pin_cmd, capture_output=True, shell=False, timeout=TIMEOUT)
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
        else:
            delay = time.time() - start
            loc_summary["abacus_status"] = proc.returncode
            loc_summary["abacus_time"] = delay

        shutil.move(f"{FUNC_OUT}", f"{OUTPUT_FOLDER}/{last_folder}-{filename}-func.txt")
        shutil.move(f"{INST_OUT}", f"{OUTPUT_FOLDER}/{last_folder}-{filename}-inst.txt")

    if DEBUG:
        print(loc_summary)
    summary[f"{last_folder}-{filename}"] = loc_summary

def list_binaries(root_path: str, pattern: str = "*"):
    matched_binaries = []

    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if fnmatch.fnmatch(full_path, pattern):
                matched_binaries.append((dirpath, filename))

    return sorted(matched_binaries)

if __name__ == "__main__":
    summary = {}
    bin_filter = "*AES-BearSSL*"

    # Load summary if existent to update it instead of erasing it
    summary_fp = os.path.join(OUTPUT_FOLDER, f"summary{'-d' if DRY_RUN else ''}.csv")
    if (os.path.exists(summary_fp)):
        with open(summary_fp, 'r', newline='') as summary_file:
            reader = csv.DictReader(summary_file)
            for row in reader:
                name = row.pop("name")
                summary[name] = row

    # Analyse every files
    for folder, filename in list_binaries(os.path.join(PWD, BIN_FOLDER), bin_filter):
        analyse_file(folder, filename, summary)

    # Update the summary
    with open(summary_fp, 'w', newline='') as f:
        fields = ["name"] + list(summary[list(summary)[0]])
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for name in list(summary):
            row = summary[name]
            row["name"] = name
            writer.writerow(row)
