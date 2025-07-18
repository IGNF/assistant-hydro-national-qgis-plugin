import os

TITRE = "Assisstant hydrographique national"
PATH_REP = f"{os.path.dirname(__file__)}"
CLEABS = "cleabs"


LAYER_HYDRO = "troncon_hydrographique"

# 0 : bouton clické → fond vert
# 1 : valeur de l'objet → fond rose
# 2 : pas de fond
# 3 : bouton valider
# 4 : label
CUSTOM_WIDGETS = ("background-color: #2ab51a ;font-weight: bold",
                  "background-color: #ff8080 ;font-weight: bold",
                  "background-color: None",
                  "background-color: #df920d ;font-weight: bold",
                  "background-color: #dcdcdc"
                  )



