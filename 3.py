import json

with open("dados/dados.json", "r") as file:
    data = json.load(file)

faturamentos = [dia["valor"] for dia in data if dia["valor"] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = [dia["dia"] for dia in data if dia["valor"] > media_mensal]

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {len(dias_acima_da_media)}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
