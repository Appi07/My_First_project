#python program for loops 


#python for loop with range

for i in range(25,28):
    print(i)
    
#python for loop with list

mylist=["ravikumar","venkatesh","narasimha",1,2,3,5,1.5,2.6,3.6]
for i in mylist:
    print(i)
            
#python for loop with tuple
mylist1=("ravikumar","venk","venkatesh","narasimha",1.2,2.3,3.4,)
for i in mylist1:
    print(i)    
   
#python for loop with Dictionary
mylist2={'name':'ravikumar',"role":"software Enginner at TATA","ctc":"5lpa"}    
for i in mylist2:
    print(i,":",mylist2[i])
    
#python for loop with set
mylist3={"ravikumar","software Engineer","5lpa"}    
for i in mylist3:
    print(i)
    
#python for loop with string
mylist4="ravikumarhandral"
for i in mylist4:
    print(i)
    
    
#python for loop ---break
for i in range(30,70):
    if(i==58):
        break
    print(i)
    
#python for loop---continue
for i in range(30,70):
    if(i==47):
        continue
    print(i)    
 
#python for loop---nested for loop
for i in range(5):
    for j in range(4):
       print(j,  end=' ')  
    print()     
    
           