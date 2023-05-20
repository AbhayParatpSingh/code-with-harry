# this is a program for KBC game 
# questions list 
Question=["Amount of oxygen required to complete combition of 27g Al is :",
          "The largest no of molecules are in:",
          "No of atoms in 12g of 6C12 is:",
          "no of electrons in 1.8 ml of H2O is:(ans*10^23)",
          "Mass of one atom of H is:"]

#Now we have to make a list containg subelist in it for options of question
Option=[["1:24g","2:12g","3:20g","4:6g"],
        ["1:36gH2O","2:28gCO","3:46gC2H5OH","4:54gN2O5"],
        ["1:6","2:12","3:6.022*10^23","4:12*6.022*10^23"],
        ["1:6.02","2:3.011","3:0.6022","4:60.22"],
        ["1:1.66*10^-24g","2:10^23g","3:10^22g","4:10^24g"]]
#Now we have to create a list/tuple to make a list of answer
#i will chose tupple to make sure that answer cannot be edited
Answer=[1,1,3,1,1]
#now taking a variable to keep record of Cash prize won
Cash=0
count=0
txt="WELCOME TO KBC GAME"
txt1="correct answer"
txt2="Wrong answer"
x=txt.center(50," ")
print(x)
print()
#Now we are using loops to show question one by one and take Answer as input from user and match it with correct answer
for i in range(0,5):
    print(Question[i])
    print()
    for j in range(0,4):
        print(Option[i][j])
    print()
    useranswer=int(input("Enter the answer from the given option"))
    print()  
    if(useranswer==Answer[i]):
        y=txt1.center(50," ")
        print(y)
        print()
        Cash=Cash+1000
        count=count+1
    else:
        y=txt2.center(50," ")
        print(y)
        print()    

    if(i==4):
        print(" total correct answer given :",count)
        print("CASH PRIZE WON BY YOU IS:",Cash)
        txt3="THANKS FOR PLAYING"
        y=txt3.center(50," ")
        print(y)
        
    else:
        txt4="NEXT QUESTION ON YOUR SCREEN IS:"
        y=txt4.center(50," ")
        print(y)
        print()    
             
    