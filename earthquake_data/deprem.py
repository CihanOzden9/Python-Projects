# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import requests
import json
from bs4 import BeautifulSoup

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AFAD Son 100 Deprem")
        self.setGeometry(200, 100, 1000, 500)
        self.show()

        self.tablo()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.tablo)
        self.timer.start()

    def tablo(self):
        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(100)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Tarih", "Yer", "Bölge", "Derinlik (km)", "Büyüklük (ML)", "Boylam", "Enlem"])
        self.table.setColumnWidth(1, 250)
        self.table.setColumnWidth(2, 200)

        url = "https://deprem.afad.gov.tr/last-earthquakes.html"
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")

        list = soup.find("tbody").find_all("tr")

        x = 0
        for td in list:
            tarih = td.find_all("td")[0].text
            yer = td.find_all("td")[6].text
            bölge = td.find_all("td")[7].text
            derinlik = td.find_all("td")[3].text
            büyüklük = td.find_all("td")[5].text
            boylam = td.find_all("td")[4].text
            enlem = td.find_all("td")[2].text

            self.table.setItem(x, 0, QtWidgets.QTableWidgetItem(tarih))
            self.table.setItem(x, 1, QtWidgets.QTableWidgetItem(yer))
            self.table.setItem(x, 2, QtWidgets.QTableWidgetItem(bölge))
            self.table.setItem(x, 3, QtWidgets.QTableWidgetItem(derinlik))
            self.table.setItem(x, 4, QtWidgets.QTableWidgetItem(büyüklük))
            self.table.setItem(x, 5, QtWidgets.QTableWidgetItem(boylam))
            self.table.setItem(x, 6, QtWidgets.QTableWidgetItem(enlem))
            x += 1

        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
