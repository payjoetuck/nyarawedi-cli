import random, questionary

data = []

def get_data() -> str:
    temp = ''
    for i, v in enumerate(data):
        temp += f'[{i + 1}] {v}\n'
    return temp

def add_data(name: str) -> None:
    data.append(name)

def rename_data(index: int, newName: str) -> None:
    data[index] = newName

def remove_data(index: int) -> None:
    del data[index]

def roll_random() -> None:
    temp = random.choice(data)
    questionary.print(temp, style="bold italic fg:yellow")
    del data[data.index(temp)]


if __name__ == '__main__':
    while True:
        main_menu = questionary.select(
            f"Welcome to Random Picker!\n{get_data()}",
            choices=["Make new partisipants", "Edit partisipants", "ROLL RANDOM!", "Quit"],
        ).ask()
        if main_menu == 'Make new partisipants':
            add_data(questionary.text("Full name").ask())
        elif main_menu == 'Edit partisipants':
            choose_index = data.index(
                    questionary.select(
                    f"Choose the participant!",
                    choices=data,
                ).ask()
            )
            edit_menu = questionary.select(
                f"Choose the participant!\n{data[choose_index]}",
                choices=["Edit name", "Remove", "Back"],
            ).ask()
            if edit_menu == 'Edit name':
                rename_data(choose_index, questionary.text("Full name").ask())
            elif edit_menu == 'Remove':
                remove_data(choose_index)
        elif main_menu == 'ROLL RANDOM!':
            if len(data) > 1:
                roll_random()
        elif main_menu == 'Quit':
            break
