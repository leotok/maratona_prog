# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1023

from collections import defaultdict
from decimal import Decimal, ROUND_DOWN

i = 0
while True:
	qtd_imoveis = int(raw_input())

	if qtd_imoveis == 0:
		break

	i += 1
	print "Cidade# %d:" % i

	heap = []
	dic = defaultdict(int)

	total_moradores = 0
	total_consumo = 0
	while qtd_imoveis != 0:
		qtd_imoveis -= 1
		read = raw_input().split(" ")
		qtd_moradores = int(read[0])
		consumo_imovel = float(read[1])
		consumo_pessoa = float(consumo_imovel // qtd_moradores)
		total_moradores += qtd_moradores
		total_consumo += consumo_imovel

		dic[consumo_pessoa] += qtd_moradores

	consumos = list(dic.keys())
	consumos.sort()
	ordem = ""

	j = 0
	while j < len(consumos):
		consumo, qtd = consumos[j], dic[consumos[j]]
		ordem += "%d-%d " %(qtd, consumo)
		j += 1
		
	print ordem[:-1]

	# URI so aceitou usando o ROUND_DOWN no resultado
	print "Consumo medio: %.2f m3.\n" %(Decimal(total_consumo/total_moradores).quantize(Decimal('.01'), rounding=ROUND_DOWN))




