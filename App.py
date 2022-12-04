class Covid19:
    avl=0
    used=0


class Vaccine(Covid19):
    Name=" "
    ID=000
    Address=" "
    dose=00

    def Storage(self,dos):
        self.avl=self.avl+int(dos)
        print("Stored",dos)
    def Avail(self):
        print("_______________________________")
        print("Available dos: ",self.avl)
        print("Distributed Doses: ",self.used)
        print("_______________________________\n\n")
    def DoseUsed(self):
        self.avl=self.avl-1
        self.used=self.used+1

    
    def setData(self,name,identity,located):
        self.Name=name
        self.ID=identity
        self.Address=located

        self.dose=self.dose+1
        print("Completed your today's Doses\n\n")
    def see(self):

        print("_______________________________")
        print("\n\nYour Information\n")
        print("Name       : ",self.Name)
        print("ID/DOB  No : ",self.ID)
        print("Doses No   : ",self.dose)

        self.dose=self.dose+1
        print("Completed your today's Doses")
        print("_______________________________\n\n\n")
        
    def userDetails(self):
        print("\n\n..............Your Data............\n")
        print("....................................")
        print(".                                  ")
        print(".                                  ")
        print(".                                  ")
        print(".             Covid-19             ")
        print(".  Provisional Vaccine Certificate ")
        print(".        Certificate No:",int(self.ID)+98769)
        print(". Name         : ",self.Name)
        print(". ID/DOB No    : ",self.ID )
        print(". Nationality  :  Bangladesh         ")
        print(". Vaccine Name :  AstraZeneca        ")
        print(". Total Doses  : ", self.dose)
        print(".                                  ")
        print(".                                  ")
        print(".                                  ")
        print("....................................")            
        print("                        ____________")
        print("                       |. Download .|")
        
def bio():
    print("\n\n\n\n")
    print("_____________________________________________________")
    print("\n             Bangladesh Covid 19 Services")
    print("......................................................")
    print("......................................................")
    print("......................................................")
    print("             Covid 19 Vaccine Registration")
    print("......................................................")

def adminAcc():
    print("\n\n   <==Admin Authority Panel==>")
    print("\n")
    aEmail=input("Enter Email Address: ")
    aUsername=input("Set Username       : ")
    aPassword=input("Set Password       : ")



#main program
bio()
adminAcc()
print("\n")
s=100
CD19=[]

for i in range(s):
    CD19.append(Vaccine())
    


    print("\n\nPress Any Key: ","Login=1","Service=2","History=3","Download=4","Logout=0",sep="\n")
    print("\n\n")
    pressMenu=int(input("Press: "))
    if pressMenu==1:
        CD19[i]=Vaccine()
        print("\n[+] [+] [+] Authority Login [+] [+] [+]\n")
        loginUsername=input("Enter Username          : ")
        loginPassword=input("Enter password          : ")
        Dist=input("Doses Quantity          : ")
        CD19[0].Storage(Dist)

        print("\n")
    elif pressMenu==2:
        CD19[i]=Vaccine()
        print("\n||......Services.....||\n")
        print("Are You Fist Dose Candidate ??  Press 1 or 2")
        check=int(input("=>:"))

        
        if check==1:
            print("\n\nYour Vaccine Code",i)
            name=input("Enter your Name            : ")   
            ID=input("Enter your Id              : ")       
            Address=input("Enter your Address         : ")
            CD19[i].setData(name,ID,Address)
            CD19[0].DoseUsed()
            

        else:
            SN=int(input("Enter Vaccine Code:         " ))
            CD19[SN].see()
            CD19[0].DoseUsed()

        

        
        
    elif pressMenu==3:
        CD19[i]=Vaccine()
        print("\n\nDetails of Doses")
        CD19[0].Avail()   
    elif pressMenu==4:
        CD19[i]=Vaccine()
        print("\n")
        checkID=int(input("Enter your ID: "))
        CD19[checkID].userDetails()
        print("\n")
    elif pressMenu==0:
        print("\n\nAny Query contact with vaccine team")
        print("Hotline:xxxxxx [Toll Free]")
        print("Powred by")
        print("Digital Bangladesh")
        print("DotTech")
        print("World Health Organizational Associate Limited (WHOAL)")
        print("IT limited")
        print("\nThank You.\n\n\n")
        break







