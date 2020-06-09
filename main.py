aa=dict()
with open('Aminoacidos.txt','r') as l:
  for line in l.readlines():
    a=line.replace('\n','').split('\t')
    aa[a[0]]=a[1]

organismos=['Camundongo','Cão','Gado-doméstico','Humano']
dna=dict()
completo=""

for o in organismos:
  with open('DNA/'+o+'.fasta','r') as l:
    l.readline()
    dna[o]=l.read()
    completo=completo+dna[o]

import re
import Graficos
with open('Passo 3/Catalase-aminoacidos.txt','w') as l:
  organismos2=dict()
  for o in organismos:
    l.write(o.upper())
    l.write('\n%20s|%27s|%21s|%23s'%('Código do aminoácido','Nome do aminoácido','Número de ocorrências','Posições de ocorrências'))
    aa3=[]
    aa2=[]
    num=[]
    códigos=[]
    for a in aa:
      lista=''
      #if dna[o].count(a)>0:
      aa2.append(aa[a])
      num.append(dna[o].count(a))
      if dna[o].count(a)>0:
        for b in re.finditer(a,dna[o]):
          if lista=='':
            lista=str(b.start())
          else:
            lista=lista+','+str(b.start())
      l.write('\n%20s|%27s|%21s|%23s'%(a,aa[a],dna[o].count(a),lista))
      #if completo.count(a)>0:
      códigos.append(a)
      aa3.append(dna[o].count(a))
    Graficos.simples(o,aa2,num)
    organismos2[o]=aa3
    l.write('\n\n')
Graficos.agrupado(códigos,organismos2)