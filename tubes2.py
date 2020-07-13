# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector #menyambungkan file dengan mysql agar bisa terhubung kedatabase

class Ui_Dialog(object):    #class 

    def koneksi(self):                      #fungsi
        con = mysql.connector.connect(      #membuat variabel con yang bisa menghubungkan ke database perpus 
            host="localhost",
            user="root",
            passwd="",
            database = "perpus"
        )

        mycursor = con.cursor()

    def setupUi(self, Dialog):                                      # fungsi setupUi untuk
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.koneksi()                                              # memanggil fungsi koneksi untuk bisa dijalankan di program
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(120, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(31, 58, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(31, 91, 47, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(31, 124, 47, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(31, 157, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(31, 190, 51, 16))
        self.label_6.setObjectName("label_6")
        self.nimEdit = QtWidgets.QLineEdit(self.tab)
        self.nimEdit.setGeometry(QtCore.QRect(100, 58, 201, 20))
        self.nimEdit.setObjectName("nimEdit")
        self.namaEdit = QtWidgets.QLineEdit(self.tab)
        self.namaEdit.setGeometry(QtCore.QRect(100, 91, 201, 20))
        self.namaEdit.setObjectName("namaEdit")
        self.kelasEdit = QtWidgets.QLineEdit(self.tab)
        self.kelasEdit.setGeometry(QtCore.QRect(100, 124, 201, 20))
        self.kelasEdit.setObjectName("kelasEdit")
        self.nomerEdit = QtWidgets.QLineEdit(self.tab)
        self.nomerEdit.setGeometry(QtCore.QRect(100, 160, 201, 20))
        self.nomerEdit.setObjectName("nomerEdit")
        self.judulEdit = QtWidgets.QLineEdit(self.tab)
        self.judulEdit.setGeometry(QtCore.QRect(100, 190, 201, 20))
        self.judulEdit.setObjectName("judulEdit")
        self.simpanButton = QtWidgets.QPushButton(self.tab)
        self.simpanButton.setGeometry(QtCore.QRect(21, 231, 75, 23))
        self.simpanButton.setObjectName("simpanButton")
        self.simpanButton.clicked.connect(self.simpan)
        self.ubahButton = QtWidgets.QPushButton(self.tab)
        self.ubahButton.setGeometry(QtCore.QRect(110, 231, 75, 23))
        self.ubahButton.setObjectName("ubahButton")
        self.ubahButton.clicked.connect(self.ubah)
        self.hapusButton = QtWidgets.QPushButton(self.tab)
        self.hapusButton.setGeometry(QtCore.QRect(199, 231, 75, 23))
        self.hapusButton.setObjectName("hapusButton")
        self.hapusButton.clicked.connect(self.hapus)
        self.bersihButton = QtWidgets.QPushButton(self.tab)
        self.bersihButton.setGeometry(QtCore.QRect(287, 231, 75, 23))
        self.bersihButton.setObjectName("bersihButton")
        self.bersihButton.clicked.connect(self.bersih)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tblNilai = QtWidgets.QTableWidget(self.tab_2)
        self.tblNilai.setGeometry(QtCore.QRect(10, 30, 371, 201))
        self.tblNilai.setRowCount(5)
        self.tblNilai.setColumnCount(5)
        self.tblNilai.setObjectName("tblNilai")
        self.tampilButton = QtWidgets.QPushButton(self.tab_2)
        self.tampilButton.setGeometry(QtCore.QRect(150, 240, 75, 23))
        self.tampilButton.setObjectName("tampilButton")
        self.tampilButton.clicked.connect(self.tampil)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "INPUT DATA BUKU"))
        self.label_2.setText(_translate("Dialog", "NIM"))
        self.label_3.setText(_translate("Dialog", "Nama"))
        self.label_4.setText(_translate("Dialog", "Kelas"))
        self.label_5.setText(_translate("Dialog", "Nomer Buku"))
        self.label_6.setText(_translate("Dialog", "Judul Buku"))
        self.simpanButton.setText(_translate("Dialog", "Simpan"))
        self.ubahButton.setText(_translate("Dialog", "Ubah"))
        self.hapusButton.setText(_translate("Dialog", "Hapus"))
        self.bersihButton.setText(_translate("Dialog", "Bersihkan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Input"))
        self.tampilButton.setText(_translate("Dialog", "Tampilkan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tabel"))

    def bersih(self): #fungsi ini untuk membersihkan jika ada text yang di lineEdit
        self.nimEdit.clear()
        self.namaEdit.clear()
        self.kelasEdit.clear()
        self.judulEdit.clear()
        self.nomerEdit.clear()
    
    def simpan(self):              # fungsi simpan untuk menyimpan data kedalam database
        nim = self.nimEdit.text()
        nama = self.namaEdit.text()
        kelas = self.kelasEdit.text()
        nomer = self.nomerEdit.text()
        judul = self.judulEdit.text()

        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "perpus"
        )

        mycursor = con.cursor()
        sql = "INSERT INTO buku VALUES (%s,%s,%s,%s,%s)"
        data = mycursor.execute(sql,(nim, nama, kelas, nomer, judul))
        con.commit()

    def ubah(self): # fungsi ubah untuk mengubah data yang ada di dalam database
        nim = self.nimEdit.text()
        nama = self.namaEdit.text()
        kelas = self.kelasEdit.text()
        nomer = self.nomerEdit.text()
        judul = self.judulEdit.text()

        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "perpus"
        )

        mycursor = con.cursor()
        sql = "UPDATE buku SET nim=%s, nama=%s, kelas=%s, nomerbuku=%s, judulbuku=%s WHERE nomerbuku=%s"
        data = mycursor.execute(sql,(nim, nama, kelas, nomer, judul, nomer))
        con.commit()        

    def hapus(self): # fungsi hapus untuk menghapus data yang ada di dalam database
        nomer = self.nomerEdit.text()

        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "perpus"
        )

        mycursor = con.cursor()
        sql = "DELETE FROM buku WHERE nomerbuku ="+nomer+" "
        data = mycursor.execute(sql)
        con.commit()        

    def tampil(self):# fungsi ini untuk menampilkan yang ada di dalam database dan memasukannya kedalam table widget yang tersedia
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "perpus"
        )

        mycursor = con.cursor()
        result = mycursor.execute("SELECT * FROM buku")
        self.tblNilai.setRowCount(0)

        for row_number, row_data in enumerate(mycursor):    # ini adalah perulangan untuk mengeluarkan data yang ada di dalam database
            self.tblNilai.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tblNilai.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
