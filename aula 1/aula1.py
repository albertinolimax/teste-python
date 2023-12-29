faturamento = 1800 # numero inteiro
custos = 900

novas_vendas = 300
faturamento = faturamento + novas_vendas

taixa_imposto = 0.1 # numero decimal -> float
mmensagem = 'O faturamento foi de' # string = txto
teve_lucro = False # boolean 

imposto = taixa_imposto * faturamento
print('Faturamento', faturamento)
print('Custos', custos)
print('Lucro', faturamento - custos - imposto)
print(mmensagem, faturamento)