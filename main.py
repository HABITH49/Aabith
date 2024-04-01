from authentication import authentication
from hrm import Employee


def main():
    employees = Employee.load_and_save_employees()
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if authentication(username, password):
            print("Authentication successful.\n")
            current_employee = Employee("1029632", "aabith", "Manager", "Computting", "2023-11-01", "Active")
            print("1. View Personal Information")
            print("2. Add New Employee information")
            print("3. Remove Employee")
            print("4. View All Employee Information")
            print("5. Update Personal Information")
            print("6. Submit Leave Requests")
            print("7. View Company Policies")
            print("8. Access Work Schedules")
            print("9. Logout")
            print("10. Exit")
            while True:
                choice = input("Enter your choice: ")

                if choice == "1":
                    print("")
                    print(current_employee.__view_personal_info__())

                elif choice == "2":
                    print("")
                    current_employee.add_employee(employees)
                    current_employee.save_employees(employees)

                elif choice == "3":
                    print("")
                    current_employee.remove_employee(employees)
                elif choice == "4":
                    print("")
                    Employee.view_employees()

                elif choice == "5":
                    print("")
                    new_position = input("Enter new position: ")
                    new_department = input("Enter new department: ")
                    update_status = current_employee.__update_personal_info__(new_position, new_department)
                    print(update_status)

                elif choice == "6":
                    leave_type = input("Enter leave type: ")
                    duration: str = input("Enter duration: ")
                    details = input("Enter more details: ")
                    leave_request = current_employee.__submit_leave_request__(leave_type, duration, details)
                    print(leave_request)
                    print("")
                    print("Your request has been submitted successfully.....")

                elif choice == "7":
                    policies = current_employee.__view_company_policies__()
                    print(policies)

                elif choice == "8":
                    schedules = current_employee.__access_work_schedules__()
                    print(schedules)

                elif choice == "9":
                    while True:
                        log = input("Do you want to logout ?(yes/no): ")
                        if log == "yes":
                            print("Logging out...\n")
                            break
                        elif log == "no":
                            print("Cancelled....")
                            exit()

                    else:
                        print("invalid input. Please try again....")

                elif choice == "10":
                    while True:
                        out: str = input("Do you want to exit?(yes / no): ")
                        if out == "no":
                            print("Cancelled....")
                            print("")
                            break
                        elif out == "yes":
                            print("Exiting from the session...")
                            exit()
                        else:
                            print(" Please try again......")

                else:
                    print(" Please try again.")
        else:
            print("Authentication failed. Please try again.\n")


if __name__ == "__main__":
    main()
