from contact_model import *
import re
import importlib
import sys

# importlib.import_module("contact.model")

class Contact:
    def menu(self):
        valid_select = False
        while valid_select == False:
            print("=======Contact Manager=======")
            print("| 1: Add New Contact        |")
            print("| 2: Update a Contact       |")
            print("| 3: Delete a Contact       |") 
            print("| 4: List all Contacts      |")
            print("| 5: Export contacts as VCF |")
            print("| 6: Exit this program      |")
            print("=============================")
            selection = input("Enter a selection to continue: ")

            if selection == '1':
                self.createContact()
                valid_select = True

            elif selection == '2':
                self.updateContact()
                valid_select = True

            elif selection == '3':
                self.deleteContact()
                valid_select = True

            elif selection == '4':
                self.listContacts()
                valid_select = True

            elif selection == '5':
                self.exportContacts()
                valid_select = True

            elif selection == '6':
                print("Exiting...")
                sys.exit()

            else:
                print("Input not recognized. Exiting")

    #1 (Nothing wrong with me)
    def createContact(self):
        createmode = True
        while createmode == True:
            first = input("\n| First name: ")
            last = input("| Last name: ")
            num = input("| Phone number: ")

            #sanitize/filter the inputs
            num = re.sub("[^0-9]", "", num)
            first = re.sub("[^a-zA-Z]+", "", first)
            last = re.sub("[^a-zA-Z]+", "", last)

            print("Parsed input:")
            print("\n| First name: {0} \n| Last name: {1}\n| Phone number: {2}".format(first, last, num))
            correct = input("\nIs this correct? (Y/n): ")

            if correct == 'Y' or correct == 'y' or correct == '':
                print("Sending to database...\n")
                Contacts(first_name=first,last_name=last,phone_number=num).save()
                createmode = False
            else:
                print("Not committed, re-prompting..")
            


        # valid_select = False
        self.menu()

    #2 (Nothing wrong with me)
    def updateContact(self):
        searchtype = input("Search & Update (ID/F/L/#): ")
        if searchtype == 'id' or searchtype == 'ID' or searchtype == 'Id' or searchtype == 'iD':
            cid = input("Enter the contact's ID: ")
            cid = re.sub("[^0-9]", "", cid)
            sql = Contacts.select().where(Contacts.id == cid).limit(1)
            
            if sql.exists():
                clist = list(sql)
                for item in clist:
                    print("_________________\n| Contact found: \n|----------------\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}".format(item.first_name,item.last_name,item.phone_number))

                print("|----------------")
                first = input("| New first name: ")
                last = input("| New last name: ")
                num = input("| New number:")
                
                
                #sanitize/filter the inputs
                num = re.sub("[^0-9]", "", num)
                first = re.sub("[^a-zA-Z]+", "", first)
                last = re.sub("[^a-zA-Z]+", "", last)
                print(cid)
                sql = Contacts.update( id=Contacts.id,first_name=first,last_name=last,phone_number=num ).where(Contacts.id==cid)
                sql.execute()
    
                self.menu()

                
            else: 
                print("Invalid input or no ID specified.\n")
                self.updateContact()

        elif searchtype == 'F' or searchtype == 'f':
            # print()
            fsearch = input("Enter the contact's first name: ")
            cid = re.sub("[^a-zA-Z]", "", fsearch)
            sql = Contacts.select().where(Contacts.id == cid).limit(1)

        elif searchtype == 'L' or searchtype == 'l':
            print('blah 2')




    
    
    def listContacts(self):
        sql = Contacts.select()
        result = list(sql)
        print("\n=============================\n|       Contacts List:      |\n=============================\n")
        for item in result:
            print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name, item.last_name, item.phone_number,item.id))
        valid_select = False
        input("Press any key to continue. ")
        self.menu()

app = Contact()
app.menu()