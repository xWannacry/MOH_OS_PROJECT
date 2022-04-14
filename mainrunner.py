import multiprocessing
import random
from threading import Semaphore
import threading
import time
from PySide2 import QtWidgets
from PySide2 import QtGui, QtCore as ss
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dummy_data import *
import main
import os
import numpy as np


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(MyQtApp, self).__init__()
        self.shared_qeue = multiprocessing.Queue()
        self.terminate = False
        self.avbl_rooms = 3
        self.threads = []
        self.treatments = []
        self.treat_avbl = []
        # data[0] is patients | data[1] is resources integers | data[2] is available resources
        self.e_data = getData()
        self.doctor_review = {'o': [], 'c': [], 'd': []}
        self.prog_status = True
        self.setupUi(self)
        self.semaC = Semaphore(1)
        self.semaD = Semaphore(1)
        self.semaO = Semaphore(1)
        self.sema1 = Semaphore(1)
        self.sema2 = Semaphore(1)
        self.sema3 = Semaphore(1)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon("images/logo.png"))
        self.pushButton.clicked.connect(self.mainprocess)
        self.exitbutton.clicked.connect(self.exitprogram)

    def exitprogram(self):
        self.terminate = True
        time.sleep(1)
        self.semaD.release()
        self.semaO.release()
        self.semaC.release()
        self.close()

    def preparepatients(self, qeue):
        res = []
        for i in range(10):
            for j in qeue:
                if j['doi'] == i:
                    res.append(j)
        return res

    def updatecardio(self):
        try:
            self.cardiowaiting.removeRow(0)
        except:
            pass

    def updatederma(self):
        try:
            self.dermawaiting.removeRow(0)
        except:
            pass

    def updateortho(self):
        try:
            self.orthowaiting.removeRow(0)
        except:
            pass

    def updatestat(self, itm):
        try:
            matching_items3 = self.statwaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if matching_items3:
                rmv = matching_items3[0].row()
                self.statwaiting.removeRow(rmv)
            matching_items4 = self.statinproc.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if matching_items4:
                rmv1 = matching_items4[0].row()
                self.statinproc.removeRow(rmv1)
        except:
            pass
        self.statlblwaiting.setText(str(self.statwaiting.rowCount()))
        self.statlblinproc.setText(str(self.statinproc.rowCount()))
        self.statlblfinish.setText(str(self.statfinish.rowCount()))

    def updateroomsandwainting(self, itm):
        try:
            matching_items4 = self.treatwaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if matching_items4:
                rmv1 = matching_items4[0].row()
                self.treatwaiting.removeRow(rmv1)
        except:
            pass

    def updateavailable(self):
        item1 = QtWidgets.QTableWidgetItem(str(self.treat_avbl[0]))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(self.treat_avbl[1]))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(self.treat_avbl[2]))
        item3.setTextAlignment(Qt.AlignCenter)
        self.bankeravbl.setItem(0, 0, item1)
        self.bankeravbl.setItem(0, 1, item2)
        self.bankeravbl.setItem(0, 2, item3)

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
        type_str = ''
        if int(itm['type']) == 0:
            match itm['review']:
                case 'o':
                    type_str = 'Orthopedics'
                case 'c':
                    type_str = 'Cardiology'
                case 'd':
                    type_str = 'Dermatology'
        elif int(itm['type']) == 1:
            type_str = 'Treatment'
        item5 = QtWidgets.QTableWidgetItem(type_str)
        item5.setTextAlignment(Qt.AlignCenter)
        if typeof == 'waiting':
            matching_items3 = self.statwaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items3:
                row = self.statwaiting.rowCount()
                self.statwaiting.setRowCount(row + 1)
                self.statwaiting.setItem(row, 0, item1)
                self.statwaiting.setItem(row, 1, item2)
                self.statwaiting.setItem(row, 2, item3)
                self.statwaiting.setItem(row, 3, item4)
                self.statwaiting.setItem(row, 4, item5)
        elif typeof == 'inprocess':
            matching_items0 = self.statinproc.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items0:
                row = self.statinproc.rowCount()
                self.statinproc.setRowCount(row + 1)
                self.statinproc.setItem(row, 0, item1)
                self.statinproc.setItem(row, 1, item2)
                self.statinproc.setItem(row, 2, item3)
                self.statinproc.setItem(row, 3, item4)
                self.statinproc.setItem(row, 4, item5)
        elif typeof == 'finished':
            matching_items1 = self.statfinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                row = self.statfinish.rowCount()
                self.statfinish.setRowCount(row + 1)
                self.statfinish.setItem(row, 0, item1)
                self.statfinish.setItem(row, 1, item2)
                self.statfinish.setItem(row, 2, item3)
                self.statfinish.setItem(row, 3, item4)
                self.statfinish.setItem(row, 4, item5)
        # update home counters
        self.statlblwaiting.setText(str(self.statwaiting.rowCount()))
        self.statlblinproc.setText(str(self.statinproc.rowCount()))
        self.statlblfinish.setText(str(self.statfinish.rowCount()))

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
                row = self.orthowaiting.rowCount()
                self.orthowaiting.setRowCount(row + 1)
                self.orthowaiting.setItem(row, 0, item1)
                self.orthowaiting.setItem(row, 1, item2)
                self.orthowaiting.setItem(row, 2, item3)
                self.orthowaiting.setItem(row, 3, item4)
                return row
        elif typeof == 'finished':
            matching_items1 = self.orthofinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                row = self.orthofinish.rowCount()
                self.orthofinish.setRowCount(row + 1)
                self.orthofinish.setItem(row, 0, item1)
                self.orthofinish.setItem(row, 1, item2)
                self.orthofinish.setItem(row, 2, item3)
                self.orthofinish.setItem(row, 3, item4)
                return row

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
                row = self.dermawaiting.rowCount()
                self.dermawaiting.setRowCount(row + 1)
                self.dermawaiting.setItem(row, 0, item1)
                self.dermawaiting.setItem(row, 1, item2)
                self.dermawaiting.setItem(row, 2, item3)
                self.dermawaiting.setItem(row, 3, item4)
                return row
        elif typeof == 'finished':
            matching_items1 = self.dermafinished.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                row = self.dermafinished.rowCount()
                self.dermafinished.setRowCount(row + 1)
                self.dermafinished.setItem(row, 0, item1)
                self.dermafinished.setItem(row, 1, item2)
                self.dermafinished.setItem(row, 2, item3)
                self.dermafinished.setItem(row, 3, item4)
                return row

    def addtreattables(self, itm):
        typeof = itm['status']
        item1 = QtWidgets.QTableWidgetItem(str(itm['tid']))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(itm['name']))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(itm['doi']))
        item3.setTextAlignment(Qt.AlignCenter)
        item4 = QtWidgets.QTableWidgetItem(str(itm['status']))
        item4.setTextAlignment(Qt.AlignCenter)
        item5 = QtWidgets.QTableWidgetItem(str(itm['resources']))
        item5.setTextAlignment(Qt.AlignCenter)
        if typeof == 'waiting':
            matching_items3 = self.treatwaiting.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items3:
                row = self.treatwaiting.rowCount()
                self.treatwaiting.setRowCount(row + 1)
                self.treatwaiting.setItem(row, 0, item1)
                self.treatwaiting.setItem(row, 1, item2)
                self.treatwaiting.setItem(row, 2, item3)
                self.treatwaiting.setItem(row, 3, item4)
                self.treatwaiting.setItem(row, 4, item5)
                return row
        elif typeof == 'finished':
            matching_items1 = self.treatfinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                row = self.treatfinish.rowCount()
                self.treatfinish.setRowCount(row + 1)
                self.treatfinish.setItem(row, 0, item1)
                self.treatfinish.setItem(row, 1, item2)
                self.treatfinish.setItem(row, 2, item3)
                self.treatfinish.setItem(row, 3, item4)
                self.treatfinish.setItem(row, 4, item5)
                return row

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
                row = self.cardiowaiting.rowCount()
                self.cardiowaiting.setRowCount(row + 1)
                self.cardiowaiting.setItem(row, 0, item1)
                self.cardiowaiting.setItem(row, 1, item2)
                self.cardiowaiting.setItem(row, 2, item3)
                self.cardiowaiting.setItem(row, 3, item4)
                return row
        elif typeof == 'finished':
            matching_items1 = self.cardiofinish.findItems(str(itm['tid']), ss.Qt.MatchContains)
            if not matching_items1:
                row = self.cardiofinish.rowCount()
                self.cardiofinish.setRowCount(row + 1)
                self.cardiofinish.setItem(row, 0, item1)
                self.cardiofinish.setItem(row, 1, item2)
                self.cardiofinish.setItem(row, 2, item3)
                self.cardiofinish.setItem(row, 3, item4)
                return row

    def patientC(self, data, i):  # latest
        data['tid'] = threading.get_native_id()
        self.addglobaltables(data)  # global waiting
        self.addcardiotables(data)  # cardio waiting
        while True:
            if self.terminate:
                break
            time.sleep(0.5)
            if self.semaC._value == 1 and i == self.cardiofinish.rowCount():
                self.semaC.acquire(self)
                self.cardioname.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    if self.terminate:
                        break
                    time.sleep(1)
                    self.cardiotime.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                # delete from waiting global/cardio
                self.updatestat(data)
                # self.updateglobal(row_id_w_g, row_id_in_g)  # global remove waiting
                self.updatecardio()  # derma remove waiting
                # show in finished globa/derma
                self.addglobaltables(data)  # finished global add
                self.addcardiotables(data)  # finished derma add
                self.semaC.release()
                break
        if self.cardiowaiting.rowCount() == 0:
            self.cardioname.setText('Finished!')
            self.cardiotime.setText('0')

    def patientO(self, data, i):
        data['tid'] = threading.get_native_id()
        self.addglobaltables(data)  # global waiting
        self.addorthotables(data)  # ortho waiting
        while True:
            if self.terminate:
                break
            time.sleep(0.5)
            if self.semaO._value == 1 and i == self.orthofinish.rowCount():
                self.semaO.acquire(self)
                self.orthoname.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    if self.terminate:
                        break
                    time.sleep(1)
                    self.orthotime.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                # delete from waiting global/cardio
                self.updatestat(data)
                self.updateortho()  # ortho remove waiting
                # show in finished globa/ortho
                self.addglobaltables(data)  # finished global add
                self.addorthotables(data)  # finished ortho add
                self.semaO.release()
                break
        if self.orthowaiting.rowCount() == 0:
            self.orthoname.setText('Finished!')
            self.orthotime.setText('0')

    def patientD(self, data, i):
        data['tid'] = threading.get_native_id()
        self.addglobaltables(data)  # global waiting
        self.adddematables(data)  # derma waiting
        while True:
            if self.terminate:
                break
            time.sleep(0.5)
            if self.semaD._value == 1 and i == self.dermafinished.rowCount():
                self.semaD.acquire(self)
                self.dermaname.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    if self.terminate:
                        break
                    time.sleep(1)
                    self.dermatime.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                # delete from waiting global/derma
                self.updatestat(data)
                self.updatederma()  # derma remove waiting
                # show in finished globa/derma
                self.addglobaltables(data)  # finished global add
                self.adddematables(data)  # finished derma add
                self.semaD.release()
                break
        if self.dermawaiting.rowCount() == 0:
            self.dermaname.setText('Finished!')
            self.dermatime.setText('0')

    def eligible(self, data):
        using = list(np.array(data['resources']) - np.array(data['allocated']))  # list
        rtval = np.all(np.asarray(using) <= np.asarray(self.treat_avbl))  # bool
        if rtval:
            self.treat_avbl = list(np.array(self.treat_avbl) - np.array(using))  # list
            self.updateavailable()
        return rtval

    def addalocated(self, data):
        self.treat_avbl = list(np.array(self.treat_avbl) + np.array(data['allocated']))  # list
        self.updateavailable()

    def updateroom(self, data, i):
        item1 = QtWidgets.QTableWidgetItem(str(data['tid']))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(data['name']))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(data['resources']))
        item3.setTextAlignment(Qt.AlignCenter)
        item4 = QtWidgets.QTableWidgetItem(str(data['doi']))
        item4.setTextAlignment(Qt.AlignCenter)
        self.bankeralgo.setItem(i, 0, item1)
        self.bankeralgo.setItem(i, 1, item2)
        self.bankeralgo.setItem(i, 2, item3)
        self.bankeralgo.setItem(i, 3, item4)

    def updatedetails(self, data, ix):
        iz = 0
        using = list(np.array(data['resources']) - np.array(data['allocated']))
        item1 = QtWidgets.QTableWidgetItem(str(using[0]))
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QtWidgets.QTableWidgetItem(str(using[1]))
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QtWidgets.QTableWidgetItem(str(using[2]))
        item3.setTextAlignment(Qt.AlignCenter)
        max1 = QtWidgets.QTableWidgetItem(str(data['resources'][0]))
        max1.setTextAlignment(Qt.AlignCenter)
        max2 = QtWidgets.QTableWidgetItem(str(data['resources'][1]))
        max2.setTextAlignment(Qt.AlignCenter)
        max3 = QtWidgets.QTableWidgetItem(str(data['resources'][2]))
        max3.setTextAlignment(Qt.AlignCenter)
        if ix == 0:
            self.gm1using.setItem(iz, 0, item1)
            self.gm1using.setItem(iz, 1, item2)
            self.gm1using.setItem(iz, 2, item3)
            self.gm1max.setItem(iz, 0, max1)
            self.gm1max.setItem(iz, 1, max2)
            self.gm1max.setItem(iz, 2, max3)
        elif ix == 1:
            self.gm2using.setItem(iz, 0, item1)
            self.gm2using.setItem(iz, 1, item2)
            self.gm2using.setItem(iz, 2, item3)
            self.gm2max.setItem(iz, 0, max1)
            self.gm2max.setItem(iz, 1, max2)
            self.gm2max.setItem(iz, 2, max3)
        elif ix == 2:
            self.gm3using.setItem(iz, 0, item1)
            self.gm3using.setItem(iz, 1, item2)
            self.gm3using.setItem(iz, 2, item3)
            self.gm3max.setItem(iz, 0, max1)
            self.gm3max.setItem(iz, 1, max2)
            self.gm3max.setItem(iz, 2, max3)

    def clearcounters(self, data):
        item1 = QtWidgets.QTableWidgetItem(str(""))
        item1.setTextAlignment(Qt.AlignCenter)
        iz = 0
        data['tid'] = ""
        data['name'] = ""
        data['doi'] = ""
        data['resources'] = ""
        self.updateroom(data, 0)
        self.updateroom(data, 1)
        self.updateroom(data, 2)
        self.gm1name.setText('Finished!')
        self.gm1time.setText('0')
        self.gm2name.setText('Finished!')
        self.gm2time.setText('0')
        self.gm3name.setText('Finished!')
        self.gm3time.setText('0')
        self.gm1using.setItem(iz, 0, item1)
        self.gm1using.setItem(iz, 1, item1)
        self.gm1using.setItem(iz, 2, item1)
        self.gm1max.setItem(iz, 0, item1)
        self.gm1max.setItem(iz, 1, item1)
        self.gm1max.setItem(iz, 2, item1)
        self.gm2using.setItem(iz, 0, item1)
        self.gm2using.setItem(iz, 1, item1)
        self.gm2using.setItem(iz, 2, item1)
        self.gm2max.setItem(iz, 0, item1)
        self.gm2max.setItem(iz, 1, item1)
        self.gm2max.setItem(iz, 2, item1)
        self.gm3using.setItem(iz, 0, item1)
        self.gm3using.setItem(iz, 1, item1)
        self.gm3using.setItem(iz, 2, item1)
        self.gm3max.setItem(iz, 0, item1)
        self.gm3max.setItem(iz, 1, item1)
        self.gm3max.setItem(iz, 2, item1)

    def patientT(self, data, i):
        data['tid'] = threading.get_native_id()
        data['allocated'] = [random.randint(2, int(data['resources'][0])+2),
                             random.randint(2, int(data['resources'][1])+2),
                             random.randint(2, int(data['resources'][2])+2)]
        print(data['allocated'])
        self.addglobaltables(data)  # global waiting
        self.addtreattables(data)  # treat waiting
        while True:
            if self.terminate:
                break
            time.sleep(0.5)
            if self.sema1._value == 1 and self.eligible(data) == True:
                self.sema1.acquire(self)
                self.updateroom(data, 0)
                self.updatedetails(data, 0)
                self.gm1name.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    if self.terminate:
                        break
                    time.sleep(1)
                    self.gm1time.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                # delete from waiting global/derma
                self.updatestat(data)
                self.updateroomsandwainting(data)  # remove waiting & room
                # show in finished globa/derma
                self.addglobaltables(data)  # finished global add
                self.addtreattables(data)  # finished derma add
                self.addalocated(data)
                self.sema1.release()
                break
            elif self.sema2._value == 1 and self.eligible(data) == True:
                self.sema2.acquire(self)
                self.updateroom(data, 1)
                self.updatedetails(data, 1)
                self.gm2name.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    if self.terminate:
                        break
                    time.sleep(1)
                    self.gm2time.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                # delete from waiting global/derma
                self.updatestat(data)
                self.updateroomsandwainting(data)  # remove waiting & room
                # show in finished globa/derma
                self.addglobaltables(data)  # finished global add
                self.addtreattables(data)  # finished derma add
                self.addalocated(data)
                self.sema2.release()
                break
            elif self.sema3._value == 1 and self.eligible(data) == True:
                self.sema3.acquire(self)
                self.updateroom(data, 2)
                self.updatedetails(data, 2)
                self.gm3name.setText(data['name'])
                data['status'] = 'inprocess'
                # show inprocess global
                self.addglobaltables(data)  # global inprocess
                counter = data['estime']
                while counter >= 0:
                    if self.terminate:
                        break
                    time.sleep(1)
                    self.gm3time.setText(str(counter))
                    counter -= 1
                data['status'] = 'finished'
                # delete from waiting global/treat
                self.updatestat(data)
                self.updateroomsandwainting(data)  # remove waiting & room
                # show in finished globa/treat
                self.addglobaltables(data)  # finished global add
                self.addtreattables(data)  # finished treat add
                self.addalocated(data)
                self.sema3.release()
                break
        if self.treatwaiting.rowCount() == 0:
            self.clearcounters(data)

    def schedualing_ortho(self):
        for i, per in enumerate(self.doctor_review['o']):
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientO, args=(per, i,))
            runthrd.start()
            self.threads.append(runthrd)

    def schedualing_cardio(self):
        for i, per in enumerate(self.doctor_review['c']):
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientC, args=(per, i,))
            runthrd.start()
            self.threads.append(runthrd)

    def schedualing_dema(self):
        for i, per in enumerate(self.doctor_review['d']):
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientD, args=(per, i,))
            runthrd.start()
            self.threads.append(runthrd)

    def schedualing_treatment(self):
        # waiting for shared data to be available
        while self.shared_qeue.empty():
            continue
        self.updateavailable()
        self.treatments = self.shared_qeue.get()
        self.tmpc.setText(str(len(self.treatments)))
        for i, per in enumerate(self.treatments):
            per['status'] = 'waiting'
            runthrd = threading.Thread(target=self.patientT, args=(per, i,))
            runthrd.start()
            self.threads.append(runthrd)

    def mainprocess(self):
        self.pushButton.setEnabled(False)
        self.pushButton.setText('Started !')
        self.treat_avbl = self.e_data[2]
        self.treat_avbl[0] += 5
        self.treat_avbl[1] += 5
        self.treat_avbl[2] += 5
        # using fork to process parent and child processes
        e_value = os.fork()

        # check the value to know parent or child
        # parent for doctor review proces and
        # child for treatment process in totals
        # two process
        if e_value > 0:
            # parent process
            for patient_data in self.e_data[0]:
                if patient_data['type'] == 0:
                    if patient_data['review'] == 'o':
                        self.doctor_review['o'].append(patient_data)
                    if patient_data['review'] == 'c':
                        self.doctor_review['c'].append(patient_data)
                    if patient_data['review'] == 'd':
                        self.doctor_review['d'].append(patient_data)
            self.orthocount.setText(str(len(self.doctor_review['o'])))
            self.doctor_review['o'] = self.preparepatients(self.doctor_review['o'])

            self.cardiocount.setText(str(len(self.doctor_review['c'])))
            self.doctor_review['c'] = self.preparepatients(self.doctor_review['c'])

            self.dermacount.setText(str(len(self.doctor_review['d'])))
            self.doctor_review['d'] = self.preparepatients(self.doctor_review['d'])

            alldrp = len(self.doctor_review['o']) + len(self.doctor_review['c']) + len(self.doctor_review['d'])
            self.drpc.setText(str(alldrp))

            tr1 = threading.Thread(target=self.schedualing_cardio())
            tr1.start()
            tr2 = threading.Thread(target=self.schedualing_dema())
            tr2.start()
            tr3 = threading.Thread(target=self.schedualing_ortho())
            tr3.start()
            tr4 = threading.Thread(target=self.schedualing_treatment())
            tr4.start()
        elif e_value == 0:
            for patient_data in self.e_data[0]:
                if patient_data['type'] == 1:
                    self.treatments.append(patient_data)
            self.treatments = self.preparepatients(self.treatments)
            self.shared_qeue.put(self.treatments)
        else:
            print("Couldn't handle fork!")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
