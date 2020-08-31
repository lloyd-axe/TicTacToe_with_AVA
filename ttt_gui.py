from tkinter import *
from tkinter import messagebox
from main import play_ai
import random
import os
import sqlite3

root  = Tk()
root.title("Tic Tac Toe with AVA")
root.resizable(width=False, height=False)
root.iconbitmap('sampleico1.ico')
tit1 = Label(root, text='Tic Tac Toe with AVA\nPlease choose your symbol:')
tit1.grid(row=0, column=0, columnspan=3)
tit3 = Label(root, text='By: Lloyd Acha')
tit3.grid(row=3, column=0)


def game_record(pWin, aWin):
	conn =sqlite3.connect('game_records.db')
	c = conn.cursor()
	c.execute("SELECT *, oid FROM game_records")
	recs = c.fetchall()
	recsl = list(recs[0])
	cur_pwins = recsl[0]
	cur_awins = recsl[1]
	if pWin:
		cur_pwins +=1
	if aWin:
		cur_awins +=1
	print(cur_pwins, cur_awins)
	c.execute("UPDATE game_records SET player_wins = :cur_pwins, ava_wins = :cur_awins WHERE oid = 1",
		{
		'cur_pwins': cur_pwins,
		'cur_awins': cur_awins
		})
	conn.commit()
	conn.close()
	return cur_pwins, cur_awins

def ply_chc(p_sym):
	root.withdraw()
	def btn_clk(val,sym):
		a_sym = 'X' if sym == 'O' else 'O'
		isDraw = False
		board = [
				[b1.get(),b2.get(),b3.get()],
				[b4.get(),b5.get(),b6.get()],
				[b7.get(),b8.get(),b9.get()]
			]
		paths = [
				[[0,0],[1,1],[2,2]],
				[[0,2],[1,1],[2,0]],
				[[0,0],[0,1],[0,2]], 
				[[1,0],[1,1],[1,2]],
				[[2,0],[2,1],[2,2]],
				[[0,0],[1,0],[2,0]],
				[[0,1],[1,1],[2,1]],
				[[0,2],[1,2],[2,2]]
			]

		if val == 1:
			py,px = 0,0
			btn1.config(text=sym, state=DISABLED)
			b1.insert(0, sym)
		elif val == 4:
			py,px = 1,0
			btn4.config(text=sym, state=DISABLED)
			b4.insert(0, sym)
			board = play_ai(board, p_sym)
		elif val == 7:
			py,px = 2,0
			btn7.config(text=sym, state=DISABLED)
			b7.insert(0, sym)
		elif val == 2:
			py,px = 0,1
			btn2.config(text=sym, state=DISABLED)
			b2.insert(0, sym)
		elif val == 5:
			py,px = 1,1
			btn5.config(text=sym, state=DISABLED)
			b5.insert(0, sym)
		elif val == 8:
			py,px = 2,1
			btn8.config(text=sym, state=DISABLED)
			b8.insert(0, sym)
		elif val == 3:
			py,px = 0,2
			btn3.config(text=sym, state=DISABLED)
			b3.insert(0, sym)
		elif val == 6:
			py,px = 1,2
			btn6.config(text=sym, state=DISABLED)
			b6.insert(0, sym)
		elif val == 9:
			py,px = 2,2
			btn9.config(text=sym, state=DISABLED)
			b9.insert(0, sym)
		pl_lb.config(text="AVA has moved, It's you're turn, you are " + p_sym +".")
		board = [
				[b1.get(),b2.get(),b3.get()],
				[b4.get(),b5.get(),b6.get()],
				[b7.get(),b8.get(),b9.get()]
			]
		#draw check
		#win check
		pWin = False
		aWin = False
		#for player
		for a in range(8):
			w_count = 0
			if not pWin:
				for b in range(3):
					cx = paths[a][b][1]
					cy = paths[a][b][0]
					if board[cy][cx] == sym:
						w_count += 1
					if w_count == 3:
						pWin = True
		if pWin:
			pl_lb.config(text="Player has won. Nice!")
			cur_pwins, cur_awins, = game_record(pWin, aWin)
			s_lb.config(text="Record:\nPlayer - " + str(cur_pwins) +"\nAVA - " + str(cur_awins))
			play_again = messagebox.askyesno('GAME DONE', 'Player Won!\nPlay Again?')
			btn1.config(state=DISABLED)
			btn2.config(state=DISABLED)
			btn3.config(state=DISABLED)
			btn4.config(state=DISABLED)
			btn5.config(state=DISABLED)
			btn6.config(state=DISABLED)
			btn7.config(state=DISABLED)
			btn8.config(state=DISABLED)
			btn9.config(state=DISABLED)
			if play_again:
				root.deiconify()
				top.destroy()
				return
			else:
				print('nah')
				return		
		turns = 0
		for a in range(3):
			for b in range(3):
				if board[a][b] != '':
					turns +=1
		#board analysis
		
		
		#AI move
		ai_coord, isDraw = play_ai(board, p_sym)
		if isDraw:
			pl_lb.config(text="It's a DRAWWW!!!!!")
			play_again = messagebox.askyesno("GAME DONE", "It's a Draw!\nPlay Again?")
			if play_again:
				root.deiconify()
				top.destroy()
				return
			else:
				print('nah')
				return
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

		for a in range(8):
			w_count = 0
			if not aWin:
				for b in range(3):
					cx = paths[a][b][1]
					cy = paths[a][b][0]
					if board[cy][cx] == a_sym:
						w_count += 1
					if w_count == 3:
						aWin = True
		if aWin:
			pl_lb.config(text="AVA won. by... ay nko")
			cur_pwins, cur_awins, = game_record(pWin, aWin)
			s_lb.config(text="Record:\nPlayer - " + str(cur_pwins) +"\nAVA - " + str(cur_awins))
			play_again = messagebox.askyesno('GAME DONE', 'AVA Wins!\nPlay Again?')
			
			btn1.config(state=DISABLED)
			btn2.config(state=DISABLED)
			btn3.config(state=DISABLED)
			btn4.config(state=DISABLED)
			btn5.config(state=DISABLED)
			btn6.config(state=DISABLED)
			btn7.config(state=DISABLED)
			btn8.config(state=DISABLED)
			btn9.config(state=DISABLED)
			if play_again:
				root.deiconify()
				top.destroy()
				return
			else:
				print('nah')
				return
			

	top = Tk()
	top.title('Tic Tac Toe with AVA')
	top.resizable(width=False, height=False)
	top.iconbitmap('sampleico1.ico')
	pl_lb = Label(top, text="It's you're turn, you are " + p_sym +".")
	pl_lb.grid(row=0, column=0, columnspan=3, sticky=W)
	pWin = False
	aWin = False
	cur_pwins, cur_awins, = game_record(pWin, aWin)
	s_lb = Label(top, text="Record:\nPlayer - " + str(cur_pwins) +"\nAVA - " + str(cur_awins))
	s_lb.grid(row=1, column=0, columnspan=3, sticky=W)
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
		pl_lb.config(text="AVA has moved, It's you're turn, you are " + p_sym +".")

	board = [
				[b1.get(),b2.get(),b3.get()],
				[b4.get(),b5.get(),b6.get()],
				[b7.get(),b8.get(),b9.get()]
			]

	top.mainloop()


btn_O = Button(root, text='O', command=lambda: ply_chc('O'), width=12,height=3)
btn_X = Button(root, text='X', command=lambda: ply_chc('X'), width=12,height=3)
btn_O.grid(row=2,column=0)
btn_X.grid(row=2,column=1)


root.mainloop()