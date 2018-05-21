import numpy as np
np.set_printoptions(threshold=np.nan)

from class1 import *
import time

import BDD_Entrainement
import BDD_Verification

r = Reseau_Neurones([9,1000,6])

r.descente_gradient(BDD_Entrainement.donneeEntrainement,500,50,0.03, 0,
                    BDD_Verification.donneeEntrainement)


with open(r'..\poidsEtBiais.py','w',encoding='utf8') as f:

    f.write("import numpy as np\n\n")

    f.write("biais = ")

    f.write(str(r.biais).replace("array","np.array"))

    f.write("\n\npoids = ")

    f.write(str(r.poids).replace("array","np.array"))
