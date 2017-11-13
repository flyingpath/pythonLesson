import cx_Oracle
import json
import sys
from datetime import datetime


dsn = """(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521))(CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = XE)))"""

def query(sqlstring, pars, tojson=True):
    
    con = cx_Oracle.connect(user="tao", password="122122", dsn=dsn)
    c = con.cursor()
    
    c.execute(sqlstring, pars)
    
    colnames = [ i[0] for i in c.description ]
    
    data = []
    
    for items in c:
        lda = []
        for item in items:
            a=type(item)
            if type(item) is cx_Oracle.LOB:
                lstr = item.read() 
            elif type(item) is str:
                lstr = item
            elif type(item) is datetime:
                lstr = item.strftime("%Y%m%d")
            else:
                lstr = item
            lda.append(lstr)
        data.append(dict(zip(colnames, lda)))
    if tojson:
        return json.dumps(data)
    else:
        return data

def queryWrite(writeSQL, inputArray, clobIndex = []):
    con = cx_Oracle.connect(user="tao", password="122122", dsn=dsn)
    c = con.cursor()
    
    for idx in clobIndex:
        CONTENT = c.var(cx_Oracle.CLOB)
        inputArray[idx] = CONTENT.setvalue(0, inputArray[idx])
    
    try:
        c.execute(writeSQL, inputArray)
        result = c.execute("COMMIT")
        if c != None:
            c.close()
        if con != None:
            con.close()
        return {
            'status': True,
            'err': ''
        }
    except cx_Oracle.DatabaseError as e:
        if c != None:
            c.close()
        if con != None:
            con.close()
        return {
            'status': False,
            'err': e.args[0]
        }
    except Exception as e:
        if c != None:
            c.close()
        if con != None:
            con.close()        
        return {
            'status': False,
            'err': e
        }

def queryDatabase():
    return 'oracle_production'