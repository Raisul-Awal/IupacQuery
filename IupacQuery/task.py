from email.quoprimime import body_encode
from client import *
import pandas as pd
from openpyxl.workbook import Workbook

if __name__ == "__main__":
    data = pd.read_csv("newfile.csv", delimiter= ',')
    Superclass = []
    Class = []
    Subclass = []
    cnt = 0;   
    for i in data['Compound ID']:
        cnt += 1
        r = iupac_query(i)
        if(r is not None and len(r['entities']) and r['entities'][0]['superclass'] is not None):  
            Superclass.append(r['entities'][0]['superclass']['name'])
        else: Superclass.append("NOT FOUND")
        if(r is not None and len(r['entities']) and r['entities'][0]['class'] is not None):  
            Class.append(r['entities'][0]['class']['name'])
        else: Class.append("NOT FOUND")
        if(r is not None and len(r['entities']) and r['entities'][0]['subclass'] is not None):  
            Subclass.append(r['entities'][0]['subclass']['name'])
        else: Subclass.append("NOT FOUND")
        print(cnt,i)


    data['SuperClass'] = Superclass
    data['Class'] = Class
    data['SubClass'] = Subclass
   
    data.to_excel('newfile.xlsx')