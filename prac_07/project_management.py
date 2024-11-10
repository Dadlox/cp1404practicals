import csv
from Codes.Practical.Week7.Prac7.project import Project
from datetime import datetime


def main():
    projects = save_csv()
    show_menu(len(projects))
    choice = get_valid_choice()
    while choice != "Q":

        if choice == "L":
            file_name = input("Enter file name to load: ")


        if choice == "S":
            file_name = input("Saving project file, write in the name: ")
            save_projects_to_file(projects, file_name)

        if choice == "D":
            display_project(projects)

        if choice == "F":
            show_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            for project in projects:
                if project.start_date >= show_date:
                    print(project)

        if choice == "A":
            projects.append(add_new_projects())

        if choice == "U":
            display_update(projects)
            update_choice = validate_update_choice(projects)
            print(f"Chosen project:")
            print(projects[update_choice])
            completion_percent = get_valid_number("Completion rate:", projects[update_choice].completion, 100)
            projects[update_choice].completion = completion_percent

        print("")
        show_menu(len(projects))
        choice = get_valid_choice()

    print("Project successfully quit.")


def add_new_projects():
    name = input("Name: ")
    start_date = get_valid_date("Start date: ")
    priority = get_valid_number("Priority: ", 0, 100)
    cost_estimate = int(input("Cost: "))
    completion = get_valid_number("Completion: ", 0, 100)
    project = Project(name, start_date, priority, cost_estimate, completion)
    return project


def display_project(projects):
    unfinished_projects = [project for project in projects if project.completion != 100]
    finished_projects = [project for project in projects if project.completion == 100]

    for i in range(len(unfinished_projects)):
        for j in range(i + 1, len(unfinished_projects)):
            if unfinished_projects[i].priority > unfinished_projects[j].priority:
                unfinished_projects[i], unfinished_projects[j] = unfinished_projects[j], unfinished_projects[i]

    for i in range(len(finished_projects)):
        for j in range(i + 1, len(finished_projects)):
            if finished_projects[i].priority > finished_projects[j].priority:
                finished_projects[i], finished_projects[j] = finished_projects[j], finished_projects[i]

    print("Unfinished projects:")
    for project in unfinished_projects:
        print(project)

    print("Finished projects:")
    for project in finished_projects:
        print(project)


def display_update(projects):
    for i, project in enumerate(projects, 1):
        print(f"{i}: {project}")


def validate_update_choice(projects):
    while True:
        try:
            choice = int(input(">>> "))
            if choice <= 0:
                print("Choice must be greater than 0.")
            elif choice > len(projects):
                print(f"Choice must be less than or equal to {len(projects)}.")
            else:
                return choice - 1
        except ValueError:
            print("The input must be a valid number.")


def show_menu(project_count):
    print("Welcome to the Python Project Manager")
    print(f"Loaded {project_count} projects from projects.txt")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def get_valid_choice():
    choice = input(">>> ").capitalize()
    while choice not in ("L", "S", "D", "F", "A", "U", "Q"):
        print("Invalid choice, choose again.")
        choice = input(">>> ").capitalize()
    return choice


import csv


def load_projects_from_file(file_name):
    projects = []
    try:
        with open(file_name, 'r') as in_file:
            reader = csv.reader(in_file, delimiter='\t')
            next(reader)

            for parts in reader:
                name = parts[0]
                start_date = parts[1]
                priority = float(parts[2])
                cost = float(parts[3])
                completion = int(parts[4])

                # Create the Project object and add it to the list
                project = Project(name, start_date, priority, cost, completion)
                projects.append(project)

        print(f"Projects loaded from {file_name}")
        return projects
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except Exception as e:
        print(f"Error loading projects: {e}")
        return []


def get_valid_number(prompt, min, max):
    number = int(input(prompt))
    while max < number < min:
        if number > max:
            print(f"Number can't be more than {max}")
        if number < min:
            print(f"Number can't be less than {min}")
        number = input(int(prompt))
    return number


def get_valid_date(prompt):
    date_str = input(prompt)
    try:
        # Parse the input into a datetime object
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return get_valid_date(prompt)


def save_csv():
    projects = []
    with open('projects.txt', 'r') as in_file:
        next(in_file)  # Skip the header line
        reader = csv.reader(in_file, delimiter='\t')
        print(reader)
        for parts in reader:
            project = Project(parts[0], parts[1], float(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        return projects


def save_projects_to_file(projects, filename):
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')

        writer.writerow(["Name", "Start Date", "Priority", "Cost", "Completion"])

        for project in projects:
            writer.writerow([project.name, project.start_date, project.priority, project.cost, project.completion])

    print(f"Projects saved to {filename}")


main()
