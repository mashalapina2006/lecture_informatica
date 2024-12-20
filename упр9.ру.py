weight_souvenir = 75  
weight_trinket = 112  
num_souvenirs = int(input("Сколько сувениров вы хотите купить? "))
num_trinkets = int(input("Сколько безделушек вы хотите купить? "))
total_weight = (num_souvenirs * weight_souvenir) + (num_trinkets * weight_trinket)
print("Общий вес вашей посылки: ", total_weight, "грамм")
