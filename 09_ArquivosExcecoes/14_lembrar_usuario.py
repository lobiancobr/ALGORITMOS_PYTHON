import json

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename, encoding="utf-8") as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Qual é o seu nome? ").strip()
    with open("username.json", "w", encoding="utf-8") as f_obj:
        json.dump(username, f_obj, ensure_ascii=False)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Bem-vindo de volta, {username}!")
    else:
        username = get_new_username()
        print(f"Vamos lembrar de você na próxima vez, {username}!")

greet_user()