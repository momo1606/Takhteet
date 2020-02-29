import sqlite3
import math as m
import time
connection=sqlite3.connect('hifz.db')
cursor=connection.cursor()



def by_line(page,line,rowid,no_line,days):
    v=[]
    l=[no_line]*days
    try:
        for c in l:
            while(c>0):
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row3=cursor.fetchone()
                rowid=rowid+1
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row=cursor.fetchone()
                #print(row)
                if(row[2]==line):
                        continue
                else:
                    c=c-1
                    line=row[2]
            rowid+=1
            cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
            row1=cursor.fetchone()
            f=row1[2]
            while(row[2]==f):
                flag=1
                rowid+=1
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row1=cursor.fetchone()
                f=row1[2]
            if(flag==1):
                rowid-=1
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row1=cursor.fetchone()
            #print(row1)
            v.append([row1[1],row1[2]])
    except:
        #print(row3)
        v.append([604,15])
    finally:
        return v
def my_iter(x=.75,days=20):
    c=15*x
    if((x-m.floor(x))==.25):
        l=[m.ceil(c)]*3+[m.floor(c)]
    elif(x-m.floor(x)==.75):
        l=[m.floor(c)]*3+[m.ceil(c)]
    elif(x-m.floor(x)==.5):
        l=[m.floor(c),m.ceil(c)]
    elif(x-m.floor(x)==0):
        l=[c]
    l=list(map(int,(l*(int(days/len(l)))+l[:days%len(l)])))
    return(l)
def generate_1(page,line,rowid,sura,l):
    v=[]
    try:
        for c in l:
            while(c>0):
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row3=cursor.fetchone()
                rowid=rowid+1
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row=cursor.fetchone()
                #print(row)
                if(row[2]==line):
                    continue
                elif((row[1]==1 and row[2]==2) or (row[1]==187 and row[2]==2)):
                    c=c-2
                    sura=sura+1
                    line=row[2]
                elif(row[3]==sura+1):
                    if(row[2]==2):
                        c=c-2
                    elif(row[2]==3):
                        c=c-3
                    sura=sura+1
                    line=row[2]
                elif(row[2]==line+1 or (row[2]==1 and row[5]==1)):
                    c=c-1
                    line=row[2]
                if(c==0):
                    break
            rowid+=1
            cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
            row1=cursor.fetchone()
            f=row1[2]
            while(row[2]==f):
                flag=1
                rowid+=1
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row1=cursor.fetchone()
                f=row1[2]
            if(flag==1):
                rowid-=1
                cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE rowid=?',(rowid,))
                row1=cursor.fetchone()
            #print(row1)
            v.append([row1[3],row1[4]])
            
    except:
        #print(row3)
        v.append([114,6])
    finally:
        return v
def line_search2(ayat_no,surah_no,no_pages,days):
    cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE sura_number=? AND ayah_number=? AND position=?',(surah_no,ayat_no,1))
    row=cursor.fetchone()
    l=my_iter(no_pages,days)
    v=generate_1(row[1],row[2],row[0],row[3],l)
    return(v)
def line_search1(line_no,page_no,no_lines,days):
    cursor.execute('SELECT rowid,page_number,line_number,sura_number,ayah_number,position FROM glyphs WHERE page_number=? AND line_number=?',(page_no,line_no))
    row=cursor.fetchone()
    v=by_line(row[1],row[2],row[0],no_lines,days)
    return(v)
                      
'''if __name__ == '__main__':
    print(line_search1(3,603,3,25))'''
    

