#Escreva um programa que compare as sequencias da mesma proteína de organismos diferentes. O programa deve detectar somente as diferenças na proteína de dois organismos e gerar na saída um arquivo que contem cabeçalho com descrição de colunas:

#posição | organismo 1 | organismo 2
#e listar essas diferença escrevendo em qual posição a diferença ocorreu e qual aminoácido aparece nessa posição para organismo 1 e organismo 2.
#Faça comparação de pelo menos três pares entre quatro organismos escolhidos.
def comparar(num,o2,dna1,dna2):
#num: numéro da comparação
#o2: lista com os dois organismos a serem comparados
#dna1: sequência da proteína do organismo 1
#dna2: sequência da proteíina do organismo 2

  #conta quantas posições são iguais para depois ver a porcentagem de semelhança
  igual=len(dna1)

  #acha qual dos organismos é o original e coloca o nome do organismo no nome do arquivo
  if o2[0].count('Mutação')!=0:
    nome=str('Mutação_DNA/Comparação mutação de '+o2[1]+'.txt')
  elif o2[1].count('Mutação')!=0:
    nome=str('Mutação_DNA/Comparação mutação de '+o2[0]+'.txt')
  else:
    #coloca o nome dos organismos no nome do arquivo
    nome=str('Comparar_DNA/Comparação '+str(num)+'.txt')
  
  with open(nome,'w') as l:

    #cabeçalho com os nomes dos organismos que estão sendo analisados
    l.write('Catalase de '+str(o2[0]).upper()+' e '+str(o2[1]).upper())

    #cabeçalho da tabela
    #Posição|Organismo 1|Organismo 2
    l.write('\n%7s|%14s|%14s'%('Posição',o2[0],o2[1]))

    for i in range(len(dna1)):
      if dna1[i]!=dna2[i]:
        igual=igual-1

        #escreve cada linha da tabela
        #Posição, Aminoácido nessa posição no organismo 1 e Aminoácido nessa posição no organismo 2
        l.write('\n%7s|%14s|%14s'%(i,dna1[i],dna2[i]))

    #porcentagem de semelhança
    igual=(igual/len(dna1))*100
    igual=round(igual, 2)
    l.write('\n\n'+str(igual)+'% de semelhança')