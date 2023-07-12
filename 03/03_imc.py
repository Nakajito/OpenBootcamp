peso = int(input("Introduce tu peso en kg: "))
estatura = float(input('Introduce tu estatura en m: '))
imc = peso / (estatura * estatura)
print(f'Tu índice de masa corporal es {imc:.2f}')