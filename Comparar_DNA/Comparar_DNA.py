def comparar():
  import random
  import re
  aa=dict()
  with open('DNA/Aminoacidos.txt','r') as l:
    for line in l.readlines():
      a=line.replace('\n','').split('\t')
      aa[a[0]]=a[1]

  organismos=['Camundongo','Cão','Gado-doméstico','Humano']
  dna=dict()

  for o in organismos:
    with open('DNA/'+o+'.fasta','r') as l:
      l.readline()
      dna[o]=l.read()

  o=[]
  a=[]
  for i in range(3):
    while True:
      a2=random.choice(list(aa.keys()))
      o2=random.sample(organismos,2)
      if o2[0]==o2[1]:
        while o2[0]==o2[1]:
          o2=random.sample(organismos,2)
      dna1=str(dna[o2[0]])
      dna2=str(dna[o2[1]])
      if dna1.count(a2)>0 or dna2.count(a2)>0:
        if o.count([o2[0],o2[1],a2])==0 and o.count([o2[1],o2[0],a2])==0:
          o.append([o2[0],o2[1]])
          a.append(a2)
          break
    with open('Comparar_DNA/Comparação '+str(i)+'txt','w') as l:
      l.write(str(aa[a2]).upper()+' na Catalase de '+str(o2[0]).upper()+' e '+str(o2[1]).upper())
      l.write('\n%7s|%14s|%14s'%('Posição',o2[0],o2[1]))
      if dna1.count(a2)>0:
        for b in re.finditer(a2,dna1):
          if(dna1[b.start()]!=dna2[b.start()]):
            l.write('\n%7s|%14s|%11s'%(b.start(),dna1[b.start()],dna2[b.start()]))
      if dna2.count(a2)>0:
        for c in re.finditer(a2,dna2):
          if(dna1[c.start()]!=dna2[c.start()]):
            l.write('\n%7s|%14s|%11s'%(c.start(),dna1[c.start()],dna2[c.start()]))