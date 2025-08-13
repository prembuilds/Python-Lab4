contact_file = "data_contacts.txt"

def add_entry():
    nm = input("Name: ").strip()
    ph = input("Phone: ").strip()
    try:
        with open(contact_file, "a") as f:
            f.write(f"{nm},{ph}\n")
        print("Contact saved.")
    except:
        print("Error saving contact.")

def view_all():
    try:
        with open(contact_file, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No contacts.")
                return
            print("\n-- Contacts --")
            for c in lines:
                nm, ph = c.strip().split(",")
                print(f"{nm} | {ph}")
    except FileNotFoundError:
        print("No file found.")
    except:
        print("Error reading contacts.")

def find_contact():
    key = input("Search name or phone: ").strip().lower()
    try:
        with open(contact_file, "r") as f:
            found = False
            for c in f:
                nm, ph = c.strip().split(",")
                if key in nm.lower() or key in ph:
                    print(f"{nm} | {ph}")
                    found = True
            if not found:
                print("No match found.")
    except FileNotFoundError:
        print("No file found.")
    except:
        print("Error while searching.")

def remove_contact():
    key = input("Name or phone to delete: ").strip().lower()
    try:
        with open(contact_file, "r") as f:
            lines = f.readlines()
        updated = []
        removed = False
        for c in lines:
            nm, ph = c.strip().split(",")
            if key in nm.lower() or key in ph:
                print(f"Removed: {nm} ({ph})")
                removed = True
            else:
                updated.append(c)
        if removed:
            with open(contact_file, "w") as f:
                f.writelines(updated)
        else:
            print("Nothing deleted.")
    except FileNotFoundError:
        print("No file found.")
    except:
        print("Error deleting contact.")

def main():
    while True:
        print("\n-- Contact Book --")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            add_entry()
        elif ch == "2":
            view_all()
        elif ch == "3":
            find_contact()
        elif ch == "4":
            remove_contact()
        elif ch == "5":
            print("Bye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
