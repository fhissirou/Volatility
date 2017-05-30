#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CarnetOrdres():
    def __init__(self):
        self.URLCARNETORDRES=""
        self.TORDERS_A=[]
        self.TACTIONS_A=[]
        self.TACHAT_A=[]
        self.TVENTE_V=[]
        self.TACTIONS_V=[]
        self.TORDERS_V=[]


    def getURLCARNETORDRES(self):
        return self.URLCARNETORDRES
    def getTORDERS_A(self):
        return self.TORDERS_A
    def getTACTIONS_A(self):
        return self.TACTIONS_A
    def getTACHAT_A(self):
        return self.TACHAT_A
    def getTVENTE_V(self):
        return self.TVENTE_V
    def getTACTIONS_V(self):
        return self.TACTIONS_V
    def getTORDERS_V(self):
        return self.TORDERS_V


    def setURLCARNETORDRES(self, val):
        self.URLCARNETORDRES= val
    def setTORDERS_A(self,val):
        self.TORDERS_A = val
    def setTACTIONS_A(self,val):
        self.TACTIONS_A= val
    def setTACHAT_A(self,val):
        self.TACHAT_A= val
    def setTVENTE_V(self,val):
        self.TVENTE_V= val
    def setTACTIONS_V(self,val):
        self.TACTIONS_V= val
    def setTORDERS_V(self,val):
        self.TORDERS_V= val

    def addTORDERS_A(self,val):
        self.TORDERS_A.append(val)
    def addTACTIONS_A(self,val):
        self.TACTIONS_A.append(val)
    def addTACHAT_A(self,val):
        self.TACHAT_A.append(val)
    def addTVENTE_V(self,val):
        self.TVENTE_V.append(val)
    def addTACTIONS_V(self,val):
        self.TACTIONS_V.append(val)
    def addTORDERS_V(self,val):
        self.TORDERS_V.append(val)

    def reset(self):
        self.TORDERS_A=[]
        self.TACTIONS_A=[]
        self.TACHAT_A=[]
        self.TVENTE_V=[]
        self.TACTIONS_V=[]
        self.TORDERS_V=[]

    #carnet d'ordre pour investir.com
    """def findCOInvestir(self):

        with urllib.request.urlopen(self.Url) as f:
            data = f.read().decode('utf-8')
            soup = bs4.BeautifulSoup(data, 'html.parser')
            tbody = soup.find('tbody')
            for tr in tbody.find_all('tr'):
                num_column= 0
                for td in tr.find_all('td'):
                    for span in td.find_all('span'):
                        val= span.get_text('', strip=True)
                        val= val.replace(',', '.')
                        val= val.replace('\xa0', '')
                        if (num_column == 0) and  (len(self.getTORDERS_A())< 10):
                            self.addTORDERS_A(int(val))

                        elif (num_column == 1) and (len(self.getTACTIONS_A())< 10):
                            self.addTACTIONS_A(int(val))

                        elif (num_column == 2) and (len(self.getTACHAT_A())< 10):
                            self.addTACHAT_A(float(val))

                        elif (num_column == 3) and  (len(self.getTVENTE_V())< 10):
                            self.addTVENTE_V(float(val))

                        elif (num_column == 4) and (len(self.getTACTIONS_V())< 10):
                            self.addTACTIONS_V(int(val))

                        elif (num_column == 5) and (len(self.getTORDERS_V())< 10):
                            self.addTORDERS_V(int(val))
                    num_column+=1"""
