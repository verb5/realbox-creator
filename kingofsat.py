#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2,sqlite3
import math

### Extract all the transponders from the given satellite + channels ###

class Satellite:


    def __init__(self,sat=''):

        self.sat=sat
        self.satFreq=''
        self.satParameters={

            #'transponderParameters':[],
            #'tansponderChannels':[]

        }
        self.baza=sqlite3.connect('bazata')
        self.c=self.baza.cursor()
        self.c.execute('CREATE TABLE if not exists parameters(channel text,transponder text,fr int,lnb character,fec text,degree int,vpid int,apid int,sid int,nid int,tid int,selected tinyint,transmited int)')
        self.channels=[]

    def execQ(self,query):
        self.c.execute(query)

    def get(self,sate):
        #self.sat=sat
        if self.sat:
            self.page=urllib2.urlopen(self.sat)
            self.soup=BeautifulSoup(self.page,"html5lib")
            conta=self.soup.find_all('table',class_='frq')


        #c.execute('drop table if exists parameters')

        self.execQ('delete from parameters where degree="%s"'%sate)
        self.baza.commit()
        #baza.close()
        #baza=sqlite3.connect('bazata')
        #c=baza.cursor()
        #baza.close()
        for el in range(len(conta)):
            satelites=conta[el].find_all('td')[:-1]
            satFreq=int(math.floor(float(satelites[2].string)))
            for headerElement in satelites:
                self.satParameters.setdefault(satFreq,{}).setdefault('transponderParameters',[]).append(headerElement.get_text())

            prn=conta[el].next_sibling.next_sibling.find_all('a',class_='A3')
            try:

                for el1 in prn:
                    el=el1.parent.parent.find_all('td')
                    chanName=el[2].get_text().strip()
                    provider='satoperator'
                    transponder=satFreq
                    fr=self.satParameters[satFreq]['transponderParameters'][3]
                    lnb=self.satParameters[satFreq]['transponderParameters'][8][:5]
                    fec=self.satParameters[satFreq]['transponderParameters'][8][-3:]
                    deg=self.satParameters[satFreq]['transponderParameters'][0][:4]+self.satParameters[satFreq]['transponderParameters'][0][5:]
                    sid=el[7].get_text()
                    vpid=el[8].get_text()
                    apid=el[9].get_text()[:4]
                    nid=self.satParameters[satFreq]['transponderParameters'][10][4:]
                    tid=self.satParameters[satFreq]['transponderParameters'][11][4:]
                    #self.execQ('delete * from parameters where degree="%s"'%deg)
                    self.execQ('''insert into parameters(channel,transponder,fr,lnb,fec,degree,vpid,apid,sid,nid,tid) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'''%(chanName,transponder,fr,lnb,fec,deg,vpid,apid,sid,nid,tid))


            except Exception as e:
                print 'error line 60 [%s]'%e
        self.baza.commit()
        self.baza.close()
        #print self.satParameters
    def getParameters(self,transponder):
        for val in self.satParameters[transponder]['transponderParameters']:
            print val

        print 'number of channels on this transponder : [%s]'%len(self.satParameters[transponder]['tansponderChannels'])


        #baza.commit()
        #baza.close()
#proba=Satellite('http://en.kingofsat.net/pos-36E.php')
#proba.get()
