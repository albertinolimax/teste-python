faturamento = 1000
custos = 700

novas_vendas = 300

faturamento, faturamento + novas_vendas
imposto = faturamento
lucro = faturamento - custos - imposto

print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)
