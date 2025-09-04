from datetime import date
import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="Chandu@30"
  )

connect()
c1 = db1.cursor()
c1.execute("drop database hotel")
c1.execute("create database hotel")
c1.execute("use hotel")
c1.execute("create table rooms(romm_no integer,type varchar(50),location varchar(30),no_of_guest integer,rent_per_day integer, status varchar(20))")
c1.execute("create table booking(room_no integer,cname varchar(20),idtype varchar(40),idno varchar(40),address varchar(50),phone varchar(10),gender varchar(20),dcheckin date,type varchar (50),rent_per_day integer)")

db1.commit()

import mysql.connector as mycon
con = mycon.connect(host="localhost",user="root",password="Chandu@30",database="hotel")

def showmenu():
    while True:
        print("@" * 30)
        print("----    HOTEL ATITHI    ----")
        print("@" * 30)
        print("Press 1 - Create a New Room")
        print("Press 2 - Show All Rooms")
        print("Press 3 - Show All Vacant Rooms")
        print("Press 4 - Show All Occupied Rooms")
        print("Press 5 - Book a Room")
        print("Press 6 - Check Out")
        print("Press 7 - Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            createRoom()
        elif choice == 2:
            showRooms()
        elif choice == 3:
            showVacantRooms()
        elif choice == 4:
            showOccupiedRooms()
        elif choice == 5:
            bookRoom()
        elif choice == 6:
            checkout()
        elif choice == 7:
            break
def createRoom():
    print(" --- ENTER ROOM DETAILS  --- ")
    rno = int(input("Enter Room No. : "))
    type = input("Enter Room Type(Simple/Delux/Super Delux):")
    guest = int(input("Enter maximum number of guests : "))
    loc = input("Enter Location details : ")
    rent_per_day = int(input("Enter Per Day Charges : "))
    status = "Vacant"
    q = "insert into rooms values(%s,%s,%s,%s,%s,%s)"
    data = (rno,type,loc,guest,rent_per_day,status)
    cr1 = con.cursor()
    cr1.execute(q,data)
    con.commit()
    print("---  Room Created Successfully  ---")

def showRooms():
    q = "select * from rooms"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)

def showVacantRooms():
    q = "select * from rooms where status='Vacant'"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)

def showOccupiedRooms():
    q = "select room_no, cname, phone from rooms,booking where status='Occupied' and romm_no = room_no"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)

def bookRoom():
    print("-" * 40)
    print("       BOOKING A ROOM ")
    print("-" * 40)
    room_no = int(input("Enter Room number : "))
    cname = input("Enter the Customer Name : ")
    idtype = input("Enter the ID submitted(PAN Card/License/Aadhar Card/Passport) : ")
    idno = input("Enter the ID number : ")
    address = input("Enter Address : ")
    phone = input("Enter Phone number : ")
    gender = input("Enter Gender : ")
    dcheckin = input("Enter Date of Check in (yyyy-mm-dd) : ")
    type = input("Enter Room Type(Simple/Delux/Super Delux):")
    rent_per_day = int(input("Enter Per Day Charges : "))
    q = "insert into booking(room_no,cname,idtype,idno,address,phone,gender,dcheckin,type,rent_per_day) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (room_no,cname,idno,idtype,address,phone,gender,dcheckin,type,rent_per_day)
    cr = con.cursor()
    cr.execute(q,data)
    con.commit()
    q = "update rooms set status='Occupied' where romm_no ="+ str(room_no)
    cr.execute(q)
    con.commit()
    print("-" * 50)
    print("      ROOM BOOKED")
    print("-" * 50)

from datetime import datetime

#Function to checkout a guest
def checkout():
    print("_______________ATITHI HOTEL PAYMENT AND CHECKOUT DETAIL__________________________")
    room_no = input("Enter the Room Number : ")
    q = "select room_no, cname, phone from rooms,booking where status='Occupied' and romm_no =" + room_no
    q = "select * from booking"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)
    print("\n")
    print("-" * 130)
    print("room_No\t\tcname\t\tidno\t\tidtype\t\taddress\t\t\tphone\t\tgender\t\tdcheckin\t\ttype\t\trent_per_day")
    print("-" * 130)
    for q in res:
        print(q[0], "\t\t", q[1],"\t\t", q[2],"\t\t", q[3],"\t\t", q[4],"\t\t", q[5],"\t\t", q[6],"\t\t", q[7],"\t\t", q[8],"\t\t", q[9])
        print("-" * 130)
    dcheckin=input("Enter Date of Check in (yyyy-mm-dd) : ")
    chkoutdate = input("Enter the date of Checkout : ")
    Total_Days=int(input("Enter the Total Number of Days : "))
    Type=input("Enter the Type of room(simple/delux/super delux): ")
    rent_per_day=int(input("Enter the rent per day : "))

    # Calculate total room bill
    Total_payment= Total_Days* rent_per_day

    Total_payment = input(f"The Total Payment is:{Total_payment} ")
    print("Payment Received successfully")
    print("-" * 130)
    print("Checkout Successfully 😇🙃Thank You😇🙃 Visit Again")
    q = "update rooms set status='Vacant' where romm_no =" + str(room_no)
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)
    cr1.execute(q)
    con.commit()


if con.is_connected():
    showmenu()