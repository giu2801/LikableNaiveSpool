def analisar():
  aa=dict()
  aa2=dict()
  with open('DNA/Aminoacidos.txt','r') as l:
    l.readline()
    l.readline()
    l.readline()
    for line in l.readlines():
      a=line.replace('\n','').split('\t')
      aa[a[0]]=a[1]
      aa2[a[0]]=a[2]

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
  with open('Analise_DNA/Catalase-aminoacidos.txt','w') as l:
    organismos2=dict()
    for o in organismos:
      l.write(o.upper())
      l.write('\n%20s|%27s|%21s|%23s'%('Código do aminoácido','Nome do aminoácido','Número de ocorrências','Posições de ocorrências'))
      a3=[]
      a2=[]
      num=[]
      códigos=[]
      for a in aa:
        lista=''
        #if dna[o].count(a)>0:
        a2.append(aa[a])
        num.append(dna[o].count(a))
        if dna[o].count(a)>0:
          for b in re.finditer(a,dna[o]):
            if lista=='':
              lista=str(b.start())
            else:
              lista=lista+','+str(b.start())
        l.write('\n%20s|%27s|%21s|%23s'%(a,aa[a],dna[o].count(a),lista))
        #if completo.count(a)>0:
        códigos.append(aa2[a])
        a3.append(dna[o].count(a))
      Graficos.simples(o,a2,num)
      organismos2[o]=a3
      l.write('\n\n')
  Graficos.agrupado(códigos,organismos2)