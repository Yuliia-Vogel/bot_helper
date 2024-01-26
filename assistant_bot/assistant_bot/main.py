import sys


contact_list = {}
# contact_list = {'NNnnn FFFfff' : '4771455464687', 'ldkhgh jdhg' : '245647897', 'Yul Meln' : '0978156194', 'Yu Me' : '097', 'Ko Ka' : '258'}


def input_error(fuction):
    def inner_func(*args):
        try:
            return fuction(*args)
        except KeyError:
            print("This contact not found")
            return "This contact not found"
        except ValueError:
            print("Incorrect input")
            return "Incorrect input"
        except IndexError:
            print("No input was done")
            return "No input was done"
    return inner_func


# основна функція, що запускається і приймає команди і видає результат
@input_error
def main():
    print("Welcome to your bot assistant!")
    while True:
        the_input = input("Please, enter the command: ")
        response = command_handler(the_input)


# обробка отриманих команд
@input_error
def command_handler(the_input):
    if len(the_input) == 0:
        raise IndexError
    phrase_casefold = ''
    phrase_casefold = the_input.casefold()
    if phrase_casefold == 'show all':
        return show_all_contacts()
    command_casefold = phrase_casefold.split(' ')
    command = command_casefold[0]
    print(f'command is {command}')
    if command == 'hello':
        print("How can I help you?")
        return "How can I help you?"
    elif command == "bye" or command == "close" or command == "exit":
        print("Good bye!")
        exit(1) 
    input_data = the_input.rsplit(' ')
    phone = input_data[-1]
    print(f'phone is {phone}')
    pre_pre_name = the_input.replace(command, '')
    pre_name = pre_pre_name.replace(phone, '')
    name = pre_name.strip()
    print(f'name is {name}') 
    if command == 'add':
        return add_new_contact(name, phone)
    elif command == "change":
        return change_contact(name, phone) 
    elif command == "phone":
        return show_phone_of_contact(name)
    else: 
        raise ValueError


# додавання нових контактів
@input_error
def add_new_contact(name, phone):
    responce =  contact_checker(name) # викликаю функцію перевірки, чи є ім"я в базі
    if responce is None:
        isdigit_check = phone.isdigit()
        if isdigit_check == False:
            print(f'Phone can contain digits only')
            raise ValueError
        else:
            contact_list[name] = phone
            print(f"Your contact list was updated with new record: {name} : {phone}")
            return "Contact added"
    else:
        print(f'{name} already exists in your contact list')
        return "Name already exists"


# зміна номера в контакті, що вже існує
@input_error
def change_contact(name, new_phone):
    responce =  contact_checker(name) # викликаю функцію перевірки, чи є ім"я в базі
    if responce is None:
        raise KeyError
    else:
        record = responce
        print(record)
        isdigit_check = new_phone.isdigit()
        if isdigit_check == False:
            print(f'phone can contain digits only')
            raise ValueError
        else:
            contact_list[name] = new_phone
            print(f'This is updated contact: {name} : {new_phone}')
            return "Contact changed"


# перевірка, чи є такий номер в списку, якщо нема - функція повертає None
@input_error
def contact_checker(name):
    for record in contact_list.items():
        if name in record:
            print(f"{name} found")
            return record
        else:
            pass
    return None 


# щоб показати номер контакту
@input_error
def show_phone_of_contact(contact_to_show):
    responce =  contact_checker(contact_to_show) # викликаю функцію перевірки, чи є ім"я в базі
    if responce is None:
        raise KeyError
    else:
        print(f"this is asked number of {responce}")
        return responce


def show_all_contacts():
    print(contact_list)
    return contact_list




if __name__ == "__main__":
    main()
