from contact_model import *
import re
import importlib
import sys
import vobject
import phonenumbers

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
            print("| 5: Search for Contacts    |")
            print("| 6: Export contacts as VCF |")
            print("| 7: Exit this program      |")
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
                self.find()
                valid_select = True
            
            elif selection == '6':
                self.exportVCF()
                valid_select = True

            elif selection == '7':
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

            print("\nParsed input:")
            print("\n| First name: {0} \n| Last name: {1}\n| Phone number: {2}".format(first, last, num))
            correct = input("\nIs this correct? (Y/n): ")

            if correct == 'Y' or correct == 'y' or correct == '':
                print("Sending to database...\n")
                Contacts(first_name=first,last_name=last,phone_number=num).save()
                input("Contact created successfully. Press any key to continue. ")
                createmode = False
            else:
                print("Not committed, re-prompting..")
            


        valid_select = False
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
                # print(cid)

                print("Sending to database...\n")
                sql = Contacts.update( id=Contacts.id,first_name=first,last_name=last,phone_number=num ).where(Contacts.id==cid)
                sql.execute()
                valid_select = False
                self.menu()

                
            else: 
                print("Invalid input or no ID specified.\n")
                self.updateContact()

        elif searchtype == 'F' or searchtype == 'f':
            # print()
            fsearch = input("Enter the contact's first name: ")
            fsearch = re.sub("[^a-zA-Z]", "", fsearch)
            sql = Contacts.select().where(Contacts.first_name.contains(fsearch))

            if sql.exists():
                clist = list(sql)
                print("| Contact(s) found: \n|------------------\n")
                for item in clist:
                    print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name,item.last_name,item.phone_number,item.id))
                
                editid = input("Enter ID of contact you wish to edit (n to quit): ")
                if editid == 'n' or editid == 'N':
                    valid_select = False
                    self.menu()
                else:
                    editid = re.sub("[^0-9]", "", editid)

                    print("|----------------")
                    first = input("| New first name: ")
                    last = input("| New last name: ")
                    num = input("| New number:")
                    
                    num = re.sub("[^0-9]", "", num)
                    first = re.sub("[^a-zA-Z]+", "", first)
                    last = re.sub("[^a-zA-Z]+", "", last)
                    
                    print("Sending to database...\n")
                    
                    sql = Contacts.update( id=Contacts.id,first_name=first,last_name=last,phone_number=num ).where(Contacts.id==editid)
                    sql.execute()
                    valid_select = False
                    self.menu()

            else: 
                print("Invalid input or not found.\n")
                self.updateContact()

        elif searchtype == 'L' or searchtype == 'l':
            # print()
            lsearch = input("Enter the contact's last name: ")
            lsearch = re.sub("[^a-zA-Z]", "", lsearch)
            sql = Contacts.select().where(Contacts.last_name.contains(lsearch))

            if sql.exists():
                clist = list(sql)
                print("| Contact(s) found: \n|------------------\n")
                for item in clist:
                    print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name,item.last_name,item.phone_number,item.id))
                
                editid = input("Enter ID of contact you wish to edit (n to quit): ")
                if editid == 'n' or editid == 'N':
                    valid_select = False
                    self.menu()
                else:
                    editid = re.sub("[^0-9]", "", editid)

                    print("|----------------")
                    first = input("| New first name: ")
                    last = input("| New last name: ")
                    num = input("| New number:")

                    num = re.sub("[^0-9]", "", num)
                    first = re.sub("[^a-zA-Z]+", "", first)
                    last = re.sub("[^a-zA-Z]+", "", last)

                    print("Sending to database...\n")
                    sql = Contacts.update( id=Contacts.id,first_name=first,last_name=last,phone_number=num ).where(Contacts.id==editid)
                    sql.execute()
                    valid_select = False
                    self.menu()
                    
            else: 
                print("Invalid input or no ID specified.\n")
                self.updateContact()

        elif searchtype == '#' or searchtype.lower() == 'num':
            numsearch = input("Enter the contact's number: ")
            numsearch = re.sub("[^0-9]", "", numsearch)
            sql = Contacts.select().where(Contacts.phone_number.cast('varchar').contains(numsearch))

            if sql.exists():
                clist = list(sql)
                print("| Contact(s) found: \n|------------------\n")
                for item in clist:
                    print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name,item.last_name,item.phone_number,item.id))
                
                editid = input("Enter ID of contact you wish to edit (n to quit): ")
                if editid == 'n' or editid == 'N':
                    self.menu()
                else:
                    editid = re.sub("[^0-9]", "", editid)

                    print("|----------------")
                    first = input("| New first name: ")
                    last = input("| New last name: ")
                    num = input("| New number:")

                    print("Sending to database...\n")
                    num = re.sub("[^0-9]", "", num)
                    first = re.sub("[^a-zA-Z]+", "", first)
                    last = re.sub("[^a-zA-Z]+", "", last)
                    sql = Contacts.update( id=Contacts.id,first_name=first,last_name=last,phone_number=num ).where(Contacts.id==editid)
                    sql.execute()
                    valid_select = False
                    self.menu()
            
            else: 
                print("Invalid input or no ID specified.\n")
                self.updateContact()
            


        else:
            print("Invalid search type.")
            self.updateContact()


    #3 (Nothing wrong with me)
    def deleteContact(self):
        cid = input("Enter id of contact to delete: ")
        cid = re.sub("[^0-9]", "", cid)

        sql = Contacts.select().where(Contacts.id == cid).limit(1)

        if sql.exists():
            print("ID found, removing from database...")
            sql = Contacts.delete_by_id(cid)
            print("Successfully removed.")
            valid_select = False
            self.menu()

        else:
            print("ID not found, returning to main menu.")
            valid_select = False
            self.menu()

    
    #4 (Nothing wrong with me)
    def listContacts(self):
        sql = Contacts.select().order_by(Contacts.id.asc())
        result = list(sql)
        print("\n=============================\n|       Contacts List:      |\n=============================\n")
        for item in result:
            print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name, item.last_name, item.phone_number,item.id))
        valid_select = False
        input("Press any key to continue. ")
        self.menu()

    def find(self):
        searchtype = input("Search for Contact(s) (ID/F/L/#): ")

        if searchtype.lower() == 'id':
            cid = input("Enter the contact's ID: ")
            cid = re.sub("[^0-9]", "", cid)
            sql = Contacts.select().where(Contacts.id == cid).limit(1)
            
            if sql.exists():
                clist = list(sql)
                for item in clist:
                    print("_________________\n| Contact found: \n|----------------\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}".format(item.first_name,item.last_name,item.phone_number))

                print("|----------------")
                input("Press any key to continue. ")
                valid_select = False
                self.menu()
            else:
                print("No contact found with supplied ID.")
                input("Press any key to continue. ")
                valid_select = False
                self.menu()
        
        elif searchtype.lower() == 'f':
            fsearch = input("Enter the contact's first name: ")
            fsearch = re.sub("[^a-zA-Z]", "", fsearch)
            sql = Contacts.select().where(Contacts.first_name.contains(fsearch))

            if sql.exists():
                clist = list(sql)
                print("| Contact(s) found: \n|------------------\n")
                for item in clist:
                    print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name,item.last_name,item.phone_number,item.id))

                input("Press any key to continue. ")
                valid_select = False
                self.menu()

            else:
                print("No contact found with supplied partial.")
                input("Press any key to continue. ")
                valid_select = False
                self.menu()
    
        elif searchtype.lower() == 'l':
                lsearch = input("Enter the contact's last name: ")
                lsearch = re.sub("[^a-zA-Z]", "", lsearch)
                sql = Contacts.select().where(Contacts.last_name.contains(lsearch))

                if sql.exists():
                    clist = list(sql)
                    print("| Contact(s) found: \n|------------------\n")
                    for item in clist:
                        print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name,item.last_name,item.phone_number,item.id))

                    input("Press any key to continue. ")
                    valid_select = False
                    self.menu()

                else:
                    print("No contact found with supplied partial.")
                    input("Press any key to continue. ")
                    valid_select = False
                    self.menu()

        elif searchtype == '#' or searchtype.lower() == 'num':
            numsearch = input("Enter the contact's number: ")
            numsearch = re.sub("[^0-9]", "", numsearch)
            sql = Contacts.select().where(Contacts.phone_number.cast('varchar').contains(numsearch))

            if sql.exists():
                clist = list(sql)
                print("| Contact(s) found: \n|------------------\n")
                for item in clist:
                    print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name,item.last_name,item.phone_number,item.id))

                input("Press any key to continue. ")
                valid_select = False
                self.menu()

            else:
                print("No contact found with supplied partial.")
                input("Press any key to continue. ")
                valid_select = False
                self.menu()


    def exportVCF(self):
        sql = Contacts.select().order_by(Contacts.id.asc())
        result = list(sql)

        for item in result:
            # print("| ID:\t\t{3}\n| First:\t{0}\n| Last:\t\t{1}\n| Number: \t{2}\n".format(item.first_name, item.last_name, item.phone_number,item.id))
            vcf = vobject.vCard()
            vcf.add('n')
            vcf.add('fn')
            vcf.add('tel')
            vcf.tel.type_param = 'cell'
            vcf.n.value = vobject.vcard.Name(family=item.last_name, given=item.first_name)
            vcf.fn.value = item.first_name + ' ' + item.last_name
            vcf.tel.value = str(phonenumbers.format_number(phonenumbers.parse(str(item.phone_number), 'US'), phonenumbers.PhoneNumberFormat.NATIONAL))
            # vcf.serialize()
            vcf.prettyPrint()
            with open(str(item.id)+'-'+item.first_name+'-'+item.last_name+'.vcf', 'w') as file:
                file.write(str(vcf.serialize()))


        valid_select = False
        input("Press any key to continue. ")
        self.menu()
            
    




app = Contact()
app.menu()