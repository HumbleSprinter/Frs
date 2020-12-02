 

import code as x 
#importing the main file("code" is the name of the file I have used) as a library 


x.create("Dinesh",25)
#to create a key with key_name,value given and with no time-to-live property


x.create("Amrita",70,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("Dinesh")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("Amrita")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("Dinesh",50)
#it returns an ERROR since the key_name already exists in the database



x.modify("Dinesh",55)
#it replaces the initial value of the respective key with new value 

 
x.delete("Dinesh")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on upto tn


