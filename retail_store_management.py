#retail store management with customer name 

bill_id = 1001
customer_id = 101
bill_amount = 199.99

cust_name = input("Enter Customer Name : ")

if len(cust_name) >= 3 and len(cust_name) <= 20 :
	print("Customer Name : ",cust_name)
	print('Bill Id: %d'%bill_id)
	print('Customer Id: %d'%customer_id)
	print('Bill Amount: Rs.%5.2f'%bill_amount)
else : 
	print("ERROR : Customer Name Length Must Between 3 and 20")
