# Condicional Simple.

sueldo = 4_100_000
sueldoMin = 1_160_000

if sueldo <= sueldoMin:
    auxTrans = 140_000
else: 
    auxTrans = 0


print(f"Auxilio de Transporte ${auxTrans:,}")