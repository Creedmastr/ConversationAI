import time

def panic(message):
    print(f"ERROR: {message}")
    time.sleep(2)
    exit(1)
