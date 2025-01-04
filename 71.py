pi_approximation = 3.0
for i in range(1, 16):
    term = 4 / (i * (i + 1) * (i + 2))
    if i % 2 == 1:  
        pi_approximation += term
    else:           
        pi_approximation -= term
    print(f"Приближение {i}: {pi_approximation:.15f}")


