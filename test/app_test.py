from config import config
import random, questionary

def get_data() -> str:
    temp = ''
    for i, v in enumerate(data):
        temp += f'[{i + 1}] {v}\n'
    return temp

def add_data(name: str) -> None:
    data.append(name)

def rename_data(index: int, newname: str) -> None:
    data[index] = newname

def remove_data(index: int) -> None:
    del data[index]

def roll_random() -> None:
    temp = random.choice(data)
    questionary.print(temp, style="bold italic fg:yellow")
    del data[data.index(temp)]


if __name__ == '__main__':
    for i in config:
        print(f"=== PATH {i['path']} ===")
        print(i['description'])
        data = []
        for n in i['actions']:
            main_menu = n['main-menu']
            if main_menu == 'Make new participants':
                add_data(n['full-name'])
            elif main_menu == 'Edit participants':
                choose_index = data.index(n['target-name'])
                edit_menu = n['edit-menu']
                if edit_menu == 'Edit name':
                    rename_data(choose_index, n['full-name'])
                elif edit_menu == 'Remove':
                    remove_data(choose_index)
            elif main_menu == 'ROLL RANDOM!':
                if len(data) > 1:
                    roll_random()
            elif main_menu == 'Quit':
                break
        print(data)
