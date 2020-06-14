#Escreva um programa que leia a sequencia da proteína de cada organismo armazenada no arquivo FASTA, gere um número aleatório que corresponde a posição na sequencia e outro que corresponde ao aminoácido, modifique o aminoácido na posição gerada para um aminoácido aleatório e salve a nova sequencia também no formato FASTA com novo nome 'organismo-mutacao.fasta'.
#Use o programa do passo 4 para comparar a sequencia original com a modificada.
#Faça uma mutação para cada organismo.
def mutar(dna1,aa,o,cabeçalho):
  #dna1: sequencia da proteína do organismo
  #aa: dicionário com código e nome dos aminoácidos
  #o: nome do organismo
  #cabeçalho: dicionário com o nome do organismo e o cabeçalho do arquivo fasta dele

  from Comparar_DNA import Comparar as comparação

  import random

  #lista com nome dois organismos, o original e o mutado
  o2=[]

  n=random.randrange(0,len(dna1))
  a=random.choice(list(aa.keys()))

  while a==dna1[n]:
    a=random.choice(list(aa.keys()))
  
  with open('Mutação_DNA/'+o+' Mutação.fasta','w') as l:
    l.write(cabeçalho[0:cabeçalho.find(' ')])
    l.write(' MUTATED')
    l.write(cabeçalho[cabeçalho.find(' '):])
    dna2=dna1[0:n]+a+dna1[n+1:]
    l.write(dna2)
    o2.append(o)
    o2.append(str(o+' Mutação'))
  comparação.comparar(0,o2,dna1,dna2)