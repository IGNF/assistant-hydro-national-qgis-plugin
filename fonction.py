import webbrowser

from .constante import *
from .mapping_version import *

def afficheDoc():
    webbrowser.open("https://ignf.github.io/assistant-hydro-national-qgis-plugin/")

def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(Ok)
    msg.setText(text)
    msg.setWindowFlags(WindowStaysOnTopHint|WindowCloseButtonHint)
    msg.exec()

def afficherinformation(text,titre = TITRE):
    msg = QMessageBox()
    msg.setIcon(Information)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(Ok)
    msg.setText(text)
    msg.setWindowFlags(WindowStaysOnTopHint|WindowCloseButtonHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)

    btnAnnuler = msg.addButton("Annuler", RejectRole )
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")

    btnValider = msg.addButton("Retirer du complexe", AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")

    msg.setWindowFlags(WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True


