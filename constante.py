import os

TITRE = "Assistant hydrographique national"
VERSION = "v1.0.0"
PATH_REP = f"{os.path.dirname(__file__)}"
CLEABS = "cleabs"

LIST_LINEEDIT_READ_ONLY = ["cleabs","code_hydrographique","cpx_toponyme_de_cours_d_eau"]
LIST_COMBOBOX_READ_ONLY = ["fictif","origine","persistance","type_d_annexe","type_de_bras","delimitation","sens_de_l_ecoulement"]
LIST_LABEL_BLOC1 = ["label_inventaire_pe","label_identifiant_police_de_l_eau"]
LIST_LABEL_BLOC2 = ["label_inventaire_bcae","label_identifiant_bcae"]

LAYER_HYDRO = "troncon_hydrographique"

# 0 : combo → fond vert ou desactivé
# 1 : modification d'attributs → fond rose
# 2 : pas de fond
# 3 : bouton valider
# 4 : label → gris clair
# 5 : bloc de label 1
# 6 : bloc de label 2
CUSTOM_WIDGETS = (" *{background-color: #2ee321;font-weight: bold;} *:disabled {background-color: #dcdcdc;color: grey}",
                    "background-color: #ff8080 ;font-weight: bold",
                    "background-color: None",
                    "background-color: #df920d ;font-weight: bold",
                    "background-color: #dcdcdc",
                    "background-color: #8be8fa",
                    "background-color: #88f4b1"
                  )






