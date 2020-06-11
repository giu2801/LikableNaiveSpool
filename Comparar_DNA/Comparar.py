#Escreva um programa que compare as sequencias da mesma proteína de organismos diferentes. O programa deve detectar somente as diferenças na proteína de dois organismos e gerar na saída um arquivo que contem cabeçalho com descrição de colunas:

#posição | organismo 1 | organismo 2
#e listar essas diferença escrevendo em qual posição a diferença ocorreu e qual aminoácido aparece nessa posição para organismo 1 e organismo 2.
#Faça comparação de pelo menos três pares entre quatro organismos escolhidos.
def comparar(num,aa,a2,o2,dna1,dna2):
  import re
  if o2[0].count('Mutação')!=0:
    nome=str('Mutação_DNA/Comparação mutação de '+o2[1]+'.txt')
  elif o2[1].count('Mutação')!=0:
    nome=str('Mutação_DNA/Comparação mutação de '+o2[0]+'.txt')
  else:
    nome=str('Comparar_DNA/Comparação '+str(num)+'.txt')
  with open(nome,'w') as l:
    l.write(str(aa).upper()+'('+a2+')'+' na Catalase de '+str(o2[0]).upper()+' e '+str(o2[1]).upper())
    l.write('\n%7s|%14s|%14s'%('Posição',o2[0],o2[1]))
    if dna1.count(a2)>0:
      for b in re.finditer(a2,dna1):
        if(dna1[b.start()]!=dna2[b.start()]):
          l.write('\n%7s|%14s|%14s'%(b.start(),dna1[b.start()],dna2[b.start()]))
    if dna2.count(a2)>0:
      for c in re.finditer(a2,dna2):
        if(dna1[c.start()]!=dna2[c.start()]):
          l.write('\n%7s|%14s|%14s'%(c.start(),dna1[c.start()],dna2[c.start()]))