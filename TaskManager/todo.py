# Το παρακάτω πρόγραμμα δημιουργεί μία λίστα οργάνωσης διεργασιών (task manager), με την οποία ο χρήστης μπορεί να δημιουργήσει, να επεξεργάσει και να τερματίσει στόχους (tasks).
import json

tasks = []

# Η παρακάτω συνάρτηση αποθηκεύει τις αλλαγές σε ένα αρχείο json, έτσι ώστε να μη χάνονται όταν τερματίζεται το πρόγραμμα, και καλείται κάθε φορά που γίνονται αλλαγές.
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass

while True:
    print("----TO DO LIST----")
    print("1. Προσθήκη")
    print("2. Προβολή")
    print("3. Ενημέρωση")
    print("4. Διαγραφή")
    print("5. Έξοδος")
    choice = input("Επίλεξε μία επιλογή: ")
    # Έλεγχος Ορθότητας Δεδομένων
    while choice < "1" or choice > "5":
        choice = input("Επίλεξε μία επιλογή μεταξύ του 1 και 5: ")
    # Προσθήκη: Ο χρήστης μπορεί να προσθέσει διεργασίες, δίνοντας status και όνομα.
    if choice == "1":
        task_name = input("Δώσε το όνομα της διεργασίας: ")
        task = {"status": False, "name": task_name}
        tasks.append(task)
        save_tasks()
    # Προβολή: Εμφανίζει στον χρήστη όλες τις διεργασίες.
    elif choice == "2":
        for num, i in enumerate(tasks, 1):
            task_name = i.get("name")
            if i.get("status") == True:
                print(f"{num}. {task_name}: [V]")
            else:
                print(f"{num}. {task_name}: [X]")
    # Ενημέρωση: Αλλάζει το status μίας διεργασίας.
    elif choice == "3":
        user_input = input(f"Δώσε τον αριθμό του task από το 1 μέχρι το {len(tasks)}: ")
        if not user_input.isdigit():
            print("Πρέπει να δώσεις αριθμό!")
            continue
        number = int(user_input) - 1
        if number < 0 or number >= len(tasks):
            print("Λάθος αριθμός!")
            continue
        else:
            target_dict = tasks[number]
            if target_dict["status"] == False:
                target_dict["status"] = True
                print("Το task ενημερώθηκε!")
            else:
                target_dict["status"] = False
                print("Το task ενημερώθηκε!")
            save_tasks()
    # Διαγραφή: Διαγράφει μία διεργασία
    elif choice == "4":
        number = int(input(f"Δώσε τον αριθμό του task από το 1-{len(tasks)}: ")) - 1
        if number < 0 or number >= len(tasks):
            print("Λάθος αριθμός!")
            continue
        else:
            del tasks[number]
            save_tasks()
    # Έξοδος: Τερματίζει το πρόγραμμα και σταματάει το while loop.
    elif choice == "5":
        break