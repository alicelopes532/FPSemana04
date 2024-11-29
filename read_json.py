import json
file_path = input()

try:
    with open(file_path, "r", encoding = "utf8") as file:
        data = json.load(file)
        print(data)
except Exception:
    print("Ocorreu um erro!")
finally:
    print("Processo concluído")