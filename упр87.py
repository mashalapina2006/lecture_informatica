first_item_cost = 10.95
other_item_cost = 2.95
def calculate_delivery_cost(num_items):
    if num_items <= 0:
        return 0 
    elif num_items == 1:
        return first_item_cost
    else:
        return first_item_cost + (num_items - 1) * other_item_cost
print("Введите количество товаров в заказе.")
num_items = int(input("Количество товаров"))
delivery_cost = calculate_delivery_cost(num_items)
print("Сумма доставки составляет: $", delivery_cost)
