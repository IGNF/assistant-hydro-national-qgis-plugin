import os.path
import webbrowser

from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt


from .constante import *
import subprocess



def afficheDoc():
    webbrowser.open("https://ignf.github.io/assistant-hydro-national-qgis-plugin/")

def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.WindowCloseButtonHint)
    msg.exec()

def afficherinformation(text,titre = TITRE):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.WindowCloseButtonHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)

    btnAnnuler = msg.addButton("Annuler", QMessageBox.RejectRole )
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")

    btnValider = msg.addButton("Retirer du complexe", QMessageBox.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")

    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True


