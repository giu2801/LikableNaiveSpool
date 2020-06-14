print('Feito por:')
print('\nDiego Zago Brito - 11779782')
print('\nGiuliana Lopes Pola - 11779802')

from Analise_DNA import Analise as analise
from Comparar_DNA import Comparar as comparação
from Mutação_DNA import Mutação as mutação

aa=dict()#dicionário com código e nome dos aminoácidos
aa2=dict()#dicionário com código e código de três letras dos aminoácidos

#constrói os dicionários de aminoácidos a partir da tabela de aminoácidos na pasta DNA
with open('DNA/Aminoacidos.txt','r') as l:
  l.readline()
  l.readline()
  l.readline()
  for line in l.readlines():
    #separa cada linha por coluna e coloca em uma lista
    a=line.replace('\n','').split('\t')
    aa[a[0]]=a[1]
    aa2[a[0]]=a[2]

organismos=['Camundongo','Cão','Gado-doméstico','Humano']
dna=dict()#dicionário com o nome do organismo e a sequência da proteína dele
cabeçalho=dict()#dicionário com o nome do organismo e o cabeçalho do arquivo fasta dele

for o in organismos:
  with open('DNA/'+o+'.fasta','r') as l:
    cabeçalho[o]=l.readline()
    dna[o]=l.read()

print('\n\nOpções: ')
print('\n1: identificar os aminoácidos da proteína de cada organismo e mostrar a frêquencia deles')
print('\n2: comparar a sequência compare a sequencias da proteína de três pares de organismos diferentes')
print('\n3: criar uma mutação na sequência de cada organismo')
opcao=int(input('\nEscolha uma opção: '))

if opcao==1:
  analise.analisar(organismos,aa,dna,aa2)

if opcao==2:
  import random
  #lista de combinações de 2 organismos, pra não repetir a combinação
  o=[]

  #compara 3 pares de organismos diferentes
  for i in range(3):
    while True:
      o2=random.sample(organismos,2)
      while o2[0]==o2[1]:
          o2=random.sample(organismos,2)
      dna1=str(dna[o2[0]])
      dna2=str(dna[o2[1]])
      if o.count([o2[0],o2[1]])==0 and o.count([o2[1],o2[0]])==0:
        o.append([o2[0],o2[1]])
        break
    comparação.comparar(i,o2,dna1,dna2)

if opcao==3:
  #faz uma mutação para cada organismo
  for o in organismos:
    mutação.mutar(dna[o],aa,o,cabeçalho[o])

exit()