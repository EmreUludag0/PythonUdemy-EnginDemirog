import sqlite3

def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")

    cursor = connection.execute("""select FirstName, LastName
                                    from customers
                                    where FirstName like '%ja'   """)


    for row in cursor:
        print("First Name= " + row[0])
        print("Last Name=  " + row[1])
        print("*************")

    print("***********************************************************************")

    #cursor = connection.execute(""" select city, count(*) from Customers
    #                            group by city having count(*)>1
    #                            order by count(*) desc""")


    #for row in cursor:
    #    print("City= " + row[0])
    #    print("Count=  " + str(row[1]))
    #    print("*************")


    connection.close()


selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers 
                        (firstName, lastName,city) 
                        values '(Emre', 'Uludag', 'Istanbul') """)
    connection.commit()
    connection.close()

#insertCustomer()

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city ='İstanbul'
                        where city = 'Ankara' """)

    connection.commit()
    connection.close()

updateCustomer()



















