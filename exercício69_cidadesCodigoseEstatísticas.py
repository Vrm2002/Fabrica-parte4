cidades=["Campo Grande","São Paulo","Rio de Janeiro","Sidrolândia","Cuiabá"]
veiculos=[]
acid=[]
plusminus=[]
vei2000=[]
cont=0

print("Veículos de passeio na ordem:\n1- {:s}\n2- {:s}\n3- {:s}\n4- {:s}\n5- {:s}".format(cidades[0],cidades[1],cidades[2],cidades[3],cidades[4]))
for i in range(5):
    veiculos.append(int(input("Digite o número de veículos de passeio na cidade correspondente: ")))
print("\nNúmeros de acidentes de trânsito na ordem:\n1- {:s}\n2- {:s}\n3- {:s}4- {:s}\n5- {:s}".format(cidades[0],cidades[1],cidades[2],cidades[3],cidades[4]))
for i in range(5):
    acid.append(int(input("Digite o número de acidentes de trânsito na cidade correspondente: ")))

plusminus.append(acid[0],acid[1],acid[2],acid[3],acid[4])
medvei=(veiculos[0]+veiculos[1]+veiculos[2]+veiculos[3]+veiculos[4])/5


print("Maior índice e Menor índice de acidentes:\n")
if min(plusminus)==acid[0]:
    print("A cidade com menor índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[0],acid[0]))
elif min(plusminus)==acid[1]:
    print("A cidade com menor índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[1],acid[1]))
elif min(plusminus)==acid[2]:
    print("A cidade com menor índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[2],acid[2]))
elif min(plusminus)==acid[3]:
    print("A cidade com menor índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[3],acid[3]))
elif min(plusminus)==acid[4]:
    print("A cidade com menor índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[4],acid[4]))
elif plusminus[0]<0 or plusminus[1]<0 or plusminus[2]<0 or plusminus[3]<0 or plusminus[4]<0:
    print("Existem números negativos. ERRO.")
else:
    print("Existem números iguais. ERRO.")

if max(plusminus)==acid[0]:
    print("A cidade com maior índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[0],acid[0]))
elif max(plusminus)==acid[1]:
    print("A cidade com maior índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[1],acid[1]))
elif max(plusminus)==acid[2]:
    print("A cidade com maior índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[2],acid[2]))
elif max(plusminus)==acid[3]:
    print("A cidade com maior índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[3],acid[3]))
elif max(plusminus)==acid[4]:
    print("A cidade com maior índice de acidentes de trânsito é {:s}, com {:d} acidentes de trânsito.".format(cidades[4],acid[4]))

print("\nA média de veículos nas cinco cidades é {:.0f}".format(medvei))

if veiculos[0]<2000:
    vei2000.append(acid[0])
if veiculos[1]<2000:
    vei2000.append(acid[1])
if veiculos[2]<2000:
    vei2000.append(acid[2])
if veiculos[3]<2000:
    vei2000.append(acid[3])
if veiculos[4]<2000:
    vei2000.append(acid[4])

for i in vei2000:
    cont=cont+1

med2000=sum(vei2000)/cont

print("\nA média de acidentes nas cidades com menos de 2000 veículos de passeio é {:.0f}".format(med2000))
