from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import dbconnection
import time

#global vnumber,drivername, ownername, drivermobile, vehiclemake, vehiclecolor
def quit():
	window.destroy()


def recognize_gui():
	pass

def register_gui():
	global reg_window
	reg_window = tk.Tk()
	reg_window.title('Vehicle Registeration')
	reg_window.geometry('1500x1000')
	reg_window.configure(bg='white')
	#head_img =Image.open('//home//balaji//Downloads//form_header.jpg')
	#head_i = ImageTk.PhotoImage(head_img)
	#Label(reg_window,image=head_i).place(x=0,y=0)

	tk.Label(reg_window,text = 'Vehicle Registration',bg='white',fg='black', font="none 20 bold").place(x=50,y=50)

	tk.Label(reg_window, text = 'Vehicle Number',bg='white',fg='black').place(x=50,y=120)
	vnumber=tk.Entry(reg_window)
	vnumber.place(x=180,y=120)
	
	tk.Label(reg_window, text = 'Driver Name',bg='white',fg='black').place(x=650,y=120)
	drivername=tk.Entry(reg_window )
	drivername.place(x=750,y=120)

	tk.Label(reg_window, text = 'Mobile Number',bg='white',fg='black').place(x=50,y=200)
	drivermobile =tk.Entry(reg_window)
	drivermobile.place(x=180,y=200)
	
	tk.Label(reg_window, text = 'Vehicle Make',bg='white',fg='black').place(x=650,y=200)
	vehiclemake =tk.Entry(reg_window )
	vehiclemake.place(x=750,y=200)

	tk.Label(reg_window, text = 'Owner Name',bg='white',fg='black').place(x=50,y=280)
	ownername = tk.Entry(reg_window)
	ownername.place(x=180,y=280)
	
	tk.Label(reg_window, text = 'Vehicle Colour',bg='white',fg='black').place(x=650,y=280)
	vehiclecolor  =tk.Entry(reg_window)
	vehiclecolor.place(x=750,y=280)

	def reg_submit():
	#print(vehicle_num,driver_name, owner_name, mobile_num, vehicle_make, vehicle_color)
		print(vnumber.get())	
		print(drivername.get())
		print(drivermobile.get())
		print(vehiclemake.get())
		print(ownername.get())
		print(vehiclecolor.get())
		print("im sql")
		sql='''INSERT INTO VEHICLE_DETAILS (VEHICLE_NUMBER,DRIVER_NAME,OWNER_NAME,MOBILE_NUMBER,VEHICLE_MAKE,COLOR ) VALUES (%s, %s, %s, %s, %s, %s)'''
		val = [vnumber,drivername, ownername, str(drivermobile), vehiclemake, vehiclecolor]

		dbconnection.write_to_db(sql,[str(vnumber.get()) , str(drivername.get()) , str(ownername.get()), str(drivermobile.get()), str(vehiclemake.get()), str(vehiclecolor.get())])

		tk.Label(reg_window,text = "VEHICLE REGISTERED SUCCESSFULLY!"  , fg = "green").place(x=600,y=500)
		time.sleep(5)
		reg_window.destroy()	

	Button(reg_window,text='Submit', bg='white', fg='black', bd=10,height=2,width=17, command=reg_submit).place(x=600,y=600)

#Main Window configurations
window = Tk()
window.title("Vehicle Detection and recognition system")
window.geometry('1500x1000')
window.configure(bg='white')

logo = Image.open('//home//balaji//Downloads//mcet_tran.png')
logo = logo.resize((50,50))
logo_d = ImageTk.PhotoImage(logo)

title = Label(window,text ="Dr. Mahalingam College of Engineering and Technology",image = logo_d,compound = 'left',bg='white',fg='black', font='none 24 bold')
title.pack()

register_icon = Image.open('//home//balaji//Downloads//car_reg.png')
register_icon.resize((150,150))
register = ImageTk.PhotoImage(register_icon)
Label(window,image=register).place(x=250,y = 200)

reg_button = Button(window,bd=10,command=register_gui,text='Register',
    bg="white",
    fg="black",
    height=2,
    width=17		
) 
reg_button.place(x=270,y=450)

recog_icon = Image.open("//home//balaji//Downloads//car_reg.png")
recog_icon.resize((100,100))
recognize = ImageTk.PhotoImage(recog_icon)
Label(window,image=recognize).place(x=550,y = 200)

recog_button = Button(window,bd=10,text='Recognize Vehicle',
    bg="white",
    fg="black",
    height=2,
    width=17		
) 
recog_button.place(x=570,y=450)

quit_button = Button(window,text="Quit",fg='black',bg='white',bd=10,height=2,width=17,command=quit)
quit_button.place(x=550,y = 600)

window.mainloop()



