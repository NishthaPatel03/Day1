bill_id=1001
customer_id=101
bill_amount=1200.0
discount=0.0

print('bill_id:',bill_id)
print('customer_id:',customer_id)
print('original bill amount:',bill_amount)

if(bill_amount>=1000):
    discount=5
elif(bill_amount>=500 and bill_amount<1000):
    discount=2
else:
    discount=1

bill_amount-=bill_amount*discount/100
print('discounted bill amount:',bill_amount)