# Assignment1 - EMS(Employee Management System)

# STEP : 1
# Here i create a dictionary and take emp_id as key and take another dictionary as value which store the information of the employee with respect the emp_id
employee_data = {101 : {'name': 'Anjali', 'age': 23, 'department': 'HR', 'salary': 50000},
                 102 : {'name': 'Satya', 'age': 20, 'department': 'Sales', 'salary': 40000},
                 103 : {'name': 'Jyoti', 'age': 24, 'department': 'Media', 'salary': 35000},
                 104 : {'name': 'Lalit', 'age': 23, 'department': 'Developer', 'salary': 55000},
                 105 : {'name': 'Vicky', 'age': 26, 'department': 'Manager', 'salary': 70000}
                }



def add_employee():
    emp_id = input("Enter employee Id : ")
    emp_id = int(emp_id)

    # Using for loop check if employee is present or not , if present the it return to main system if not then it added 
    if emp_id in employee_data:
        print("The employee is already present in the dictionary ")
        return
    # adding employee data
    print("Adding Employee data ")
    name = input("Enter name of the Employee : ")
    age = int(input("Enter age of the Employee : "))
    department = input("Enter department of the Employee : ")
    salary = int(input("Enter salary of the Employee : "))
    employee_data[emp_id]={
        'name':name,
        "age":age,
        "department":department,
        "slary":salary
        }
    print("Adding Employee data Successfully! ")



def view_employee():
    if not employee_data:
        print("No employees available.")
        return
    # using for loop to retrieve the data from dictionary here i use .items() - use to acess the key-value pairs from the dictionary
    for emp_id,details in employee_data.items() :
        print(f'{emp_id} \t {details['name']} \t {details['age']} \t {details['department']} \t {details['salary']} ')


def search_employee(): 
    # here if emp_id presemt then it show the details of employe
    emp_id = int(input("Enter Employee Id number " ))
    if emp_id in employee_data:
        employee =  employee_data[emp_id]
        print("name" ,employee['name'] )
        print("age" ,employee['age'] )
        print("department" ,employee['department'] )
        print("salary" ,employee['salary'] )
        # if not present then it show this msg
    else : 
        print("Employee not found.")


# STEP : 2 
# I creat a main MenuSystem which add, view , search for employee and exit 
def MenuSystem():
    while True:
        number = input("Chosse number between 1-4 : ")
        # used to add employee 
        if number == '1':
            add_employee()
        # used to view employee 
        elif number== '2':
            view_employee()
        # used to search employee 
        elif number == '3':
            search_employee()
        # used to exit user from the EMS  
        elif number == '4':
            print("Thank-you")
            break
        # used to tell user that they enter incorrect number and he has to enter valid number so that they can perform given operations 
        else :
            print("Invalid number please enter correct number! ")

MenuSystem()