import json
import GOT


def initialise_config(path: str) -> dict:
    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except Exception as e:
        print(f"Unable to initialise project {e}.")
        exit(1)
    return config


if __name__ == '__main__':
    config = initialise_config("config.json")
    score = 0
    while True:
        character_num = int(input("Introduceti un numar intre 1 si 999 sau 0 pentru exit: "))
        if 0 < character_num < 1000:
            character_dict = GOT.get_character_dict(config['url_character'], character_num)
            score += GOT.character_name(character_dict)
        if character_num == 0:
            break

    print(score)