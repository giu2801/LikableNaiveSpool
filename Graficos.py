def simples(o,aa,num):
  import matplotlib.pyplot as plt
  import numpy as np
  # Fixing random state for reproducibility
  np.random.seed(19680801)
  plt.rcdefaults()
  plt.rcParams.update({'figure.autolayout': True})
  fig, ax = plt.subplots()

  # Example data
  y_pos = np.arange(len(aa))

  ax.barh(y_pos, num, align='center')
  ax.set_yticks(y_pos)
  ax.set_yticklabels(aa)
  ax.invert_yaxis()  # labels read top-to-bottom
  ax.set_xlabel('Número de ocorrências')
  ax.set(ylabel='Aminoácido')
  ax.set_title('Catalase de '+o)

  #plt.show()

  fig.savefig('Analise_DNA/Catalase de '+o+'.png', transparent=False, dpi=80, bbox_inches="tight")
  plt.close('all')

def agrupado(aa,num):
  import matplotlib.pyplot as plt
  import numpy

  # data
  organismos=list(num.keys())
  x = numpy.arange(len(num[organismos[0]]))

  #plot data
  #use zorder to put bars in front of grid
  bar_width=0.2
  i=0
  colors=['green','red','orange','blue']
  for o in organismos:
    plt.bar(x + bar_width*i, num[o], width=bar_width, color=colors[i],label=o)
    i=i+1

  #labels
  #adjust x until it is centered
  plt.xticks(x+ bar_width*3/2, aa)
  plt.title('Catalase de 4 organismos')
  plt.xlabel('Aminoácido')
  plt.ylabel('Número de ocorrências')

  #legend
  plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          ncol=4, fancybox=True)

  #grid
  plt.grid(axis='y')
  plt.savefig('Analise_DNA/Catalase de 4 organismos.png', transparent=False, dpi=80, bbox_inches="tight")
  plt.close('all')