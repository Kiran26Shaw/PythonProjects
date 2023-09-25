import pickle   #module imported

from time import gmtime, strftime                     #module imported
n=strftime("%a, %d %b %Y", gmtime())                  #function for day and date
n=str(n)
today=n[5:]
print(n)
print("-"*57,"LIFE CARE HOSPITAL","-"*56)
print("-"*60,"WELCOME!!!!","-"*60)                    #cover page

print("1.LOGIN")                                      #menu to enter
print("2.EXIT")
ch=int(input("Enter your choice: "))
print()
if ch==1:
    print("*"*50,"LIFE CARE HOSPITAL WELCOMES YOU!!","*"*48)       #page that will appear after logging in
    print("                             !!MEDICINES CURE DISEASES, BUT ONLY DOCTORS CAN CURE PATIENTS!!")
    print("*"*133)
    while True:
        a=input("Please enter the appropriate username: ")      #username and password for security purpose
        if a=='Live your life to the fullest':
            b=input("Please enter password: ")
            if b=='1234@Lifecare':
                print()
                print("-"*50,"YOU HAVE SUCCESSFULLY ENTERED!","-"*51)
                print("-"*53,"How can we help you?","-"*58)
                break
            else:
                print("Wrong password, Try again!")
        else:
            print("You've entered a wrong username, Try again!")
                                                                
    print("1.ENTER AS A DOCTOR?")                               #options: doctor / patient
    print("2.ENTER AS A PATIENT?")
    print("3.EXIT")
    ch1=int(input("Enter your choice: "))
    print()
    
    #DOCTOR
    if ch1==1:
        while True:
            def menu1():                #function of display the menu
                print("*"*133)
                print("1.Register a new doctor")
                print("2.Update doctor details") 
                print("3.Delete doctor details")
                print("4.Display all doctor details")
                print("5.Search doctor")
                print("6.Exit")
                print("*"*133)
                ch2=int(input("Enter your choice: "))
                
                if ch2==1:              #func to register details of a doctor into the file
                    def writedoc():     
                        with open("DOCT",'ab+') as f: #will create file if not existing else reads the records from the existing file
                            if f.tell()>0:                        
                                f.seek(0)              
                                doc=pickle.load(f)
                            else:                     
                                doc=[]                
                            while True:              #loop for accepting records
                                d_id=int(input("Enter doctor id: "))
                                name=input("Enter name of the doctor: ")
                                gen=input("Enter gender: ")
                                age=int(input("Enter age of the doctor: "))
                                dep=input("Enter the alloted department: ")
                                while True:         
                                    phn=input("Enter a valid phone no.: ")
                                    if len(phn)!=10 or phn.isdigit==False:
                                        print("PLEASE ENTER A VALID PHONE NO.!") 
                                    else:
                                        break
                                d=[d_id,name,gen,age,dep,phn]  
                                doc.append(d)        #add records in file
                                c=input("Do you want to enter more?: ")
                                if c=='n' or c=='N':
                                    break
                            print("RECORD REGISTERED!")
                            with open("DOCT", 'wb') as f:  #will open the file for overwriting
                                pickle.dump(doc,f)
                    writedoc()   #function call
                        
                if ch2==4:
                    def displaydoc():   #func to diplay all the names and details of doctors      
                        try:
                            with open("DOCT", 'rb+') as f:
                                space="%20s %20s %20s %20s %20s %20s"  
                                print()
                                print("="*130)
                                print(space %("DOCTOR ID", "NAME", "GENDER", "AGE", "DEPARTMENT", "PHONE NO.")) 
                                print()
                                print("="*130)
                                doc=pickle.load(f)
                                for i in doc:                     
                                    for j in i:
                                        print("%20s" % j, end='') 
                                    print()
                                print("="*130)
                                print()
                        except EOFError:
                            print("NO RECORDS TO DISPLAY!")
                    displaydoc()   #function call

                if ch2==3:
                    def deletedoc():    #func to delete the record of the doctor from the file
                        try:
                            with open("DOCT", 'rb+') as f:
                                k=[]    #object which will contain all the other records except the one whcih is to be deleted
                                a=int(input("Enter the doctor id to be deleted: ")) 
                                doc=pickle.load(f)
                                found=0 
                                for i in doc:       #loop to traverse the file 
                                    if i[0]==a:
                                        found+=1    #required data found
                                    else:
                                        k.append(i) #all the records except the one which is to be deleted is appended in the object
                                if found==0:
                                    print("RECORD NOT FOUND!")  
                                else:
                                    f.seek(0)                   
                                    pickle.dump(k,f)            #file now contains the data except the deleted one
                                    print("RECORD DELETED!")    
                        except EOFError:
                            print("FILE HAS NO RECORDS!")
                                  
                    deletedoc()  #function call

                if ch2==2:
                    def updatedoc():    #func to update/rectify any detail of a doctor
                        with open("DOCT", 'rb+') as f:
                            s=pickle.load(f)
                            fnd=0
                            up=int(input("Enter the doctor id whose details are to be updated: "))
                            for i in s:             #traversing file
                                if i[0]==up:
                                    fnd=1           #data found
                                    print("Current name is: ", i[1])
                                    op=input("Do you want to update name(Y/N): ")      #if name is to be updated
                                    if op=='Y':
                                        i[1]=input("Enter new name: ")
                                       
                                    elif op=='N':
                                        print("Current gender is: ", i[2])
                                        op1=input("Do you want to update gender(Y/N): ")  #if gender is to be updated
                                        if op1=='Y':
                                            i[2]=input("Enter updated gender: ")
                                            
                                        elif op1=='N':
                                            print("Current age is: ", i[3])
                                            op2=input("Do you want to update age(Y/N): ")    #if age is to be updated
                                            if op2=='Y':
                                                i[3]=input("Enter new age: ")
                                        
                                            elif op2=='N':
                                                print("Current department is: ", i[4])
                                                op3=input("Do you want to change department(Y/N): ")   #if department is to be updated
                                                if op3=='Y':
                                                    i[4]=input("Enter new department: ")

                                                elif op3=='N':
                                                    print("Current phone no. is:", i[5])
                                                    op4=input("Do you want to update phone no.(Y/N): ") #if phn no. is to be updated
                                                    if op4=='Y':
                                                        while True:             
                                                            i[5]=input("Enter a valid phone no.: ")
                                                            if len(i[5])!=10 or i[5].isdigit==False:
                                                                print("PLEASE ENTER A VALID PHONE NO.!") 
                                                            else:
                                                                break        
                            if fnd==0: 
                                print("RECORD NOT FOUND!") 
                            else:
                                f.seek(0)
                                pickle.dump(s,f)        #updated data in the file
                                print("RECORD UPDATED!")   
                    updatedoc()   #function call

                if ch2==5:
                    def searchdoc():    #func to search details of a doctor
                        try:
                            with open("DOCT", 'rb') as f:
                                s=pickle.load(f)
                                fnd=0
                                search=int(input("Enter the doctor id whose record is to be searched: "))
                                for i in s:                #traversing file
                                    if i[0]==search:        
                                        print("RECORD FOUND!")
                                        print(i)
                                        fnd=1              #record found
                                if fnd==0:
                                    print("RECORD NOT FOUND!")   
                        except EOFError:
                            print("FILE HAS NO RECORDS!")
                    searchdoc()   #function call
                    
                if ch2==6:
                    def exitdoc():      #exit 
                        print("-"*100,"THANK YOU! HAVE A WONDERFUL DAY!")
                        exit()
                    exitdoc()   #function call
                    
            menu1()   #function call
            
    #PATIENT                
    elif ch1==2:
        while True:
            def menu2():                #operations you can perform if u enter as a patient                
                print("*"*133)
                print("1.Register a new patient")
                print("2.Update patient details") 
                print("3.Delete patient details")
                print("4.Display all patient details")
                print("5.Search patient")
                print("6.Set an appointment")
                print("7.Display all appointments")
                print("8.Delete an appointment")
                print("9.Search an appointment")
                print("10.Exit")
                print("*"*133)
                ch3=int(input("Enter your choice: "))
                
                if ch3==1:
                    def writepat():     #func to register details of a patient into the file
                        with open("PAT",'ab+') as f1:  #will create file if not existing else reads the records from the existing file

                            if f1.tell()>0:
                                f1.seek(0)
                                pat=pickle.load(f1)
                            else:
                                pat=[]
                            while True:                #loop for accepting records
                                p_id=int(input("Enter patient id: "))
                                name=input("Enter name of the patient: ")
                                gen=input("Enter gender: ")
                                age=int(input("Enter age of the patient: "))
                                dis=input("Enter his disease: ")
                                while True:            #loop to chk correctivity of no. of digits of phn no.
                                    phn=input("Enter a valid phone no.: ")
                                    if len(phn)!=10 or phn.isdigit==False:
                                        print("PLEASE ENTER A VALID PHONE NO.!")   #if incorrect no. is given
                                    else:
                                        break
                                p=[p_id, name,gen,age,dis,phn]
                                pat.append(p)          #add records in file
                                c=input("Do you want to enter more?: ")
                                if c=='n' or c=='N':
                                    break
                            print("RECORD REGISTERED!")
                            with open("PAT", 'wb') as f1:   #will open the file for overwriting
                                pickle.dump(pat,f1)
                                                          
                    writepat()  #function call
                        
                if ch3==4:
                    def displaypat():   #func to diplay names and details of all patients
                        try:
                            with open("PAT", 'rb+') as f1:
                                space="%20s %20s %20s %20s %20s %20s"   #this is used to provide some spacing in between the columns
                                print()
                                print("="*130)
                                print(space %("PATIENT ID", "NAME", "GENDER", "AGE", "DISEASE", "PHONE NO."))  #spacing
                                print()
                                print("="*130)
                                pat=pickle.load(f1)
                                for i in pat:                      #traversing the file
                                    for j in i:
                                        print("%20s" % j, end='')  #data displayed
                                    print()
                                print("="*130)
                                print()
                        except EOFError:
                            print("FILE HAS NO RECORDS TO DISPLAY!")
                    displaypat()   #function call

                if ch3==3:
                    def deletepat():    #func to delete the record of a patient
                        with open("PAT", 'rb+') as f1:
                            k1=[]       #object which will contain all the other records except the one which is to be deleted
                            a=int(input("Enter the patient id to be deleted: ")) 
                            pat=pickle.load(f1)
                            found=0
                            for i in pat:     #loop to traverse the file 
                                if i[0]==a:
                                    found+=1  #required data found
                                else:
                                    k1.append(i)   #all the records except the one which is to be deleted is appended in the object
                            if found==0:
                                print("RECORD NOT FOUND!")
                            else:
                                f1.seek(0)
                                pickle.dump(k1,f1) #file now contains the data except the deleted one 
                                print("RECORD DELETED!")
                    deletepat()  #function call

                if ch3==2:
                    def updatepat():    #func to update any detail of a patient
                        with open("PAT", 'rb+') as f1:
                            s=pickle.load(f1)
                            fnd=0
                            up=int(input("Enter the patient id whose details are to be updated: "))
                            for i in s:             #traversing file
                                if i[0]==up:
                                    fnd=1           #data found
                                    print("Current name is: ", i[1])
                                    op=input("Do you want to update name(Y/N): ")      #if name is to be updated
                                    if op=='Y':
                                        i[1]=input("Enter new name: ")
                                       
                                    elif op=='N':
                                        print("Current gender is: ", i[2])
                                        op1=input("Do you want to update gender(Y/N): ")  #if gender is to be updated
                                        if op1=='Y':
                                            i[2]=input("Enter updated gender: ")
                                            
                                        elif op1=='N':
                                            print("Current age is: ", i[3])
                                            op2=input("Do you want to update age(Y/N): ")    #if age is to be updated
                                            if op2=='Y':
                                                i[3]=input("Enter new age: ")
                                        
                                            elif op2=='N':
                                                print("Current disease is: ", i[4])
                                                op3=input("Do you want to replace disease(Y/N): ")   #if disease is to be updated
                                                if op3=='Y':
                                                    i[4]=input("Enter new department: ")

                                                elif op3=='N':
                                                    print("Current phone no. is:", i[5])
                                                    op4=input("Do you want to update phone no.(Y/N): ") #if phn no. is to be updated
                                                    if op4=='Y':
                                                        while True:             
                                                            i[5]=input("Enter a valid phone no.: ")
                                                            if len(i[5])!=10 or i[5].isdigit==False:
                                                                print("PLEASE ENTER A VALID PHONE NO.!") 
                                                            else:
                                                                break
                            if fnd==0:
                                print("RECORD NOT FOUND!")  
                            else:
                                f1.seek(0)
                                pickle.dump(s,f1)        #updated data in the file
                                print("RECORD UPDATED!")
                    updatepat()  #function call

                if ch3==5:
                    def searchpat():    #func to search details of a patient
                        try:
                            with open("PAT", 'rb') as f1:
                                s=pickle.load(f1)
                                fnd=0
                                search=int(input("Enter the patient id whose record is to be searched: ")) 
                                for i in s:       #traversing file
                                    if i[0]==search:
                                        print("RECORD FOUND!")
                                        print(i)
                                        fnd=1     #record found
                                if fnd==0:
                                    print("RECORD NOT FOUND!")   
                        except EOFError:
                            print("FILE HAS NO RECORDS!")
                    searchpat()   #function call

                if ch3==6:
                    def appoint():      #func to set an appointment
                        with open("APP",'ab+') as file:#will create file if not existing else reads the records from the existing file
                            if file.tell()>0:
                                file.seek(0)
                                app=pickle.load(file)
                            else:
                                app=[]
                            while True:                #loop for accepting records
                                sno=int(input("Enter the serial no. of the patient: "))
                                pname=input("Enter name of the patient: ")
                                dname=input("Enter name of the doctor to be appointed: ")
                                dis=input("Enter patient's disease: ")
                                a=[sno, pname, dname, dis]
                                app.append(a)          #add records in file
                                cho=input("D you want to add more appointments: ")
                                if cho=='n' or cho=='N':
                                    break
                            print("APPOINTMENT FIXED!")
                            with open("APP", 'wb') as file:  #opens the file for overwriting 
                                pickle.dump(app, file)
                    appoint()    #function call

                if ch3==7:
                    def displayapp():   #func to display all the appointments
                        try:
                            with open("APP", 'rb+') as file:
                                    space="%20s %20s %20s %20s"   #this is used to provide some spacing in between the columns
                                    print()
                                    print("="*130)
                                    print(space %("S.No.", "PATIENT NAME", "DOCTOR NAME", "DISEASE")) #spacing
                                    print()
                                    print("="*130)
                                    app=pickle.load(file)
                                    for i in app:                 #traversing the file
                                        for j in i:
                                            print("%20s" % j, end='') #data displayed
                                        print()
                                    print("="*130)
                                    print()
                        except EOFError:
                            print("FILE HAS NO RECORDS TO DISPLAY!")
                    displayapp()    #function call

                if ch3==8:
                    def deleteapp():
                        with open("APP", 'rb+') as file:
                            k2=[]        #object which will contain all the other records except the one whcih is to be deleted
                            a=int(input("Enter the serial no. to be deleted: "))  
                            app=pickle.load(file)
                            found=0
                            for i in app:       #loop to traverse the file 
                                if i[0]==a:
                                    found+=1    #required data found
                                else:
                                    k2.append(i)  #all the records except the one which is to be deleted is appended in the object
                            if found==0:
                                print("APPOINTMENT NOT FOUND!")
                            else:
                                file.seek(0)
                                pickle.dump(k2,file)  #file now contains the data except the deleted one 
                                print("APPOINTMENT DELETED!")
                    deleteapp()   #function call

                if ch3==9:
                    def searchapp():
                        try:
                            with open("APP", 'rb') as file:
                                s1=pickle.load(file)
                                fnd=0
                                srch=int(input("Enter the serial no. whose details is to be searched: "))
                                for i in s1:    #traversing file
                                    if i[0]==srch:
                                        print("RECORD FOUND!")
                                        print(i)
                                        fnd=1   #record found
                                if fnd==0:
                                    print("APPOINTMENT NOT FOUND!") 
                        except EOFError:
                            print("FILE HAS NO RECORDS!")
                    searchapp()  #function call

                if ch3==10:
                    def exitpat():      #func to exit 
                        print("-"*100,"THANK YOU! HAVE A WONDERFUL DAY!")
                        exit()
                    exitpat()  #function call
    
            menu2()  #function call
    elif ch1==3:
        print("-"*120,"THANK YOU!")     #exit
    else:
        print("PLEASE ENTER A VALID VALUE")  #this message will be displayed if option other than mentioned above is chosen        
elif ch==2:
    print("                                                              Thank You!")    #exit
    exit()
else:
    print("Wrong choice!")              #message displayed if wrong choice is made
    
#THE END!
    
