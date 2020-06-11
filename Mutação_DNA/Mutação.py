#Escreva um programa que leia a sequencia da proteína de cada organismo armazenada no arquivo FASTA, gere um número aleatório que corresponde a posição na sequencia e outro que corresponde ao aminoácido, modifique o aminoácido na posição gerada para um aminoácido aleatório e salve a nova sequencia também no formato FASTA com novo nome 'organismo-mutacao.fasta'.
#Use o programa do passo 4 para comparar a sequencia original com a modificada.
#Faça uma mutação para cada organismo.
def mutar():
  from Comparar_DNA import Comparar as comparação
  import random
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
  cabeçalho=dict()

  for o in organismos:
    with open('DNA/'+o+'.fasta','r') as l:
      cabeçalho[o]=l.readline()
      dna[o]=l.read()

  for o in organismos:
    o2=[]
    dna1=dna[o]
    n=random.randrange(0,len(dna[o]))
    a=random.choice(list(aa.keys()))
    while a==dna1[n]:
      a=random.choice(list(aa.keys()))
    with open('Mutação_DNA/'+o+' Mutação.fasta','w') as l:
      texto=cabeçalho[o]
      l.write(texto[0:texto.find(' ')])
      l.write(' MUTATED')
      l.write(texto[texto.find(' '):])
      dna2=dna1[0:n]+a+dna1[n+1:]
      l.write(dna2)
      o2.append(o)
      o2.append(str(o+' Mutação'))
    comparação.comparar(0,aa[a],a,o2,dna1,dna2)