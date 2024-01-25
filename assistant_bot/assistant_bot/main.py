import sys


# contact_list = []
contact_list = [{'name': 'NNnnn FFFfff', 'phone': '4771455464687'}, {'name': 'ldkhgh jdhg', 'phone': '245647897'}, {'name': 'Yul Meln', 'phone':
'0978156194'}, {'name': 'Yu Me', 'phone': '097'}, {'name': 'Ko Ka', 'phone': '258'}]



# основна функція, що запускається і приймає команди і видає результат
def main():
    print("Welcome to your bot assistant!")
    while True:
        command = input("Please, enter the command: ")
        response = command_handler(command)
        # exit() #just to exit while creating and testing code

#обробка отриманих команд
def command_handler(command):
    phrase_casefold = ''
    phrase_casefold = command.casefold()
    command_casefold = phrase_casefold.split(' ')
    print(command_casefold)
    for word in command_casefold:
        if word == 'hello':
            print("How can I help you?")
        if word == 'add':
            print("I'll add a new contact")
            add_new_contact()
        elif word == "change":
            print("to change phone number or name in contact")
            change_contact() 
        elif word == "phone":
            print("show phone number of the contact")
            show_phone_of_contact()
        elif word == "all":
            print("show all saved contacts")
            show_all_contacts() 
        elif word == "bye" or word == "close" or word == "exit":
            print("Good bye!")
            exit(1) 
        else: 
            # print("Invalid command")
            pass


# #додавання нових контактів
def add_new_contact():
    record = {}
    name = input("Please, enter the name of new contact: ")
    phone = input("Please, enter phone of the new contact: ")
    record["name"] = name
    record["phone"] = phone
    contact_list.append(record)
    print(f"Your contact list was updated with new record: {record}")
    print(contact_list)


# зміна номеру чи імені в контакті
def change_contact():
    contact_to_change = input("Enter the name whose number you want to change: ")
    responce =  contact_upd_checker(contact_to_change) # викликаю функцію перевірки, чи є номер в базі
    if responce is None:
        print("The contact not found")
    else:
        record = responce
        new_phone = input("Enter the new phone number: ")
        record["phone"] = new_phone
        print(f'This is updated contact: {record}')


# викликаю функцію перевірки, чи є такий номер в списку, якщо нема - функція повертає None
def contact_upd_checker(contact):
    for record in contact_list:
        if contact in record.get("name"):
            print(f"{record} found")
            return record
        else:
            pass
    return None 


def show_phone_of_contact():
    contact_to_show = input("Enter the name whose number to show: ")
    responce =  contact_upd_checker(contact_to_show) # викликаю функцію перевірки, чи є номер в базі
    if responce is None:
        print("The contact not found")
    else:
        print(f"this is asked number of {responce.get('name')}: {responce.get('phone')}")


def show_all_contacts():
    print(contact_list)
    return contact_list


if __name__ == "__main__":
    main()
        
# show_phone_of_contact()