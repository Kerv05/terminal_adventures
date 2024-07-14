ppl = {}    
roll_for_del = 1
def main():
    print("""WELCOME TO YOUR CONTACTS PROGRAM!!!
If this is your first time using this program, please acknowledge the ff:
    1. To create a contact, type in 'Create'
    2. To view all of your contacts, type in 'View'
    3. To search a specific contact, type in 'Search' with the name of your contact.
    4. You may end the program by typing in 'End'
          """)

    load()

    while True:
        try:
            intro = input("Create/View/Search Contacts: ")
            temp_intro = intro.upper()[0]
            intro_new = temp_intro + intro[1:]
            if "Create" in intro_new:
                create(ppl)
            elif "View" in intro_new:
                view()
            elif "Search" in intro_new:
                search(intro)              
            elif "Delete" in intro_new:
                delete(intro)
            elif "End" in intro_new:
                raise EOFError
            else:
                print(f"'{intro}' does not exist.")
        except ValueError:
            print("\nEnter a valid argument. 'Search [Contact Name]'\n")
            continue
        except EOFError:
            print("\n-----Program terminated.-----\n")
            break

def save():
    with open('contacts.txt', 'w') as file:
        file.write(str(ppl))

def load():
    with open("contacts.txt") as reading_file:
        listed_contacts = reading_file.read()
    if listed_contacts != '{}':
        new_listed = listed_contacts.strip('{}')
        listed_broken = new_listed.split(',')

        for item in listed_broken:
            x, y = item.replace("'", "").split(':')
            ppl.update({x.strip():y.strip()})
    else:
        pass

def view():
    global roll_for_del
    if len(ppl) == 0:
        print("\nYou have an empty contact.\n")
    else:
        ppl_keys = list(ppl.keys())
        ppl_keys.sort()
        sorted_dict = {i: ppl[i] for i in ppl_keys}
        for index, (key, value) in enumerate(sorted_dict.items(), start=1):
            print(f"{index}. {key} : {value}")

        if roll_for_del == 1:
            print("\nTo delete a contact, type in 'delete [Contact Name]'.\n")
            roll_for_del =- 1
        else:
            pass

def create(org_list):
    global roll_for_del
    while True:
        crte_ppl = input("Name of contact: ").strip()
        if crte_ppl in ppl:
            print(f"\n'{crte_ppl}' already exists in your contacts.\n")
            break
        while True:
            try:
                ppl_num = int(input("Enter Number: "))
                break
            except ValueError:
                print("\nEnter a number, Clown.\n")
        
        conf = input(f"{crte_ppl} : {ppl_num} confirmed? [yes/no] ")
        
        try:
            if conf.casefold() == "yes":
                org_list.update({crte_ppl:ppl_num})
                save() 
                print("\nContact updated!\n")
                if roll_for_del == 1:
                    print("To delete a contact, type in 'delete [Contact Name]'.\n")
                    roll_for_del =- 1
                else:
                    pass
                break
            elif conf.casefold() == "no":
                continue
            else:
                raise ValueError
        except ValueError:
            print(f"\nError: '{conf}' is invalid. Try creating a contact again.\n")
            break

def search(input_str):
    global roll_for_del
    load()
    _, person = input_str.split(maxsplit=1)
    person = person.strip()

    if ppl.get(person) == None:
        print(f"\n'{person}' does not exist in your contacts.\n")        

    if person in ppl:
        info = ppl[person]
        print(f"\n{person} : {info}\n")
        if roll_for_del == 1:
            print("To delete a contact, type in 'delete [Contact Name]'.\n")
            roll_for_del =- 1
        else:
            pass

def delete(input):
    _, person = input.split(maxsplit=1)
    person = person.strip()
    if ppl.get(person) == None:
        print(f"\n'{person}' does not exist in your contacts.\n")        
    if person in ppl:
        del ppl[person]
        save()
        print("\nContact deleted.\n")

main()
