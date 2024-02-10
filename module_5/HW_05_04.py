def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."

    return inner

@input_error
def parse_input(user_input):
    parts = user_input.strip().split(' ', 2)
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return command, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid input. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
