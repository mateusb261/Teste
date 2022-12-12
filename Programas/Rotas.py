total_de_cidades_atendidas_pela_empresa = int(input())
dicionario_de_distancia_entre_as_cidades = {}
i1 = 1
i2 = 2
while i1 < i2:
    i2 = i1 + 1
    while i2 <= total_de_cidades_atendidas_pela_empresa:
        entrada_de_distancia_entre_duas_cidades = int(input())
        dicionario_de_distancia_entre_as_cidades[(('%d%d') % (i1, i2))] = entrada_de_distancia_entre_duas_cidades
        i2 += 1
    i1 += 1

total_de_cidades_da_rota_escolhida = int(input())
cidade_digitada = 0
soma_de_rotas = 0
contador_de_cidades_totais_digitadas = 0
primeira_cidade = 0
chave = 0
for cidade in range(total_de_cidades_da_rota_escolhida):
    cidade_digitada = int(input())
    contador_de_cidades_totais_digitadas += 1
    if contador_de_cidades_totais_digitadas == 1:
        primeira_cidade = cidade_digitada
    elif contador_de_cidades_totais_digitadas >= 2:
        if chave < cidade_digitada:
            chave= int(("%d%d" % (chave, cidade_digitada)))
            soma_de_rotas += dicionario_de_distancia_entre_as_cidades['%d' % chave]
        elif chave > cidade_digitada:
            chave = int("%d%d" % (cidade_digitada, chave))
            soma_de_rotas += dicionario_de_distancia_entre_as_cidades['%d' % chave]
    chave = cidade_digitada
if contador_de_cidades_totais_digitadas == total_de_cidades_da_rota_escolhida:
    if primeira_cidade < cidade_digitada:
        chave = int("%d%d" % (primeira_cidade, cidade_digitada))
        soma_de_rotas += dicionario_de_distancia_entre_as_cidades['%d' % chave]
    elif primeira_cidade > cidade_digitada:
        chave = int("%d%d" % (cidade_digitada, primeira_cidade))
        soma_de_rotas += dicionario_de_distancia_entre_as_cidades['%d' % chave]

litros_de_combustível = soma_de_rotas/3
preço_do_diesel = float(input())
custo_total = litros_de_combustível * preço_do_diesel
print("R$ %.2f" % custo_total)