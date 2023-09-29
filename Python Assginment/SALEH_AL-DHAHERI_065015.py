                                #============================================================================================
                                                
                                        ##########                      ##               ###########     #           #
                                        ##                   #          ##               #               #           #
                                        ##                 #   #        ##               #               #           #
                                        ########         #       #      ##               ###########     ########### #
                                              ##        # ######## #    ##               #               #           #
                                              ##      #              #  ##               #               #           #
                                        #######     #                 # ###############  ###########     #           #

                                    #                       ***** Frist Layer Functions Start ****
                                #============================================================================================

#############################################                                                          ################################################
                                                            #                                     #
                                                         #######                               #######
                                                        #########                             #########
                                                        #########                             #########                     
                                                         #######                               #######
                                                            #                                     #
                                            ####################### globle Functions Section ##################

###########################################                                                           ####################################################





#######################Design Fucntion ########################
#$$$$$$$ function use to print shape at the  start of the  progrram$$$$$$$$$$$$
def Ocean(): 
                  # OCEAN Sdn Bhd
    print("""
                                               #       #       #        #                                              #       #       #    
                                              ###     ###     ###      ###    ##    # # #       #          #      #   ###     ###     ### 
                                             #####   #####   #####    #####  #  #   #          # #        # #     #  #####   #####   ##### 
                                             #####   #####   #####    ##### #    #  #        #     #     #   #   #   #####   #####   #####  
                                              ###     ###     ###      ###   #  #   #       # ##### #   #     # #     ###     ###     ###      
                                               #       #       #        #      #    # # #  #         # #       #       #       #       #   """)
#######################Design Fucntion ########################
#$$$$$$$ function use to print  shape at the  end of the  program$$$$$$$$$$$$
def byeBye(): 
            
    print("""
                                            #####                              # # # #    # # # #    # # # #        # # #                            #####                
                                            #####   #####                      #   #  #  #  #        #   #  #   #   #                       #####    ##### 
                                            #####   #####                      # # #    #   # # #    # # #    #     # # #                   #####    #####
                                            #####   #####   #####    #####     #   #   #    #        #   #    #     #       #####   #####   #####    #####
                                            #####   #####   #####    #####     # # #   #    # # #  # # # #    #     # # #   #####   #####   #####    #####
    """)
    print("="*200)
#######################Design Fucntion ########################
#$$$$$$$ function use to print  shape at we moce  for  parent  fucntion to chiled function$$$$$$$$$$$$

def back():  
    print("""         
                                                                                      # # #
                                                                 ===================== # # # #
                                                                 ===================== # # # # # 
                                                                 ===================== #  # # #  
                                                                                      # # # #
        """)
#######################Design Fucntion ########################      
#$$$$$$$ function use to print  shape at we move  from child fucntion to parent function$$$$$$$$$$$$          
def forward(): 
    print ("""         
                                                                                      # # #
                                                                                    # # # # ====================
                                                                                  # # # # # ====================
                                                                                    # # # # ====================  
                                                                                      # # #  
            """)

#####Exit Function ####################
#$$$$$$$ function use  to move  out  of certian function to the  zone of antoher function passed as parameter$$$$$$$$$$$$
def Function_out(func): 
    print("If you Want To Leave insert [0], If you Want to continue The process press Enter")
    while True: 
        leave = input("Plese Enter The Value Here: ")
        print("")
        if leave in ["0", ""]: 
            if leave == "0":    
                back()
                return func()
            else: 
                return
        else: 
            print("Dear Only Zero and  Enter Are Allowed!!!: ")

#####Entero Message#####################
#$$$$$$$$$$$$$$$$function use  to print greeting message $$$$$$$$$$$$$$$$$$$$$
def startMaessage(section,name): 
    print("\n"+"=" * 200)
    print( "\n"+ " "*90+ " Hello And Welcome " + name.strip("\n") +" This", section,"Section")
    print("\n"+"=" * 200)

####READ FILes Function#################
#$$$$$$$$$$$$$$$ function use to read File and  returen list of the  file  comcomponent $$$$$$$$$$$$$$$$$$$$$$$$$$$
def read(file): 
    import os 
    path = os.path.abspath(file)
    readFile = open(path)
    list1 = readFile.readlines()
    readFile.close()
    return list1

########## Write Function #############
#$$$$$$$$$$$$$$$ function use to write File and  returen list of the  file  comcomponent $$$$$$$$$$$$$$$$$$$$$$$$$$$
def write(file,list): 
    import os 
    path = os.path.abspath(file)
    write = open(path, "w")
    write.writelines(list)
    write.close()

########## Search Function #############
#$$$$$$$$$$$$$$$$$$$$$$$$$function use  to sreach by  the  name  of user or medicin or and  thing accept name and file name $$$$$$$$$$$$$$$$$$
def search(name1,file):
    print("please Enter The Name Of "+ name1 + " Your Looking For")
    name = input("Enter The Value  Here Please ")+"\n"
    list = read(file)
    while True: 
        if (name in list) and (list[list.index(name)-1] == "start\n"): 
                counter = list.index(name)
                return [name,counter]
        else: 
            print()
            print("Sorry Dear!!! The "+name1+" You are Looking For Is Not Is Not Existed")
            print()
            print("Dear If you Want TO Re-Enter The name press Enter IF You Want To Stop Enter [0]")
            while True:
                exit = input("")
                if exit in ["0", ""]: 
                    if exit == "0":    
                        return [False,False]
                    else: 
                        break
                else: 
                    print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter")    
            print("Enetr The name Again Please!!") 
            name = input("Enter The Value  Here Please: ")+"\n"

####################Login Function ########################
#$$$$$$$$$$$$$$$$$$$$$$$$
def logIn(log):
        #log in code  for  admin 
    startMaessage("Login","Login please")
    if log == 1: 
        list = read("admin.txt")
        print("Please Enter your Name And You Password")
        while True: 
            adminName = input("Admin Name: ")+"\n"
            adminPassword = input("Admin password: ")+"\n"
            if adminName != "start" and adminName != "end" and adminName in list: 
                if adminPassword != "start" and adminPassword != "end" and adminPassword in list:      
                    print("="*200)     
                    forward()
                    print("="*200+"\n")
                    print(" "*95+ " Hello And Welcome "+adminName)
                    return adminName
            print("incorrect Password or user name Enter your Password And User Name  Again\n")
            print("="*200)
            Function_out(main)
    elif log == 2: 
        userList = read("userData.txt")
        print("Please Enter your Name And You Password")
        while True: 
            userName = input("Enter User Name: ")+"\n"
            userPassword = input("Enter your Password: ")+"\n"
            if userName != "start" and userName != "end" and userName in userList: 
                    if userPassword != "start" and userPassword != "end" and userPassword in userList:            
                        print("="*200)
                        forward()
                        print("="*200+"\n")
                        print(" "*95+ " Hello And Welcome "+userName)
                        return userName
            print("incorrect Password or user name Enter your Password And User Name  Again\n")
            print("="*200)
            Function_out(main)

########## View Specific Function #############
def veiwSpecific(list1,list2,name,number): 
    for i in range(len(list1)): 
        if list1[i] == name: 
            print("====================================")
            j = i 
            counter = 0
            while j < (i + number): 
                print(list2[counter] + ": "+list1[j])
                counter = counter +1
                j = j + 1
            print("====================================")


########## View ALL Function #############
def viewAll(file,list): 
    list1 = read(file)
    for i in list1:
        if i != "start\n" and  i != "end\n":   
              print(list[counter] + ": " + i)
        else: 
            # counter used to display the informatin like name: , Exp: , along with the  data.
            counter = -1
            if i == "start\n": 
                print("="*50)     
        counter = counter +1 
    print("="*50)   



                                #============================================================================================
                                                
                                        ##########                       ##               ###########     #           #
                                        ##                   #           ##               #               #           #
                                        ##                 #   #         ##               #               #           #
                                        ########         #       #       ##               ###########     ########### #
                                              ##        # ######## #     ##               #               #           #
                                              ##      #              #   ##               #               #           #
                                        #######     #                 #  ###############  ###########     #           #

                                    #                       ***** Second Layer Functions Start ****
                                #============================================================================================

######### ###################################                                                          ################################################
                                                            #                                     #
                                                         #######                               #######
                                                        #########                             #########
                                                        #########                             #########                     
                                                         #######                               #######
                                                            #                                     #
                                            ####################### Admin Functions Section ##################

###########################################                                                           ####################################################

                                                               
                                                          ##                            ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                    ########### Uplode Medicin  Function #############


def uploadMedicin(adminName):
    startMaessage("Medicin Uplode", adminName) 
    name = input("enter the Medicin name You Need Want To Uplode: ")+"\n"
    expired = input("enter the expired date in DD/MM/YY format : ") +"\n"
    price = input("enter the price: ")
    while True: 
        if price.isnumeric(): 
                price = "RM"+price+"\n"
                break
        print("excuse Me Dear Only Numrical Value Available")    
        price = input("Please Enter The Price Again: ")

    specification = input("enter the  specification: ")+"\n"
    MedicinList = ["start\n",name,expired,price,specification,"end\n"]
    Function_out(main)
    appendFile = open("Meadicin-Data.txt","a")
    appendFile.writelines(MedicinList)
    appendFile.close()
    print("="*200)
    print("Medicin Data has uploded successfully to the  system ^_^\n")
    print("Medicin Name: " + name)
    print("Medicin Price: " + price)
    print("Medicin Expired Date: " + expired)
    print("Medicin specification : " + specification)
    print("="*200)
    print("If You Would Like To View , modify , Delete Medicin or specific Medicin Detail Press Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To View Medicin Detail In System ")
        print("[2]- Enter Two To Update/Modify Medicin Information")
        print("[3]- Enter Three To Delete Medicin Information")
        print("[4]- Enter Four To specific Medicine Detail Information")
        print("[5]- Enter Five To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4","5"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 5\n") 
        if choice =="1": 
            print("="*200)
            forward()
            AllMedicins(adminName)
        elif choice == "2": 
            print("="*200)
            forward()
            updateModify(adminName)
        elif choice == "3": 
            print("="*200)
            forward()
            deleteInfo(adminName)
        elif choice == "4": 
            print("="*200)
            forward()
            specificMdDetial(adminName)
        elif choice == "4": 
            print("="*200)
            back()
            main()
    Function_out(main) 
    uploadMedicin(adminName)
                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                 ############ View All Medicins Function #############

def AllMedicins(adminName): 
    startMaessage("Medicin View", adminName)
    viewAll("Meadicin-Data.txt",["name","Exp","Price","specification"])
    print("If You Would Like To Uplode Or modify or Delete Medicin Press Enter IF no Press Zero")
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One TO Uplode New Medicin Detail In System ")
        print("[2]- Enter Two To Update/Modify Medicin Information")
        print("[3]- Enter Three To Delete Medicin Information")
        print("[4]- Enter Four To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 4\n") 
        if choice =="1": 
            print("="*200)
            forward()
            uploadMedicin(adminName)
        elif choice == "2": 
            print("="*200)
            forward()
            updateModify(adminName)
        elif choice == "3": 
            print("="*200)
            forward()
            deleteInfo(adminName)
        elif choice == "4": 
            print("="*200)
            back()
            main()
    Function_out(main)
    AllMedicins(adminName)


                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                   ############ Updata / modify  Function #############




def updateModify(adminName):
    startMaessage("Updata/Modify", adminName) 
    listmid = read("Meadicin-Data.txt")
    mdName = search("Meadicin","Meadicin-Data.txt")[1]
    if mdName == False: 
        print("="*200)
        back()
        print("="*200) 
        main()
    print("="*200)
    print("[1]- Enter One To modify the name")
    print("[2]- Enter Two To modify the Expired Data")
    print("[3]- Enter Three To modify the Expired Data")
    print("[4]- Enter Four To Modify The Specification")
    print("[5]- Enter FIve To Quit")
    print("="*200)
    while True:
        print("Enter The Value Here Please: ")
        choose = input("")
        if choose in ["1","2","3","4","5"]: 
            break
        print("")
        print("Please re-Enter your option, your option should be From 1 to 5\n")  
    
    if choose == "1": 
        data = input("enter thw  new name for the medical: ")+"\n"
        listmid[int(mdName)] = data
        write("Meadicin-Data.txt", listmid)
    elif choose == "2": 
        mdName = mdName + 1
        data = input("enter thw  new name for the Expired data Y/M/D: ")+"\n"
        listmid[int(mdName)] = data
        write("Meadicin-Data.txt", listmid)
    elif choose == "3": 
        mdName = mdName + 2
        data = input("enter thw  new name for the Expired data price: ")+"\n"
        listmid[int(mdName)] = data
        write("Meadicin-Data.txt", listmid)
    elif choose == "4": 
        mdName = mdName + 3
        data = input("enter the new specification: ")+"\n"
        listmid[int(mdName)] = data
        write("Meadicin-Data.txt", listmid) 
    elif choose == "5": 
        print("the  changing process has been stoped")
        updateModify(adminName)
    print("If You Would Like To Uplode , View , Delete Medicin Press , specific Medicin Detail  Enter IF no Press Zero")
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
           
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Upload New Medicin In System ")
        print("[2]- Enter Two To Veiw Medicin Information")
        print("[3]- Enter Three To Delete Medicin Information")
        print("[4]- Enter Four To specific Medicin Detail")
        print("[5]- Enter Five To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4","5"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 5\n") 
        if choice =="1": 
            print("="*200)
            forward()
            uploadMedicin(adminName)
        elif choice == "2": 
            print("="*200)
            forward()
            AllMedicins(adminName)
        elif choice == "3": 
            print("="*200)
            forward()
            deleteInfo(adminName)
        elif choice == "4": 
            print("="*200)
            forward()
            specificMdDetial(adminName)
        elif choice == "5": 
            back()
            main()              
    Function_out(main)
    updateModify(adminName)

                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  Delete Function #############
def deleteInfo(adminName): 
    startMaessage("Delete", adminName)
    listmid = read("Meadicin-Data.txt")
    mdName = search("Meadicin","Meadicin-Data.txt")[1]
    if mdName == False: 
        print("="*200)
        back()
        print("="*200) 
        main()
    print("="*200)
    print("[1]- Enter One If You Want To Delete A Specific Data")
    print("[2]- Enter Two If You Want To Delete The  Whole Item")
    print("[3]- Enter Three To Quti")
    print("="*200)
    print("Enter The Value Here Please: ")
    while True:
        deleteType = input("")
        if deleteType in ["1","2","3"]: 
            break
        print("Please re-Enter your option, your option should be From 1 to 3\n") 
    if  deleteType == "1": 
        print("="*200)
        print("[1]- Enter One If You Want To Delete The name")
        print("[2]- Enter Two If You Want To Delet The Expired Data")
        print("[3]- Enter Three If You Want TO Delete The Price")
        print("[4]- Enter Four If You Want Two Delete Specification")
        print("="*200)
        while True:
            choose = input("")
            if choose in ["1","2","3","4"]: 
                break
            print("Please re-Enter your option, your option should be From 1 to 4\n") 
        if choose == "1": 
            print("press Enter To Varfiy Data Delet And Enetr Zero If You Want TO Stop The Process")
            while True:    
                delete = input("Please Enter The  Value  Here: ")
                if delete in ["0",""]: 
                    if delete == "0":
                        print("*"*45 + "The Process is Stoped successful"+ 45*"*" + "\n")
                        break
                    else: 
                        listmid[int(mdName)] = "\n"
                        write("Meadicin-Data.txt", listmid)
                        print("delete process have  done successfully")
                        break
                else: 
                    print()
                    print("Dear!!! Only Zero And Enter Are Allowed")    
                
        elif choose == "2": 
            mdName = mdName + 1
            print("press Enter TO Varfiy deletion process And Enetr Zero If You Want TO Stop The Process")
            while True:    
                delete = input("")
                if delete in ["0",""]: 
                    if delete == "0":
                        print("*"*45 + "The Process is Stoped successful"+ 45*"*" + "\n")
                        break
                    else: 
                        listmid[int(mdName)] = "\n"
                        write("Meadicin-Data.txt", listmid)
                        print("delete process have  done successfully")
                        break
                else: 
                    print()
                    print("Dear!!! Only Zero And Enter Are Allowed")   

        elif choose == "3": 
        
            mdName = mdName + 2
            print("press Enter TO Varfiy Data deletion process And Enetr Zero If You Want TO Stop The Process")
            while True:    
                delete = input("")
                if delete in ["0",""]: 
                    if delete == "0":
                        print("*"*45 + "The Process is Stoped successful"+ 45*"*" + "\n")
                        break
                    else: 
                        listmid[int(mdName)] = "\n"
                        write("Meadicin-Data.txt", listmid)
                        print("delete process have  done successfully")
                        break
                else: 
                    print()
                    print("Dear!!! Only Zero And Enter Are Allowed")   

        elif choose == "4": 
            mdName = mdName + 3
            print("press Enter TO Varfiy deletion process And Enetr Zero If You Want TO Stop The Process")
            while True:    
                delete = input("")
                if delete in ["0",""]: 
                    if delete == "0":
                        print("*"*45 + "The Process is Stoped successful"+ 45*"*" + "\n")
                        break
                    else: 
                        listmid[int(mdName)] = "\n"
                        write("Meadicin-Data.txt", listmid)
                        print("delete process have  done successfully")
                        break
                else: 
                    print()
                    print("Dear!!! Only Zero And Enter Are Allowed")   
        else: 
            print("the  changing process has been stoped")
    elif deleteType == "2": 
        print("press Enter TO Varfiy deletion process Data Delet And Enetr Zero If You Want TO Stop The Process")
        while True:    
                delete = input("")
                if delete in ["0",""]: 
                    if delete == "0":
                        print("*"*45 + "The Process is Stoped successful"+ 45*"*" + "\n")
                        break
                    else: 
                        listmid[int(mdName-1)] = ""
                        listmid[int(mdName)] = ""
                        listmid[int(mdName+1)] =""
                        listmid[int(mdName+2)] = ""
                        listmid[int(mdName+3)] = ""
                        listmid[int(mdName+4)] = ""
                        write("Meadicin-Data.txt", listmid)
                        print("delete process have  done successful")
                        break
                else: 
                    print()
                    print("Dear!!! Only Zero And Enter Are Allowed")   
    elif deleteType == "3":  
        deleteInfo(adminName)
    print("If You Would Like To Uplode , View All medicin , modify/Update Medicin  , Veiw specific Medicin Detail Press Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Upload New Medicin In System ")
        print("[2]- Enter Two To Veiw Medicin Information")
        print("[3]- Enter Three To Modify Medicin Information")
        print("[4]- Enter Four To specific Medicin Detail Information")
        print("[5]- Enter Five To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4","5"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 5\n") 
        if choice =="1": 
            print("="*200)
            forward()
            uploadMedicin(adminName)
        elif choice == "2": 
            print("="*200)
            forward()
            AllMedicins(adminName)
        elif choice == "3": 
            forward()
            updateModify(adminName)
        elif choice == "4": 
            print("="*200)
            forward()
            specificMdDetial(adminName)        
        elif choice == "5": 
            print("="*200)
            back()
            main()                
    Function_out(main)
    deleteInfo(adminName)

                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############ View All Medicins Function #############



def specificMdDetial(adminName): 
    startMaessage("specific Detial", adminName)
    list1 = read("Meadicin-Data.txt")
    mdName = search("Meadicin","Meadicin-Data.txt" )[0]
    veiwSpecific(list1, ["name","Exp","Price","specification"], mdName, 4)
    print("If You Would Like To  modify/Update or Delete Medicin Press Enter  , IF no Press [0] Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Delete Information")
        print("[2]- Enter Two To Modify Medicin Information")
        print("[3]- Enter Three To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4"]: 
                    break
                print("Please re-Enter your option, your option should be From 1 to 3\n") 
        if choice =="1": 
            print("="*200)
            forward()
            deleteInfo(adminName)
        elif choice == "2": 
            forward()
            print("="*200)
            updateModify(adminName)
        elif choice == "3": 
            print("="*200)
            back()
            main()
    Function_out(main)
    specificMdDetial(adminName)


                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############ View All  Orders  Function #############
def viewAllOrders(adminName): 
    startMaessage("View Order", adminName) 
    viewAll("order-data.txt",["name","Exp","Price","specification"])
    print("If You Would Like To View Specific order  Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
            
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To View Specific order In System ")
        print("[2]- Enter Two To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should 1 or 2\n") 
        if choice =="1": 
            print("="*200)
            forward()
            specificOrderDetial(adminName)
        elif choice == "2": 
            print("="*200)
            back()
            main()
    Function_out(main)
    viewAllOrders(adminName)

                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############ View Oerders Function #############
def specificOrderDetial(adminName): 
    startMaessage("Search Order of the specific customer", adminName)
    list1 = read("order-data.txt")
    orderName = search("uesr", "order-data.txt")[0]
    veiwSpecific(list1, ["name","madican-name","Quantity", "Price"], orderName, 4)
    print("If You Would Like To View All  orders  Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
            
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To View Specific order In System ")
        print("[2]- Enter Two To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be 1 or 2\n") 
        if choice =="1": 
            print("="*200)
            forward()
            viewAllOrders(adminName)
        elif choice == "2": 
            print("="*200)
            back()
            main()
    Function_out(main)
    specificMdDetial(adminName)


#############################################                                                          ################################################
                                                            #                                     #
                                                         #######                               #######
                                                        #########                             #########
                                                        #########                             #########                     
                                                         #######                               #######
                                                            #                                     #
                                            ####################### New User Functions Section ##################

###########################################                                                           ####################################################



                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  New  User Regist Function #############


def userRegist(): 
    startMaessage(" New User Registration","New User")
    userList =  read("userData.txt")
    name = input("Enter Your Name Please: ")+"\n"
    password = input("Enter Your Password Please most Be  more inclued more  then six char: ")+"\n"
    while True: 
        if name in userList or len(password) < 7: 
            print("your user name  may exist or your password is shoter than 6 char")
            name = input("Enter Your User Name Again: ")+"\n"
            password = input("Enter Your Password Again: ")+"\n"
        else: 
            print("acceptable User Name  And Password")
            print("PLease Enter The  other Informations\n")
            break

    phoneNumber = input("Enter Your Phone Number Please: ")+"\n"
    gander = input("Enter Your Gander: ")+"\n"

    print("="*200)
    print("congratulations !!! "+ name + "The Registration Process Have Done successfully \n")
    print("Name:", name)
    print("password:", password)
    print("Phone Number:", phoneNumber)
    print("Gender:", gander)
    print("="*200)
    userDateList = ["start\n",name,password,phoneNumber,gander,"end\n"]
    appendFile = open("userData.txt","a")
    appendFile.writelines(userDateList)
    appendFile.close()
    print("If You Would Like If You Want To Login Into Your Account Or View  The  exexisted midicen Press Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
            
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Login To your  Account")
        print("[2]- Enter Two To View The Existed Medicin")
        print("[3]- Enter Three  To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4","5"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 3\n") 
        if choice =="1": 
            print("="*200)
            forward()
            registedUser()
        elif choice == "2": 
            print("="*200)
            forward()
            allMedicinsNewUser()
        elif choice == "3": 
            print("="*200)
            back()
            main()
    Function_out(main) 
    userRegist()

                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  View all medicins Function #############
   


def allMedicinsNewUser(): 
    startMaessage("View All Medicin","New User")
    viewAll("Meadicin-Data.txt",["name","Exp","Price","specification"]) 
    print("If You Would Like If You Want To Login Into Your Account Or View  The  exexisted midicen Press Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 

    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Login If you have Account Already")
        print("[2]- Enter Two To Regist an Account")
        print("[3]- Enter Three  To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4","5"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 3\n") 
        if choice =="1": 
            print("="*200)
            forward()
            registedUser()
        elif choice == "2": 
            print("="*200)
            forward()
            userRegist()
        elif choice == "3": 
            print("="*200)
            back()
            main()
    Function_out(main) 
    allMedicinsNewUser()




#############################################                                                          ################################################
                                                            #                                     #
                                                         #######                               #######
                                                        #########                             #########
                                                        #########                             #########                     
                                                         #######                               #######
                                                            #                                     #
                                           ################### Regested User Functions Section ##################

###########################################                                                           ####################################################

                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############ Veiw All Medicines Function #############
                                        
def allMedicinsRegistedUser(userName): 
    startMaessage("Medicin View", userName)
    viewAll("Meadicin-Data.txt",["name","Exp","Price","specification"])
    print("If You Would Like To Buy , Veiw Orders or View Personl Information Enter IF no Press Zero")

    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
           
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Order a Medicin")
        print("[2]- Enter Two To Veiw Orders")
        print("[3]- Enter Three To View Personl Information")
        print("[4]- Enter Four To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 4\n") 
        if choice =="1": 
            print("="*200)
            forward()
            orderPay(userName)
        elif choice == "2": 
            print("="*200)
            forward()
            viewPersonalOrders(userName)
        elif choice == "3": 
            print("="*200)
            forward()
            viewPersonalInforamtion(userName)
        elif choice == "4": 
            print("="*200)
            back()
            main()   
    Function_out(main)
    allMedicinsRegistedUser(userName)

                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  order and pay Function #############
                                                

def orderPay(userName): 
    startMaessage("Order and  payment", userName)
    meadicinList = read("Meadicin-Data.txt")
    list1 = ["name","madican-name","Quantity", "Price"]
    viewAll("Meadicin-Data.txt", ["name","Exp","Price","specification"])
    #check and  enter the  name of the  medicon want  to by
    mdIndex = search("Medicin","Meadicin-Data.txt")[1]
        # enter the  quntity
    while True:   
        quntity = input("enter the quantity you need to buy: ")
        if quntity.isnumeric(): 
            quntity = int(quntity)
            break
        else: 
            print("Only Numerical Value Allowed!!!")

    price = int(meadicinList[mdIndex+2].strip("RM"))
    total = price * quntity
    print("The Total Payment Is: RM", total)
    pay = int(input("enter the payment: "))
    while pay < total: 
            exit = input("The Payment Smaller Then The Total Type 0 If You Want To Quit And Press Enetr To continue: ")
            if exit in  ["0",""]:
                if exit == "0": 
                    registedUser()
                elif exit == "": 
                     pay = int(input("the  price you have enterd is less than total reenter the payment: "))
            else: 
                 print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter")      
    
    mdName = meadicinList[mdIndex]
    payment = ("price:"+ str(price) +"MR "+ "T:" + str(total) + "MR")+"\n"
    userName =  userName
    orderdata = ["start\n", userName,mdName,str(quntity)+"\n",payment,"end\n"]
    appendFile = open("order-data.txt","a")
    appendFile.writelines(orderdata)
    appendFile.close()
    print("="*200) 
    print(" "*75+ "congratulations "+ userName.strip("\n") + " The  Payment process Done successfully\n")
    print("Name:",userName)
    print("Medicin:", mdName)
    print("Quntity:", "X"+str(quntity))
    print()
    print("Price:", payment)
    if(pay > total): 
         print("you have a "+ str(pay - total)+ "RM remain") 
    print("="*200)
    print("If You Would Like To  Medicin View, Veiw Orders or View Personl Information Enter IF no Press Zero")
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
            
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To View  Medicins information")
        print("[2]- Enter Two To Veiw Orders")
        print("[3]- Enter Three To View  Information Personl")
        print("[4]- Enter Four To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 4\n") 
        if choice =="1": 
            print("="*200)
            forward()
            print("="*200)
            allMedicinsRegistedUser(userName)
        elif choice == "2": 
            print("="*200)
            forward()
            print("="*200)
            viewPersonalOrders(userName)
        elif choice == "3": 
            print("="*200)
            forward()
            print("="*200)
            viewPersonalInforamtion(userName)
        elif choice == "4": 
            print("="*200)
            back()
            main()
    Function_out(main)
    orderPay(userName)

                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  View personal orders Function #############


def viewPersonalOrders(userName): 
    startMaessage("Personal Order", userName)
    list1 = read("order-data.txt")
    veiwSpecific(list1,["name","Medicin","Quntity", "Price-"],userName,4)
    print("If You Would Like To View Medicin, Veiw Orders or View Personl Information Enter IF no Press Zero")
    
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
           
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Order a Medicin")
        print("[2]- Enter Two To Personl Information")
        print("[3]- Enter Three To View  Medicins information")
        print("[4]- Enter Four To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 4\n") 
        if choice =="1": 
            print("="*200)
            forward()
            orderPay(userName)
        elif choice == "2": 
            print("="*200)
            forward()
            viewPersonalInforamtion(userName)
        elif choice == "3": 
            print("="*200)
            forward()
            allMedicinsRegistedUser(userName)
        elif choice == "4": 
            print("="*200)
            back()
            main()    
    Function_out(main)
    viewPersonalOrders(userName)

                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  View Personal Info Function #############


def viewPersonalInforamtion(userName): 
    startMaessage("Personal Personal", userName)
    list1 = read("userData.txt")
    veiwSpecific(list1,["name","password","phone", "gander"],userName,4)
    print("If You Would Like To  Medicin View, Veiw Orders or View Personl Information Enter IF no Press Zero")
   
    while True: 
        advancOptions= input("Enter Your Value  Here Please: ")
        if advancOptions in ["" , "0"]: 
            break
        else: 
            print("Only Zero and Enter Allowed Please Dear Press The 0 or Enter") 
    if advancOptions == "": 
        print("="*200) 
        print("[1]- Enter One To Order a Medicin")
        print("[2]- Enter Two To Veiw Orders")
        print("[3]- Enter Three To View  Medicins information")
        print("[4]- Enter Four To Exit")
        print("="*200)
        while True:
                choice = input("Enetr The Option Here Please: ")
                if choice in ["1","2","3","4"]: 
                    break
                print("")
                print("Please re-Enter your option, your option should be From 1 to 4\n") 
        if choice =="1": 
            print("="*200)
            forward()
            orderPay(userName)
        elif choice == "2": 
            print("="*200)
            forward()
            viewPersonalOrders(userName)
        elif choice == "3": 
            print("="*200)
            forward()
            allMedicinsRegistedUser(userName)
        elif choice == "4": 
            print("="*200)
            back()
            main()
    Function_out(main)
    viewPersonalInforamtion(userName)
                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  New  User Regist Function #############


                                #============================================================================================
                                                
                                        ##########                      ##               ###########     #           #
                                        ##                   #          ##               #               #           #
                                        ##                 #   #        ##               #               #           #
                                        ########         #       #      ##               ###########     ########### #
                                              ##        # ######## #    ##               #               #           #
                                              ##      #              #  ##               #               #           #
                                        #######     #                 # ###############  ###########     #           #

                                    #                       ***** Third Layer Functions Start ****
                                #============================================================================================

#############################################                                                          ################################################
                                                            #                                     #
                                                         #######                               #######
                                                        #########                             #########
                                                        #########                             #########                     
                                                         #######                               #######
                                                            #                                     #
                                            ####################### Section Major Functions Section ##################

###########################################                                                           ####################################################


                                                          ##                             ##                                  
                                                         #####                          ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  ADMIN ***** Function #############
def admin(): 
    log = 1
    adminName = logIn(log)
    if adminName : 
            startMaessage("Admin",adminName)
            print("="*200)
            print("[1]- Enter TO Upload Medicin Detail In System ")
            print("[2]- Enter Two To View All Uploaded Medicins")
            print("[3]- Enter Three To Update/Modify Medicin Information")
            print("[4]- Enter Four To Delete Medicin Information")
            print("[5]- Enter Five To Search For specific Medicin Detail")
            print("[6]- Enter Six To To View All Orders")
            print("[7]- Enter Seven To Search Order OF Specific customer")
            print("[8]- Enter Eight to Exit \n")
            print("="*200)
            print("Enter The Value Here Please: ")
            while  True: 
                proceses   = input(" ")
                if proceses in ["1","2","3","4","5","6","7","8"]: 
                    break
                else: 
                    print("")
                    print("Please re-Enter your option, your option should be From 1 to 8\n")    
            if proceses == "1":
                print("="*200)
                forward()
                uploadMedicin(adminName)
            elif proceses == "2":
                print("="*200)
                forward()
                AllMedicins(adminName)                
            elif proceses == "3": 
                print("="*200)
                forward()
                updateModify(adminName)
            elif proceses == "4": 
                print("="*200)
                forward()
                deleteInfo(adminName)
            elif proceses == "5":
                print("="*200) 
                forward()
                specificMdDetial(adminName)
            elif proceses == "6":
                print("="*200) 
                forward()
                viewAllOrders(adminName)
            elif proceses == "7":
                print("="*200) 
                forward()
                specificOrderDetial(adminName)
            elif proceses == "8":
                print("="*200)  
                back()
                main()


        
                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  New User ******* Function #############

def newUser(): 
    print("="*200)
    print("[1]- Enter One To Regist Into The System")
    print("[2]- Enter Two To View  Medicins")
    print("[3]- Enter Three To Exit ")
    print("="*200)
    print("Enter The Value Here Please: ")
    while  True: 
            proceses = input("")
            if proceses  in ["1","2","3"]: 
                break
            else:
                print("Please re-Enter your option, your option should be From 1 to 3\n")
                print("")
    if proceses == "1": 
        userRegist()
    elif proceses == "2": 
        allMedicinsNewUser()
    elif proceses == "3": 
            print("="*200)
            back()
            main()
    Function_out(main)
    newUser()

                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  Regested user****** Function #############
                                       
def registedUser(): 
        log = 2
        userName = logIn(log)
        if userName:
            startMaessage("Resgisted User",userName)
            print("="*200)
            print("[1]- Enter To View The Available Medicin In System ")
            print("[2]- Enter Two To Order a Medicin")
            print("[3]- Enter Three To Veiw Orders")
            print("[4]- Enter Four To View Personl Information")
            print("[5]- Enter Five To Exit \n")
            print("="*200)
            print("Enter The Value Here Please: ")
            while  True: 
                proceses   = input(" ")
                if proceses in ["1","2","3","4","5"]: 
                    break
                else: 
                    print("")
                    print("Please re-Enter your option, your option should be From 1 to 5 \n") 
            if proceses == "1" : 
                allMedicinsRegistedUser(userName)
            elif proceses == "2": 
                orderPay(userName)
            elif proceses == "3":
                viewPersonalOrders(userName)
            elif proceses == "4":
                viewPersonalInforamtion(userName)
            else: 
                print("="*200)
                back()                                
                main()
        Function_out(main)
        registedUser()


                                #============================================================================================
                                                
                                        ##########                      ##               ###########     #           #
                                        ##                   #          ##               #               #           #
                                        ##                 #   #        ##               #               #           #
                                        ########         #       #      ##               ###########     ########### #
                                              ##        # ######## #    ##               #               #           #
                                              ##      #              #  ##               #               #           #
                                        #######     #                 # ###############  ###########     #           #

                                    #                       ***** Third Layer Functions Start ****
                                #============================================================================================

#############################################                                                          ################################################
                                                            #                                     #
                                                         #######                               #######
                                                        #########                             #########
                                                        #########                             #########                     
                                                         #######                               #######
                                                            #                                     #
                                            ####################### Section Major Functions Section ##################

###########################################                                                           ####################################################



                                                         ##                              ##                                  
                                                        #####                           ####                
                                                        #########                   #########                  
                                                        #########                   #########                 
                                                        ########                     #########                 
                                                        #######                        #######       
                                                                                                    
                                                    ############  Main ****** Function #############
def main():
    print("="*200 +"\n")
    #Ask which type of user:
    print(" "*55 + "Hello and Welcome to “OCEAN Sdn Bhd” Online Pharmacy Management System" +"\n")
    Ocean()
    print("\n"+"="*200)
    print("[1]- Enter one For Admin")
    print("[2]- Enter Two For New  Customer")
    print("[3]- Enter Three For  Registered Customer Customer")
    print("[4]- Enter Four to Exit")
    while  True: 
            select  = input("Enter Your Option Here please: ")
            if select in ["1","2","3","4"]: 
                break
            else: 
                print("")
                print("Please re-Enter your option, your option should be From 1 to 4\n")
    print("="*200+ "\n") 
    print("*"*200)
    if(select == "1"): 
        forward()
        admin()
    elif (select == "2"):
        forward()
        newUser()
    elif (select == "3"): 
        forward()
        registedUser()
    elif select == "4": 
        byeBye()
        import sys
        sys.exit()
main()