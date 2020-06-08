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

  fig.savefig('Passo 3/Catalase de '+o+'.png', transparent=False, dpi=80, bbox_inches="tight")

def agrupado(aa,num):
  import matplotlib.pyplot as plt
  import matplotlib.patches as mpatches
  import numpy

  # data
  organismos=list(num.keys())
  x = numpy.arange(len(num[organismos[0]]))

  #plot data
  #use zorder to put bars in front of grid
  bar_width=0.15
  i=0
  colors=['green','red','orange','blue']
  for o in organismos:
    plt.bar(x + bar_width*i, num[o], width=bar_width, color=colors[i], zorder=2)
    i=i+1

  #labels
  #adjust x until it is centered
  plt.xticks(x + bar_width*2, aa)
  plt.title('Catalase de 4 organismos')
  plt.xlabel('Aminoácido')
  plt.ylabel('Número de ocorrências')

  #legend
  green_patch = mpatches.Patch(color='green', label=organismos[0])
  red_patch=mpatches.Patch(color='red', label=organismos[1])
  orange_patch = mpatches.Patch(color='orange', label=organismos[2])
  blue_patch = mpatches.Patch(color='blue', label=organismos[3])
  plt.legend(handles=[green_patch, red_patch,orange_patch, blue_patch],loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)

  #grid
  plt.grid(axis='y')
  plt.savefig('Passo 3/Catalase de 4 organismos.png', transparent=False, dpi=80, bbox_inches="tight")