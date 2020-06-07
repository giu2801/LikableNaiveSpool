import matplotlib.pyplot as plt
import numpy as np

def simples(o,aa,num):
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

  fig.savefig('Catalase de '+o+'.png', transparent=False, dpi=80, bbox_inches="tight")