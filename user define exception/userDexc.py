class CheckSalary(Exception):
    pass

try:
    empid=int(input("enter the empid :- "))
    empname=input('enter the name:-')
    salary = int(input("Enter the salary:- "))
    if salary < 0:
        raise CheckSalary('salary should not be negative!')
    
except CheckSalary as e :
    print("Error",e)

print('I am here')