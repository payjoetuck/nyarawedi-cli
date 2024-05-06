import random, questionary

data = []

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
    while True: #1
        main_menu = questionary.select(
            f"Welcome to Random Picker!\n{get_data()}",
            choices=["Make new participants", "Edit participants", "ROLL RANDOM!", "Quit"],
        ).ask() #2
        if main_menu == 'Make new participants': #3
            add_data(questionary.text("Full name").ask()) #4
        elif main_menu == 'Edit participants':
            choose_index = data.index(
                    questionary.select(
                    "Choose the participant!",
                    choices=data,
                ).ask()
            ) #5
            edit_menu = questionary.select(
                f"Choose the participant!\n{data[choose_index]}",
                choices=["Edit name", "Remove", "Back"],
            ).ask() #6
            if edit_menu == 'Edit name': #7
                rename_data(choose_index, questionary.text("Full name").ask()) #8
            elif edit_menu == 'Remove':
                remove_data(choose_index) #9
            #10
        elif main_menu == 'ROLL RANDOM!':
            if len(data) > 1: #11
                roll_random() #12
            else:
                pass #13
        elif main_menu == 'Quit':
            break #14
        #15
    quit() #16
