from Analise_DNA import Analise as analise
from Comparar_DNA import Comparar as comparação
from Mutação_DNA import Mutação as mutação
aa=dict()
with open('DNA/Aminoacidos.txt','r') as l:
  l.readline()
  l.readline()
  l.readline()
  for line in l.readlines():
    a=line.replace('\n','').split('\t')
    aa[a[0]]=a[1]

organismos=['Camundongo','Cão','Gado-doméstico','Humano']
dna=dict()

for o in organismos:
  with open('DNA/'+o+'.fasta','r') as l:
    l.readline()
    dna[o]=l.read()

i=0
#analise.analisar()

if i==2:
  import random
  o=[]
  a=[]
  for i in range(3):
    while True:
      a2=random.choice(list(aa.keys()))
      o2=random.sample(organismos,2)
      dna1=str(dna[o2[0]])
      dna2=str(dna[o2[1]])
      while o2[0]==o2[1]:
          o2=random.sample(organismos,2)
      while dna1.count(a2)==0 and dna2.count(a2)==0:
          a2=random.choice(list(aa.keys()))
      if o.count([o2[0],o2[1],a2])==0 and o.count([o2[1],o2[0],a2])==0:
        o.append([o2[0],o2[1],a2])
        a.append(a2)
        break
    comparação.comparar(0,aa[a2],a2,o2,dna1,dna2)

mutação.mutar()