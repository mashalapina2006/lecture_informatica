price = [4.95, 9.95, 14.95, 19.95, 24.95]
for x in price:
    print(x, f'{x*0.6:.{2}f}', f'{x-x*0.6:.{2}f}')


