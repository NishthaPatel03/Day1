employee_id=1001
basic_salary=15000.00
allowance=6000.00
tax=0

gross_salary=basic_salary+allowance

if(gross_salary<=5000):
    tax=0
elif(gross_salary>5000 and gross_salary<=10000):
    tax=10
elif(gross_salary>10000 and gross_salary<=20000):
    tax=20
else:
    tax=30
income_tax= gross_salary*tax/100

net_salary=gross_salary-income_tax

print("employee_id:",employee_id)
print("basic salary:",basic_salary)
print("allowance:",allowance)
print("income tax:",income_tax)
print("net salary:",net_salary)