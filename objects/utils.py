'''
Created on 02/11/2013

@author: antonior
'''
import sqlite3
import sys
import xlwt


class sqlite():
    '''
    classdocs
    '''


    def __init__(self,dbname):
        '''
        Constructor
        '''
        self.name=dbname
    
    def connect(self):
        self.conn=sqlite3.connect(self.name)
        self.curs = self.conn.cursor()

    

    
    def tabtosqlite(self,name,_filename,types):
        fd=file(_filename)
        header=fd.readline()
        a_header=header.split('\t')
        cerate_fields=''
        if len(a_header)!=len(types):
            return "Please check types argument"
        else:
            for i,field in enumerate(a_header):
                cerate_fields=cerate_fields+" "+field+" "+types[i]+','
            cerate_fields=cerate_fields[:-1]
            self.curs.execute('''CREATE TABLE '''+name+''' ('''+cerate_fields+''')''') 
                
        for line in fd:
            insert_values=""
            a_line=line[:-1].split('\t')
            for i,value in enumerate(a_line):
                if types[i]=='TEXT':
                    insert_values=insert_values+"'"+value+"',"
                elif value=='-':
                    insert_values=insert_values+"'"+value+"',"
                else:
                    insert_values=insert_values+value+","
            insert_values=insert_values[:-1]
            self.curs.execute("INSERT INTO "+name+" VALUES ("+insert_values+")")
            self.conn.commit()
        fd.close()
        
    

class table():
    
        def __init__(self,_filename):
            '''
            Constructor
            '''
            self.ifile=_filename
        
        def tabletosqlite (self,prefix,tablename,listoftyoes):
            print "INFO: Exporting annotation to sqlite"
            
            a=sqlite(prefix)
            a.connect()
            a.tabtosqlite(tablename, self.ifile, listoftyoes)
            a.conn.close()
        
        def tabletoxls (self,prefix,tablename):
            
            print "INFO: Exporting annotation to xls"
            
            fd=file(self.ifile)
            headline=fd.readline().replace('\n','').split("\t")
            
            # Initialize the workbook and sheet
            wb = xlwt.Workbook()
            ws = wb.add_sheet(tablename)
    
            # Create header font
            header_style = xlwt.easyxf('font: bold on')
            #write header
            for c,colunm in enumerate(headline):
                ws.write(0,c,colunm,style=header_style)
            
            #write body
            for r,line in enumerate(fd):
                row=line.replace('\n','').split('\t')
                for c,cell in enumerate(row):
                    try:
                        ws.write(r+1,c,float(cell))
                    except:
                        ws.write(r+1,c,cell)
                         
            fd.close()
                
            wb.save(prefix+'.xls')
            
            
            
    