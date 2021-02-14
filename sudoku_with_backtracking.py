a=[
    [0,0,5,3,0,0,0,0,0],
    [8,0,0,0,0,0,0,2,0],
    [0,7,0,0,1,0,5,0,0],
    [4,0,0,0,0,5,3,0,0],
    [0,1,0,0,7,0,0,0,6],
    [0,0,3,2,0,0,0,8,0],
    [0,6,0,5,0,0,0,0,9],
    [0,0,4,0,0,0,0,3,0],
    [0,0,0,0,0,9,7,0,0]
]

def Find_unsolved_spaces(a):
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                return (i,j)
    return None

def print_board(d):
    for i in range(9):
        print(f'{d[i][0]} {d[i][1]} {d[i][2]} | {d[i][3]} {d[i][4]} {d[i][5]} | {d[i][6]} {d[i][7]} {d[i][8]}')
        if i==2 or i==5:
            print(f'---------------------')

def valid(a,pos_x,pos_y,num):
    for i in range(len(a[0])):
        if a[pos_x][i] == num and pos_y != i:
            return False

    for i in range(len(a)):
        if a[i][pos_y] == num and pos_x != i:
            return False

    box_x = int(pos_y / 3)
    box_y = int(pos_x / 3)

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if a[i][j] == num and (i,j) != (pos_x,pos_y):
                return False

    return True

def Solution(a):
    find=Find_unsolved_spaces(a)
    if not find:
        return True
    else:
        x,y=find
    
    for i in range(1,10):
        if valid(a,x,y,i):
            
            a[x][y]=i
        
            if Solution(a):
                return True

            a[x][y] = 0

    return False

Solution(a)
print_board(a)
