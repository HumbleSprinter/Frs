import threading 

from threading import*
import time

dicti={} 



def create(key,value,timeout=0):
    if key in dicti:
        print("error: this key is already exists") 
    else:
        if(key.isalpha()):
            if len(dicti)<(1024*1020*1024) and value<=(16*1024*1024):  
                if timeout==0:
                    nlist=[value,timeout]
                else:
                    nlist=[value,time.time()+timeout]
                if len(key)<=32: 
                    dicti[key]=nlist
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")


            
def read(key):
    if key not in dicti:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        bict=dicti[key]
        if bict[1]!=0:
            if time.time()<bict[1]: 
                stri=str(key)+":"+str(bict[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(bict[0])
            return stri



def delete(key):
    if key not in dicti:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        bict=dicti[key]
        if bict[1]!=0:
            if time.time()<bict[1]: 
                del dicti[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dicti[key]
            print("key is successfully deleted")





def modify(key,value):
    bict=dicti[key]
    if bict[1]!=0:
        if time.time()<bict[1]:
            if key not in dicti:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                nlist=[]
                nlist.append(value)
                nlist.append(bict[1])
                dicti[key]=nlist
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dicti:
            print("error: given key does not exist in database. Please enter a valid key") 
        else:
            nlist=[]
            nlist.append(value)
            nlist.append(bict[1])
            dicti[key]=nlist
