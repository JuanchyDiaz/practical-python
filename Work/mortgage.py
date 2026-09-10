# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_end_month = 12

while principal > 0:
    month += 1
    current_payment = payment
    if month <= extra_payment_end_month:
        current_payment += extra_payment
    principal = principal * (1 + rate / 12) - current_payment
    total_paid += current_payment

print(f'{month} months, Total paid: {total_paid:,.2f}')

print(month, 'months,', 'Total paid:', round(total_paid, 2))