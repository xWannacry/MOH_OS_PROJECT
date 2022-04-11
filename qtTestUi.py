import threading
import time

from PySide2 import QtWidgets
from PySide2 import QtGui, QtCore as ss
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dummy_data import *
import main
import os

from threading import *


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(MyQtApp, self).__init__()
        self.threads = []
        self.treatments = []
        self.doctor_review = {'o': [], 'c': [], 'd': []}
        self.prog_status = True
        self.setupUi(self)
        self.semaC = Semaphore
        self.semaD = Semaphore
        self.semaO = Semaphore
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon("images/logo.png"))
        self.pushButton.clicked.connect(self.mainprocess)

    def preparepatients(self, qeue):
        res = []
        for i in range(10):
            for j in qeue:
                if j['doi'] == i:
                    res.append(j)
        return res

    def updateglobal(self, row_id_w,row_id_in):
        try:
            self.statwaiting.removeRow(row_id_w)
            self.statinproc.removeRow(row_id_in)
        except:
            pass

    def updatecardio(self, rowid):
        try:
            self.cardiowaiting.removeRow(rowid)
        except:
            pass

    def updatederma(self, rowid):
        try:
            self.dermawaiting.removeRow(rowid)
        except:
            pass

    def updateortho(self, rowid):
        try:
            self.orthowaiting.removeRow(rowid)
        except:
            pass

    def addglobaltables(self, itm):
        typeof = itm['status']
        item1 = QtWidgets.QTableWidgetItem(str(itm['tid']))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(itm['name']))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(itm['doi']))
        item3.setTextAlignment(Qt.AlignCenter)
        item4 = QtWidgets.QTableWidgetItem(str(itm['status']))
        item4.setTextAlignment(Qt.AlignCenter)
        if typeof == 'waiting':
            matching_items3 = self.statwaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items3:
                rowPosition1 = self.statwaiting.rowCount()
                self.statwaiting.setRowCount(rowPosition1 + 1)
                self.statwaiting.setItem(rowPosition1, 0, item1)
                self.statwaiting.setItem(rowPosition1, 1, item2)
                self.statwaiting.setItem(rowPosition1, 2, item3)
                self.statwaiting.setItem(rowPosition1, 3, item4)
                return rowPosition1
        elif typeof == 'inprocess':
            matching_items0 = self.statinproc.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items0:
                rowPosition2 = self.statinproc.rowCount()
                self.statinproc.setRowCount(rowPosition2 + 1)
                self.statinproc.setItem(rowPosition2, 0, item1)
                self.statinproc.setItem(rowPosition2, 1, item2)
                self.statinproc.setItem(rowPosition2, 2, item3)
                self.statinproc.setItem(rowPosition2, 3, item4)
                return rowPosition2
        elif typeof == 'finished':
            matching_items1 = self.statfinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                rowPosition3 = self.statfinish.rowCount()
                self.statfinish.setRowCount(rowPosition3 + 1)
                self.statfinish.setItem(rowPosition3, 0, item1)
                self.statfinish.setItem(rowPosition3, 1, item2)
                self.statfinish.setItem(rowPosition3, 2, item3)
                self.statfinish.setItem(rowPosition3, 3, item4)
                return rowPosition3

    def addorthotables(self, itm):
        typeof = itm['status']
        item1 = QtWidgets.QTableWidgetItem(str(itm['tid']))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(itm['name']))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(itm['doi']))
        item3.setTextAlignment(Qt.AlignCenter)
        item4 = QtWidgets.QTableWidgetItem(str(itm['status']))
        item4.setTextAlignment(Qt.AlignCenter)
        if typeof == 'waiting':
            matching_items3 = self.orthowaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items3:
                rowPosition1 = self.orthowaiting.rowCount()
                self.orthowaiting.setRowCount(rowPosition1 + 1)
                self.orthowaiting.setItem(rowPosition1, 0, item1)
                self.orthowaiting.setItem(rowPosition1, 1, item2)
                self.orthowaiting.setItem(rowPosition1, 2, item3)
                self.orthowaiting.setItem(rowPosition1, 3, item4)
                return rowPosition1
        elif typeof == 'finished':
            matching_items1 = self.orthofinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                rowPosition3 = self.orthofinish.rowCount()
                self.orthofinish.setRowCount(rowPosition3 + 1)
                self.orthofinish.setItem(rowPosition3, 0, item1)
                self.orthofinish.setItem(rowPosition3, 1, item2)
                self.orthofinish.setItem(rowPosition3, 2, item3)
                self.orthofinish.setItem(rowPosition3, 3, item4)
                return rowPosition3

    def adddematables(self, itm):
        typeof = itm['status']
        item1 = QtWidgets.QTableWidgetItem(str(itm['tid']))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(itm['name']))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(itm['doi']))
        item3.setTextAlignment(Qt.AlignCenter)
        item4 = QtWidgets.QTableWidgetItem(str(itm['status']))
        item4.setTextAlignment(Qt.AlignCenter)
        if typeof == 'waiting':
            matching_items3 = self.dermawaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items3:
                rowPosition1 = self.dermawaiting.rowCount()
                self.dermawaiting.setRowCount(rowPosition1 + 1)
                self.dermawaiting.setItem(rowPosition1, 0, item1)
                self.dermawaiting.setItem(rowPosition1, 1, item2)
                self.dermawaiting.setItem(rowPosition1, 2, item3)
                self.dermawaiting.setItem(rowPosition1, 3, item4)
                return rowPosition1
        elif typeof == 'finished':
            matching_items1 = self.dermafinished.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                rowPosition3 = self.dermafinished.rowCount()
                self.dermafinished.setRowCount(rowPosition3 + 1)
                self.dermafinished.setItem(rowPosition3, 0, item1)
                self.dermafinished.setItem(rowPosition3, 1, item2)
                self.dermafinished.setItem(rowPosition3, 2, item3)
                self.dermafinished.setItem(rowPosition3, 3, item4)
                return rowPosition3

    def addcardiotables(self, itm):
        typeof = itm['status']
        item1 = QtWidgets.QTableWidgetItem(str(itm['tid']))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(itm['name']))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(itm['doi']))
        item3.setTextAlignment(Qt.AlignCenter)
        item4 = QtWidgets.QTableWidgetItem(str(itm['status']))
        item4.setTextAlignment(Qt.AlignCenter)
        if typeof == 'waiting':
            matching_items3 = self.cardiowaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items3:
                rowPosition1 = self.cardiowaiting.rowCount()
                self.cardiowaiting.setRowCount(rowPosition1 + 1)
                self.cardiowaiting.setItem(rowPosition1, 0, item1)
                self.cardiowaiting.setItem(rowPosition1, 1, item2)
                self.cardiowaiting.setItem(rowPosition1, 2, item3)
                self.cardiowaiting.setItem(rowPosition1, 3, item4)
                return rowPosition1
        elif typeof == 'finished':
            matching_items1 = self.cardiofinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                rowPosition3 = self.cardiofinish.rowCount()
                self.cardiofinish.setRowCount(rowPosition3 + 1)
                self.cardiofinish.setItem(rowPosition3, 0, item1)
                self.cardiofinish.setItem(rowPosition3, 1, item2)
                self.cardiofinish.setItem(rowPosition3, 2, item3)
                self.cardiofinish.setItem(rowPosition3, 3, item4)
                return rowPosition3

    def patientC(self, data):
        data['tid'] = threading.get_native_id()
        row_id_w_g = self.addglobaltables(data)  # global waiting
        row_id_w_c = self.addcardiotables(data)  # cardio waiting
        while True:
            if self.semaC._value == 1:
                self.semaC.acquire()
                self.cardioname.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global/ cardio
                row_id_in_g = self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    time.sleep(1)
                    self.cardiotime.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                self.semaC.release()
                # delete from waiting global/cardi
                self.updateglobal(row_id_w_g,row_id_in_g)  # global remove waiting
                self.updatecardio(row_id_w_c)  # cardio remove waiting
                # show in finished globa/cardio
                self.addglobaltables(data) # finished global add
                self.addcardiotables(data) # finished cardio add

    def patientO(self, data):
        data['tid'] = threading.get_native_id()
        row_id_w_g = self.addglobaltables(data)  # global waiting
        row_id_w_c = self.addorthotables(data)  # ortho waiting
        while True:
            if self.semaO._value == 1:
                self.semaO.acquire()
                self.orthoname.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                row_id_in_g = self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    time.sleep(1)
                    self.orthotime.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                self.semaO.release()
                # delete from waiting global/ortho
                self.updateglobal(row_id_w_g,row_id_in_g)  # global remove waiting
                self.updateortho(row_id_w_c)  # ortho remove waiting
                # show in finished globa/ortho
                self.addglobaltables(data) # finished global add
                self.addorthotables(data) # finished ortho add

    def patientD(self, data):
        data['tid'] = threading.get_native_id()
        row_id_w_g = self.addglobaltables(data)  # global waiting
        row_id_w_c = self.adddematables(data)  # derma waiting
        while True:
            if self.semaD._value == 1:
                self.semaD.acquire()
                self.dermaname.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                row_id_in_g = self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    time.sleep(1)
                    self.dermatime.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                self.semaD.release()
                # delete from waiting global/derma
                self.updateglobal(row_id_w_g,row_id_in_g)  # global remove waiting
                self.updatederma(row_id_w_c)  # derma remove waiting
                # show in finished globa/derma
                self.addglobaltables(data) # finished global add
                self.adddematables(data) # finished derma add

    def monitoring(self):
        while self.prog_status == True or len(self.threads) > 0:
            try:
                for thread in self.threads:
                    if thread.info['status'] == 'waiting':
                        self.addtableshome()
            except:
                pass

    def schedualing_ortho(self):
        for per in self.doctor_review['o']:
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientD, args=(per,))
            runthrd.start()
            self.threads.append(runthrd)

    def schedualing_cardio(self):
        for per in self.doctor_review['c']:
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientC, args=(per,))
            runthrd.start()
            self.threads.append(runthrd)

    def schedualing_dema(self):
        for per in self.doctor_review['d']:
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientD, args=(per,))
            runthrd.start()
            self.threads.append(runthrd)

    def schedualing_treatment(self):
        pass

    def mainprocess(self):
        # monitor all threads
        # self.monitoring()
        # get dummy data for testing
        e_data = getData()

        # using fork to process parent and child processes
        e_value = os.fork()

        # process each patient
        for patient_data in e_data:

            # check the value to know parent or child
            # parent for doctor review proces and
            # child for treatment process in total
            # two process
            if e_value > 0 and patient_data['type'] == 0:
                if patient_data['review'] == 'o':
                    self.doctor_review['o'].append(patient_data)
                if patient_data['review'] == 'c':
                    self.doctor_review['c'].append(patient_data)
                if patient_data['review'] == 'd':
                    self.doctor_review['d'].append(patient_data)
            elif e_value == 0 and patient_data['type'] == 1:
                self.treatments.append(patient_data)
            else:
                print("Couldn't handle fork!")

        self.orthocount.setText(str(len(self.doctor_review['o'])))
        self.doctor_review['o'] = self.preparepatients(self.doctor_review['o'])

        self.cardiocount.setText(str(len(self.doctor_review['c'])))
        self.doctor_review['c'] = self.preparepatients(self.doctor_review['c'])

        self.dermacount.setText(str(len(self.doctor_review['d'])))
        self.doctor_review['d'] = self.preparepatients(self.doctor_review['d'])

        self.treatments = self.preparepatients(self.treatments)

        self.schedualing_cardio()
        self.schedualing_dema()
        self.schedualing_ortho()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
