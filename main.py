import random

board = [
			[' ', ' ', ' '],
			[' ', ' ', ' '],
			[' ', ' ', ' ']
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

def play_player(px, py, board, p_sym):
	board[py][px] = p_sym
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
	p_path = []
	for a in range(8):
		for b in range(3):
			ppx = paths[a][b][1]
			ppy = paths[a][b][0]
			if board[ppy][ppx] == p_sym:
				p_path.append(a)
				break

def win_checker(p_sym, a_sym, p_path, a_path, board):
    set_a = set(a_path)
    set_p = set(p_path)
    unc_apath = list(set_a - set_p)
    unc_ppath = list(set_p - set_a)

    p_count = 0
    a_count = 0
    blnk_p = []
    blnk_a = []
    ptoWin = False
    atoWin = False

    for a in unc_ppath: #all paths
        for b in range(3): #coords on each path
            cx = paths[a][b][1]
            cy = paths[a][b][0]
            if board[cy][cx] == p_sym: #count p sym
                p_count += 1
            elif board[cy][cx] == '': #locate remaining cell
                blnk_p = [cy,cx]
                print(f'b {blnk_p}')
        if p_count == 2: #p is 1 away from win
                ptoWin = True
                break
        else:
            p_count = 0 #reset if not 2

    #ai to win
    for a in unc_apath: #all paths
        for b in range(3): #coords on each path
            cx = paths[a][b][1]
            cy = paths[a][b][0]
            if board[cy][cx] == a_sym: #count p sym
                a_count += 1
            elif board[cy][cx] == '': #locate remaining cell
                blnk_a = [cy,cx]
                print(f'ba {blnk_p}')
        if a_count == 2: #p is 1 away from win
                atoWin = True
                break
        else:
            a_count = 0 #reset if not 2
    return ptoWin, atoWin, blnk_p, blnk_a

def play_ai(board, p_sym):
	a_sym = 'X' if p_sym == 'O' else 'O'
	turns = 0
	for a in range(3):
		for b in range(3):
			if board[a][b] != '':
				turns +=1
	#board analysis
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
	p_path = []
	for a in range(8):
		for b in range(3):
			ppx = paths[a][b][1]
			ppy = paths[a][b][0]
			if board[ppy][ppx] == p_sym:
				p_path.append(a)
				break
	a_path = []
	for a in range(8):
		for b in range(3):
			apx = paths[a][b][1]
			apy = paths[a][b][0]
			if board[apy][apx] == a_sym:
				a_path.append(a)
				break
	print(turns)
	print(p_path)
	print(a_path)
	#first turn
	if turns <=1:
		while True:
			ai_path1 = random.randint(0,7)
			ai_path2 = random.randint(0,2)
			x1 = paths[ai_path1][ai_path2][1]
			y1 = paths[ai_path1][ai_path2][0]
			print(y1,x1)
			print(board)
			if board[y1][x1] != p_sym:
				print(board[y1][x1])
				board[y1][x1] = a_sym
				ai_coord = [y1, x1]
				return ai_coord
	else:
		set_p = set(p_path)
		set_a = set(a_path)
		unc = set_a - set_p
		avl_a = list(unc)
		ptoWin, atoWin, blnk_p, blnk_a = win_checker(p_sym, a_sym, p_path, a_path, board)

		if atoWin:
			ax = blnk_a[1]
			ay = blnk_a[0]
			ai_coord = [ay, ax]
			board[ay][ax] = a_sym
			return ai_coord
		if ptoWin:
			ax = blnk_p[1]
			ay = blnk_p[0]
			ai_coord = [ay, ax]
			board[ay][ax] = a_sym
			return ai_coord

		if avl_a != []:
			ai_path = random.choice(avl_a)
			print(f'avl {avl_a}')
			avl_cells = paths[ai_path]
			while True:
				nxt_move = random.randint(0,2)
				cx = avl_cells[nxt_move][1]
				cy = avl_cells[nxt_move][0]
				if board[cy][cx] == '':
					ai_coord = [cy,cx]
					board[cy][cx] = a_sym
					return ai_coord
		else:
			print('empty')
			while True:
				ai_path1 = random.randint(0,7)
				ai_path2 = random.randint(0,2)
				x1 = paths[ai_path1][ai_path2][1]
				y1 = paths[ai_path1][ai_path2][0]
				print(y1,x1)
				print(board)
				print('aaaaaa')
				if board[y1][x1] == '':
					print(board[y1][x1])
					board[y1][x1] = a_sym
					ai_coord = [y1, x1]
					return ai_coord
	print(board)
	return ai_coord