# pomodoro

import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound


# main script 
t_now = dt.datetime.now()  #current time
t_pom = 25*60  #pomodoro time
t_delta = dt.timedelta(0,t_pom) #time delta in minutes
t_fut = t_now + t_delta
delta_sec = 5*60
t_fin = t_now + dt.timedelta(0,t_pom+delta_sec)


root = tkinter.Tk()
root.withdraw()
#show alert
messagebox.showinfo("Pomodoro Started!" , "\nIt is now " +t_now.strftime("%H:%M") + "hrs. \nTimer set for 25 minutes.")


#main script(loop)
while True:
	# pomodoro time
	if t_now < t_fut:
		print('pomodoro')

	elif t_fut <= t_now <= t_fin:
		#check if is the first time here, if it is, ring a bell
		print('in break')
		if breaks == 0:
			print('if break')
			#annoy!!!
			for i in range(5):
				winsound.Beep((i+100), 700)
			print('Break time!@')
			breaks += 1


	else:
		print('finished')

		breaks = 0

		#let user know break is over
		for i in range(10):
			winsound.Beep((i+100), 500)
			#ask if they want to start again

		usr_ans = messagebox.askyesno("Pomodoro finished!", "Would you like to start another Pomodoro?")
		total_pomodoros += 1
		if usr_ans == True:


			t_now = dt.datetime.now()
			t_fut = t_now + dt.timedelta(0,t_pom)
			t_fin = t_now + dt.timedelta(0,t+pom+delta_sec)
			continue

		elif usr_ans == False:


			messagebox.showinfo("Pomodoro Finished!" , "\nYou completed "+str(total_pomodoros)+" pomodoros today!")
			break