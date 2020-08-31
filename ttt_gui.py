from tkinter import *
from main import play_player, play_ai
import random

root  = Tk()
root.title("Tic Tac Toe with AVA")
root.resizable(width=False, height=False)
tit1 = Label(root, text='Please Choose')
tit1.grid(row=0, column=0)

def ply_chc(p_sym):
	root.destroy()
	def btn_clk(val,sym):
		a_sym = 'X' if sym == 'O' else 'O'
		board = [
				[b1.get(),b2.get(),b3.get()],
				[b4.get(),b5.get(),b6.get()],
				[b7.get(),b8.get(),b9.get()]
			]

		if val == 1:
			py,px = 0,0
			play_player(px, py, board, sym)
			btn1.config(text=sym, state=DISABLED)
			b1.insert(0, sym)
		elif val == 4:
			py,px = 1,0
			play_player(px, py, board, sym)
			btn4.config(text=sym, state=DISABLED)
			b4.insert(0, sym)
			board = play_ai(board, p_sym)
		elif val == 7:
			py,px = 2,0
			play_player(px, py, board, sym)
			btn7.config(text=sym, state=DISABLED)
			b7.insert(0, sym)
		elif val == 2:
			py,px = 0,1
			play_player(px, py, board, sym)
			btn2.config(text=sym, state=DISABLED)
			b2.insert(0, sym)
		elif val == 5:
			py,px = 1,1
			play_player(px, py, board, sym)
			btn5.config(text=sym, state=DISABLED)
			b5.insert(0, sym)
		elif val == 8:
			py,px = 2,1
			play_player(px, py, board, sym)
			btn8.config(text=sym, state=DISABLED)
			b8.insert(0, sym)
		elif val == 3:
			py,px = 0,2
			play_player(px, py, board, sym)
			btn3.config(text=sym, state=DISABLED)
			b3.insert(0, sym)
		elif val == 6:
			py,px = 1,2
			play_player(px, py, board, sym)
			btn6.config(text=sym, state=DISABLED)
			b6.insert(0, sym)
		elif val == 9:
			py,px = 2,2
			play_player(px, py, board, sym)
			btn9.config(text=sym, state=DISABLED)
			b9.insert(0, sym)
		board = [
				[b1.get(),b2.get(),b3.get()],
				[b4.get(),b5.get(),b6.get()],
				[b7.get(),b8.get(),b9.get()]
			]

		#AI move
		ai_coord = play_ai(board, p_sym)
		if ai_coord == [0,0]:
			b1.insert(0, a_sym)
			btn1.config(text=a_sym, state=DISABLED)
		elif ai_coord == [1,0]:
			b4.insert(0, a_sym)
			btn4.config(text=a_sym, state=DISABLED)
		elif ai_coord == [2,0]:
			b7.insert(0, a_sym)
			btn7.config(text=a_sym, state=DISABLED)
		elif ai_coord == [0,1]:
			b2.insert(0, a_sym)
			btn2.config(text=a_sym, state=DISABLED)
		elif ai_coord == [1,1]:
			b5.insert(0, a_sym)
			btn5.config(text=a_sym, state=DISABLED)
		elif ai_coord == [2,1]:
			b8.insert(0, a_sym)
			btn8.config(text=a_sym, state=DISABLED)
		elif ai_coord == [0,2]:
			b3.insert(0, a_sym)
			btn3.config(text=a_sym, state=DISABLED)
		elif ai_coord == [1,2]:
			b6.insert(0, a_sym)
			btn6.config(text=a_sym, state=DISABLED)
		elif ai_coord == [2,2]:
			b9.insert(0, a_sym)
			btn9.config(text=a_sym, state=DISABLED)
			
	top = Tk()
	top.title('Tic Tac Toe with AVA')
	top.resizable(width=False, height=False)
	pl_lb = Label(top, text='You are ' + p_sym)
	pl_lb.grid(row=0, column=0)
	btn1 = Button(top, text=' ', command=lambda: btn_clk(1,p_sym), width=12,height=3)
	btn2 = Button(top, text=' ', command=lambda: btn_clk(2,p_sym), width=12,height=3)
	btn3 = Button(top, text=' ', command=lambda: btn_clk(3,p_sym), width=12,height=3)
	btn4 = Button(top, text=' ', command=lambda: btn_clk(4,p_sym), width=12,height=3)
	btn5 = Button(top, text=' ', command=lambda: btn_clk(5,p_sym), width=12,height=3)
	btn6 = Button(top, text=' ', command=lambda: btn_clk(6,p_sym), width=12,height=3)
	btn7 = Button(top, text=' ', command=lambda: btn_clk(7,p_sym), width=12,height=3)
	btn8 = Button(top, text=' ', command=lambda: btn_clk(8,p_sym), width=12,height=3)
	btn9 = Button(top, text=' ', command=lambda: btn_clk(9,p_sym), width=12,height=3)
	btn1.grid(row=2,column=0)
	btn2.grid(row=2,column=1)
	btn3.grid(row=2,column=2)
	btn4.grid(row=3,column=0)
	btn5.grid(row=3,column=1)
	btn6.grid(row=3,column=2)
	btn7.grid(row=4,column=0)
	btn8.grid(row=4,column=1)
	btn9.grid(row=4,column=2)

	b1 = Entry(top, text='')
	b2 = Entry(top, text='')
	b3 = Entry(top, text='')
	b4 = Entry(top, text='')
	b5 = Entry(top, text='')
	b6 = Entry(top, text='')
	b7 = Entry(top, text='')
	b8 = Entry(top, text='')
	b9 = Entry(top, text='')

	if p_sym == 'X':
		ai_chc1 =[1,3,7,9,5]
		ai_fm = random.choice(ai_chc1)
		if ai_fm == 1:
			btn1.config(text='O', state=DISABLED)
			b1.insert(0, 'O')
		elif ai_fm == 3:
			btn3.config(text='O', state=DISABLED)
			b3.insert(0, 'O')
		elif ai_fm == 7:
			btn7.config(text='O', state=DISABLED)
			b7.insert(0, 'O')
		elif ai_fm == 9:
			btn9.config(text='O', state=DISABLED)
			b9.insert(0, 'O')
		elif ai_fm == 5:
			btn5.config(text='O', state=DISABLED)
			b5.insert(0, 'O')

	board = [
				[b1.get(),b2.get(),b3.get()],
				[b4.get(),b5.get(),b6.get()],
				[b7.get(),b8.get(),b9.get()]
			]

	top.mainloop


btn_O = Button(root, text='O', command=lambda: ply_chc('O'), width=12,height=3)
btn_X = Button(root, text='X', command=lambda: ply_chc('X'), width=12,height=3)
btn_O.grid(row=2,column=0)
btn_X.grid(row=2,column=1)


root.mainloop()