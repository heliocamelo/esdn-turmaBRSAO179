valorEmReais = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

conversaoDolar = valorEmReais / taxaDolar
print(f"R${valorEmReais:.2f} convertido pra dólar é igual a: ${conversaoDolar:.2f}")

conversaoEuro = valorEmReais / taxaEuro
print(f"R${valorEmReais:.2f} convertido para euro é igual a: €{conversaoEuro:.2f}")