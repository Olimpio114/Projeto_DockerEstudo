#Observe a lista de pessoas e responda:

pessoas = {
"Mariana":25,
"Carlos":32,
"Beatriz":28,
"Rafael":51
}
#a) Como incluir o Felipe de 34 anos?
pessoas[ "Felipe"] = 34
print (pessoas)
#b)Como excluir Carlos da lista?

del pessoas["Carlos"]

#c)Como imprimir as idades ?
for idade in pessoas.values():
    print(idade)
#d)Comoimprimir apenas os nomes?
for nome in pessoas:
    print(nome)
#e)Como imprimir a lista completa?
for nome, idade in pessoas.items(): 
#print(f"Os nomes dos participantes são: {nome}")
     print(f" {nome} tem: {idade} anos") 
	
	
	valores = [30, 50, 10, 40, 20]
soma = 0
for valor in valores:
    soma += valor
print(valores)   #saída [30, 50, 10, 40, 20]
print(soma)   #saída  150

media = soma/len(valores)
print(media)  #saída  30

#Adicionar valores a lista
valores.append(50)
print(valores) #saída  [30, 50, 10, 40, 20, 50]


#Insira o elemento 40 na posição 2
valores.insert(2,40)
print(valores)  #saída [30, 50, 40, 10, 40, 20, 50]

#Remover um item específico da litsa
valores.remove(30)
print(valores) #saída [50, 40, 10, 40, 20, 50]

#Organiza a litsa em ordem crescente
valores.sort()
print(valores)  #saída [10, 20, 40, 40, 50, 50]

#Revrte a ordem da litsa
valores.reverse()
print(valores) #saída  [50, 50, 40, 40, 20, 10]
