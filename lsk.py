import os
import time
import subprocess

BANNER = r"""
  ▄▄▄      ▄▄▄▄▄     ▄▄▄▄   ▄▄▄
 ▀██▀     ██▀▀▀▀█▄  █▀ ██  ██
  ██      ▀██▄  ▄▀     ██ ██
  ██        ▀██▄▄      █████
  ██      ▄   ▀██▄     ██ ██▄
 ████████ ▀██████▀   ▀██▀  ▀██▄
"""

script_map = [
    ("DDos", "ddos.py"),
    ("TempMail", "tempmail.py"),
    ("Option 3", "C.py"),
    ("Option 4", "D.py"),
]

def typewriter(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_banner_menu():
    os.system("clear")
    print("\033[92m" + BANNER + "\033[0m")
    for i, (label, _) in enumerate(script_map, start=1):
        print(f"[{i}] {label}")
    print("[0] Exit\n")

while True:
    show_banner_menu()
    choice = input("Select an option > ")

    if choice == "0":
        os.system("clear")
        typewriter("Exiting...")
        break

    if not choice.isdigit():
        os.system("clear")
        typewriter("Invalid option.")
        time.sleep(1)
        continue

    choice = int(choice)

    if not (1 <= choice <= len(script_map)):
        os.system("clear")
        typewriter("Invalid option.")
        time.sleep(1)
        continue

    label, script_name = script_map[choice - 1]
    script_path = f"program/{script_name}"

    os.system("clear")
    typewriter(f"Running {label}")
    time.sleep(0.5)

    if not os.path.isfile(script_path):
        os.system("clear")
        typewriter(f"Script not found: {script_path}")
        time.sleep(1.3)
        continue

    typewriter("Executing...\n")
    time.sleep(0.4)

    subprocess.run(["python", script_path])
    time.sleep(1)
