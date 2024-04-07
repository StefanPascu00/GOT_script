import json


def add_user(player_id: str, all_players: dict, path: str = "auth.json") -> dict:
    score = 0
    passwd = ""
    confirm_passwd = " "
    while len(passwd) < 3:
        while passwd != confirm_passwd:
            passwd = input("Introdu parola ta: ")
            confirm_passwd = input("Confirma parola: ")
        if len(passwd) < 3:
            print("Parola e prea scurta")
            passwd = ""
            confirm_passwd = " "

    new_user = {player_id: {"score": 0, "password": passwd, "time": "0"}}
    all_players.update(new_user)
    with open(path, "w") as f:
        f.write(json.dumps(all_players, indent=4))

    return new_user


def login(path: str = "auth.json") -> dict:
    is_new_user = False
    user = input("Logheaza-te: ")
    new_user = {}
    with open(path, "r") as f:
        users = json.loads(f.read())

    if user not in users:
        user_pick = input("Utilizatorul nu exista. Doresti sa te inscri ca nou jucator Y/N: ")
        if user_pick.lower() == "y":
            new_user = add_user(player_id=user, all_players=users)
            is_new_user = True
        else:
            while user not in users:
                user = input("Logheaza-te, utilizatorul nu exista: ")

    if not is_new_user:
        passwd = input("Introdu parola: ")
        counter = 0
        while passwd != users[user]["password"]:
            passwd = input("Parola gresita. Reintrodu parola: ")
            counter += 1
            if counter == 3:
                raise Exception("Parola a fost introdusa de prea multe ori.")
    else:
        return new_user

    return {user: users[user]}
