import subprocess

if __name__ == '__main__':
    while True:
        try:
            # subprocess.run(["/home/str/5sah/.venv/bin/python", "/home/str/5sah/start_all_bot.py"])
            subprocess.run(["/home/str/5sah/.venv/bin/python", r"/home/str/5sah/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
