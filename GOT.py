import json
import requests


def get_character_dict(url: str, character_number: int):
    try:
        response = requests.get(url + str(character_number))
        if response.status_code == 200:
            character_dict = json.loads(response.text)
            if character_dict.get('error'):
                raise Exception(f"Ceva nu a functionat bine.")
            return character_dict

        else:
            raise Exception(f"Something wrong with the api\n"
                            f"Code: {response.status_code}\n"
                            f"Message: {response.text}")
    except Exception as e:
        print(e)


def character_name(character_dict: dict) -> int:
    if character_dict['aliases'] != "":
        x = 0
        for char in character_dict['aliases']:
            print(str(x) + ". " + char)
            x += 1
    elif character_dict['titles'] != "":
        x = 0
        for char in character_dict['titles']:
            print(str(x) + ". " + char)
            x += 1
    else:
        print("Nu avem aliases sau titles alegeti alt numar.")
    name = input("Care este numele personajului ? ")
    if name == character_dict['name']:
        print("Correct answer.")
        return 1
    print("Wrong answer.")
    return 0


