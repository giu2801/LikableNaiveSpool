#Para realizar este passo escreva um programa que leia cada arquivo de proteína baixada em formato FASTA, identifique todos os animoácidos e gere um arquivo com o nome no formato 'proteína-aminoacidos.txt' com uma tabela com as seguintes colunas:
#Código do aminoácido | Nome completo do aminoácido | O número de ocorrências na sequencia | Lista de posições de ocorrências separadas com vírgula
#Prepare um histograma de número de ocorrências de aminoácidos para cada organismo usando biblioteca matplotlib.

def analisar(organismos,aa,dna,aa2):
#organimos:lista de organismos
#aa:dicionário com código e nome dos aminoácidos
#dna:dicionario com organismo e código genético dele
#aa2:dicionário com código e código de três letras de cada aminoácido

  import re
  import Graficos

  with open('Analise_DNA/Catalase-aminoacidos.txt','w') as l:
    
    #dicionário que recebe a contagem de cada aminoácido por organismo
    organismos2=dict()

    #fazer uma tabela de aminoácidos para cada organismo (todas as tabelas no mesmo arquivo txt)
    for o in organismos:
      l.write(o.upper())
      l.write('\n%20s|%27s|%21s|%1s'%('Código do aminoácido','Nome do aminoácido','Número de ocorrências','Posições de ocorrências'))

      #lista de contagem de cada aminoácido de um organismos
      a3=[]

      #lista de nomes de cada aminoácido
      a2=aa.values()

      #lista de contagem de cada aminoácido em um organismo
      num=[]

      #lista de código de três letras de cada aminoácido
      códigos=aa2.values()

      for a in aa:
        #lista de posições de um aminoácido
        lista=[]

        num.append(dna[o].count(a))

        if dna[o].count(a)>0:
          for b in re.finditer(a,dna[o]):
            lista.append(b.start())
        
        lista=str(lista).replace('[','')
        lista=lista.replace(']','')
        lista=lista.replace(' ','')

        #escreve cada linha da tabela
        #'Código do aminoácido','Nome do aminoácido','Número de ocorrências','Posições de ocorrências'
        l.write('\n%20s|%27s|%21s|%1s'%(a,aa[a],dna[o].count(a),lista))

        a3.append(dna[o].count(a))
      
      #faz o gráfico em barras com a contagem de aminoácidos de um organismo (imagens com o nome 'Catalase de...' na pasta Analise_DNA)
      Graficos.simples(o,a2,num)

      organismos2[o]=a3

      #pular uma linha dps de cada tabela
      l.write('\n\n')

  #faz o gráfico em barras agrupado com a contagem de aminoácidos de todos os organismos (imagem com o nome 'Catalase de 4 organismos' na pasta Analise_DNA)
  Graficos.agrupado(códigos,organismos2)