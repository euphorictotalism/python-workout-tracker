import os


def findworkout(workout_name):
    found = False
    counter = 1

    with open("workout_data.csv", "r") as file:
        for line in file:
            details = line.strip().split(",") 

            date = details[0].strip()
            workout = details[1].strip()
            muscle_group = details[2].strip()
            sets = details[3].strip()
            reps = details[4].strip()
            weight = details[5].strip()

            if workout_name.lower().strip() == workout.lower().strip():
                print(f"Workout #{counter}")
                print(f"Date: {date}")
                print(f"Exercise: {workout}")
                print(f"Muscle Group: {muscle_group}")
                print(f"Sets: {sets}")
                print(f"Reps: {reps}")
                print(f"Weight: {weight}")
                print("-" * 45)

                counter += 1
                found = True

    if found == False:
        print(f"Workout {workout_name} not found in the database.")


def addworkout (date, workout_name, muscle_group, sets, reps, weight):
        data = (date, workout_name, muscle_group, sets, reps, weight)
        print(date, workout_name, muscle_group, sets, reps, weight)
        with open("workout_data.csv", "a") as file:
         file.write(f"{date}, {workout_name}, {muscle_group}, {sets} ,{reps} , {weight}\n")
         
def show_progress(workout):
    first_weight = None
    max_weight = None
    last_weight = None

    with open("workout_data.csv", "r") as file:
        for line in file:
            details = line.strip().split(",")

            workout_from_file = details[1].strip()
            weight = float(details[5].strip())

            if workout.lower().strip() != workout_from_file.lower().strip():
                continue

            if first_weight == None:
                first_weight = weight

            last_weight = weight

            if max_weight == None or weight > max_weight:
                max_weight = weight

    if first_weight == None:
        print("Workout not found.")
    else:
        print(f"Starting weight: {first_weight}")
        print(f"Latest weight: {last_weight}")
        print(f"Max weight: {max_weight}")
        print(f"Weight change: {last_weight - first_weight}")

def menu():
    while True:
        os.system("cls")
        print(os.getcwd())

        print("=" * 45)
        print("      WORKOUT TRACKER")
        print("=" * 45)
        print("1. Add a new workout")
        print("2. View workout profiles")
        print("3. Show Progress")
        print("4. Exit")

        option = int(input("Please select an option from the list above: "))

        if option == 1:
            print("Valid option selected, enter the values to add a new workout")
            date = input("Please enter the date of the workout (YYYY-MM-DD): ")
            workout_name = input("Please enter the name of the workout you are adding: ")
            muscle_group = input("Please enter the muscle group targeted: ")
            sets = int(input("Please enter the number of sets: "))
            reps = int(input("Please enter the number of reps: "))
            weight = float(input("Please enter the weight used: "))

            addworkout(date, workout_name, muscle_group, sets, reps, weight)

            print("-" * 45)
            print(f"The workout {workout_name} targeting {muscle_group} with {sets} sets of {reps} reps at {weight} weight has been added.")
            print("-" * 45)

            input("\nPress Enter to return to menu...")

        elif option == 2:
            if os.path.exists("workout_data.csv"):
                workout = input("Please enter the name of the workout you want to view: ")
                findworkout(workout)
            else:
                print("Not found, please add a workout first.")

            input("\nPress Enter to return to menu...")

        elif option == 3:
            if os.path.exists("workout_data.csv"):
                workout = input("Please enter the name of the workout you want to view your progress for: ")
                show_progress(workout)
            else:
                print("Not found, please add a workout first.")

            input("\nPress Enter to return to menu...")

        elif option == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid option")
            input("\nPress Enter to return to menu...")


menu()
