faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())
soma_percentual = 0

print("Percentual de representação por estado:")
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    soma_percentual+=percentual
    print(f"{estado}: {percentual:.2f}%")
    print(f"{soma_percentual:.2f}")
