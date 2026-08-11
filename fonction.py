import webbrowser

from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt

from .constante import *

def afficheDoc():
    webbrowser.open("https://ignf.github.io/assistant-hydro-national-qgis-plugin/")

def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowType.Dialog|Qt.WindowType.WindowCloseButtonHint)
    msg.exec()

def afficherinformation(text,titre = TITRE):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowType.Dialog|Qt.WindowType.WindowCloseButtonHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)

    btnAnnuler = msg.addButton("Annuler", QMessageBox.ButtonRole.RejectRole )
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")

    btnValider = msg.addButton("Retirer du complexe", QMessageBox.ButtonRole.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")

    msg.setWindowFlags(Qt.WindowType.Dialog)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True


