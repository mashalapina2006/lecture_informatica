PENNIES_PER_NICKEL = 5
NICKEL = 0.05
total = 0.00
line = input("Введите цену товара (пустая строка для выхода): ")
while line != "":
    total = total+float(line)
line = input("Введите цену товара (пустая строка для выхода): ")
print("Полная сумма к оплате: %.02f" % total)
rounding_indicator = total * 100 % PENNIES_PER_NICKEL 
if rounding_indicator < PENNIES_PER_NICKEL / 2:
    cash_total = total - rounding_indicator/100 
else: 
        cash_total = total + NICKEL - rounding_indicator / 100
print("Сумма для оплаты наличными: %.02f" % cash_total)

