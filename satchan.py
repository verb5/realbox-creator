#!/usr/bin/env python
from time import sleep
from PySide.QtCore import *
from PySide.QtGui import *
from kingofsat import Satellite
from threading import Thread
import sys,mainWindow
import time,re,inspect,sqlite3


BAZA='bazata'

class getData(QThread):
    def __init__(self,parent=None):
        super(getData,self).__init__()

    def run(self):
        self.sati=appSat.dialog.satLista.currentText()
        self.satData=Satellite(sat=appSat.satelites[self.sati])
    #print 'gotovo %s'%self.satData.satParameters
        self.satData.get(self.sati[-5:])
        #for trans in sorted(self.satData.satParameters):
        #    print trans
        #print sati
        #pass



            ######################### copy / paste ########################################
            #for chan in self.satData.satParameters[trans].setdefault('tansponderChannels',[]):
            #    print chan
            #    item=QStandardItem(chan)
            #    item.setCheckState(Qt.Unchecked)
            #    item.setCheckable(True)
            #    item.setEditable(False)
            #    item.setSelectable(True)
            #
            #    print item
            #    appSat.model.appendRow(item)








class SatApp(QDialog):
    def __init__(self,parent=None):
        self.id=0
        super(SatApp,self).__init__()
        #storing the selected db
        self.storDb={}

        self.dialog=mainWindow.Ui_Dialog()
        self.dialog.setupUi(self)
        self.setWindowTitle('RealBox chanlist')
        self.satelites={'Hotbird 13.0E':'http://en.kingofsat.net/pos-13E.php',
                        'Astra 19.2E':'http://en.kingofsat.net/pos-19.2E.php',
                        'Astra 28.2E':'http://en.kingofsat.net/pos-28.2E.php',
                        'Intelsat 901 18.0W':'http://en.kingofsat.net/pos-18W.php',
                        'Hellas 39.0E':'http://en.kingofsat.net/pos-39E.php'}
        self.model=QStandardItemModel()
        self.model2=QStandardItemModel()
        self.dialog.chanList1.setModel(self.model)
        self.dialog.chanList2.setModel(self.model2)
        self.dialog.download.clicked.connect(self.fetchChan)
        self.dialog.satLista.addItems(self.satelites.keys())
        self.dialog.rightBtn.clicked.connect(self.transmit)
        #self.dialog.status.setText('proba')
        self.dialog.chanList2.horizontalHeader().setVisible(False)
        self.dialog.chanList2.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        #self.dialog.chanList2.resizeColumnsToContents()
        #self.dialog.chanList2.setColumnWidth(1,400)
        self.dialog.upBtn.clicked.connect(self.moveUp)
        self.dialog.downBtn.clicked.connect(self.moveDown)
        self.dialog.chanList2.setAcceptDrops(True)
        self.dialog.satLista.currentIndexChanged.connect(self.populateList)
        #self.dialog.chanList2.setDragEnabled(True)
        #self.dialog.chanList1.setDragEnabled(True)
        self.populateList()
        self.finished.connect(self.selected)

    def selected(self):

        baza=sqlite3.connect(BAZA)
        c=baza.cursor()
        c.execute('update parameters set selected=0')
        baza.commit()
        baza.close()
    def setAlert(self):
        self.dialog.status.setText('Loading..')

    def endAlert(self):
        self.dialog.status.clear()

    def populateList(self):
        #print 'trugna'
        #pulni s kanali listata
        self.model.clear()
        self.sati=str(self.dialog.satLista.currentText()[-5:])
        #print sati
        baza=sqlite3.connect(BAZA)
        c=baza.cursor()

        try:
            c.execute('select channel,selected from parameters where degree="%s"'%self.sati)
            for (channel,selected) in c.fetchall():
                item=QStandardItem(channel)

                item.setEditable(False)
                item.setSelectable(True)
                if selected == 1:
                    item.setCheckState(Qt.Checked)
                    item.setCheckable(False)
                    item.setEnabled(False)
                else:
                    item.setCheckState(Qt.Unchecked)
                    item.setCheckable(True)
                #print item
                self.model.appendRow(item)
                print channel
        except Exception as e:
            print e


    def fetchChan(self):
        self.model.clear()
        baza=sqlite3.connect(BAZA)
        c=baza.cursor()
        baza.commit()
        baza.close()
        self.tred=getData()
        self.tred.started.connect(self.setAlert)
        self.tred.finished.connect(self.endAlert)
        self.tred.finished.connect(self.populateList)
        self.tred.start()

    def getChanPar(self,chan):
        for trans in  self.tred.satData.satParameters.keys():
            for channels in self.tred.satData.satParameters[trans]['tansponderChannels']:
                if chan in channels:
                    print 'channel %s found on %s Mhz'%(chan,trans)
                    #print '[%s] parameters : %s'%(chan,self.tred.satData.satParameters)
    def transmit(self):
        baza=sqlite3.connect(BAZA)
        c=baza.cursor()
        #c.execute('select channel,selected from parameters where degree="%s"'%self.sati)
        c.execute('select count(*) from parameters where degree="%s"'%self.sati)
        #for (chan,selekt) in c.fetchall():
        for i in range(c.fetchone()[0]):
            if self.model.item(i).checkState() and self.model.item(i).isEnabled():
                programname=self.model.item(i).text()
                self.model2.appendRow(QStandardItem('%s'%programname))
            # c.execute('update parameters set selected=1 where degree="%s" and channel="%s"'%(self.sati,str(self.model.item(i).text())))
            # baza.commit()
            #
                self.model.item(i).setEnabled(False)
                self.model2.item(self.id).setEditable(False)
                self.id+=1
                #c=baza.cursor()
                c.execute('update parameters set selected=1,transmited="%s" where degree="%s" and channel="%s"'%(self.id,self.sati,programname))
                #print('update parameters set selected=1,transmited="%s" where degree="%s" and channel="%s"'%(self.sati,self.id,programname))
            ###if self.model.item(chan).checkState() and self.model.item(chan).isEnabled():

                #print i
        baza.commit()
        baza.close()
    def moveUp(self):
        #self.select=
        curRow=self.dialog.chanList2.selectedIndexes()[0].row()

        if curRow > 0:
            prevRowTxt=self.model2.item(curRow-1).text()
            curRowTxt=self.model2.item(curRow).text()
            #print self.prevRow
            self.model2.item(curRow).setText(prevRowTxt)
            self.model2.item(curRow-1).setText(curRowTxt)
            print curRow
            curRow-=1

        self.dialog.chanList2.selectRow(curRow)

    def moveDown(self):
        curRow=self.dialog.chanList2.selectedIndexes()[0].row()

        if curRow < self.model2.rowCount()-1:
            nextRowTxt=self.model2.item(curRow+1).text()
            curRowTxt=self.model2.item(curRow).text()
            self.model2.item(curRow).setText(nextRowTxt)
            self.model2.item(curRow+1).setText(curRowTxt)
            print curRow
            curRow+=1

        self.dialog.chanList2.selectRow(curRow)


app=QApplication(sys.argv)
appSat=SatApp()
appSat.show()
app.exec_()
