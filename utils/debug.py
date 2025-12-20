import time

DEBUG = 0 # 1 -> open, 0 -> close

def log(level, module, message):
    if DEBUG:
        print(f"[{time.strftime('%H:%M:%S')}] [{level}] [{module}] {message}")

# INFO, DEBUG, WARN, ERROR, SAVE, LOAD