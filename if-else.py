bill_id=1001
customer_id=101
bill_amount=199.99

print('bill_id:',bill_id)
print('customer_id:',customer_id)
print('original bill amount:',bill_amount)

if(bill_amount>500):
    bill_amount-=bill_amount*0.02
else:
    bill_amount-=bill_amount*0.01

print('discounted bill amount:',bill_amount)