a=[
    [7,3,8,5,1,0,9,6,2],
    [0,4,9,3,0,7,0,0,5],
    [0,5,1,0,2,0,0,0,0],
    [3,0,2,7,0,0,0,0,0],
    [0,0,6,4,0,2,7,5,3],
    [4,0,0,6,0,0,2,1,0],
    [0,0,0,2,0,0,0,3,0],
    [0,0,0,0,3,0,6,4,0],
    [0,0,3,9,0,5,0,2,0]
]
def Find_unsolve_dic(a):
    lst={}
    count=0
    ycord=0
    for x in range(len(a)):
        for y in a[x]:
            if y==0:
                lst[count]=f'{x}{ycord}'   # Check the empty places in the sudoku
                count+=1
            if ycord==8:
                ycord=0
            else:
                ycord+=1
    return lst
    
def Find_ans_dic(lst):    
    dict_for_ans={}
    for x in lst.keys():
        ac=int(lst[x])
        aa=ac%10
        if (ac-aa)==0:
            ab=0
        else:    
            ab=int((ac-aa)/10)
        ans=[]
        for j in range(1,10):
            if j in a[ab]:  # Check the row of the sudoku
                continue
            else:
                counter=0
                for i in range(9):   # Check the Column of the Sudoku
                    if j!=a[i][aa]:
                        counter+=1
                    if counter==9:
                        ad=int(aa/3)                        
                        ae=int(ab/3)
                        counter=0
                        for t in range(ad*3,ad*3+3):   # Check the grid of the Sudoku
                            for k in range(ae*3,ae*3+3):
                                if j!=a[k][t]:
                                    counter+=1
                        if counter==9:
                            ans.append(j)
        dict_for_ans[lst[x]]=ans 
    return dict_for_ans       

def place(a,b,c):
    d=int(a)
    e=d%10
    if int(d/10)==0:
        f=0
    else:
        f=int(d/10)
    c[f][e]=b[0]  # Place the value in the sudoku
    return c


b=Find_unsolve_dic(a)
c=Find_ans_dic(b)
d=a
x=c.keys()
y=c.values()
count=len(x)
var=count
final=len(x)
end=True

while end:
    for t,z,k in zip(x,y,range(count)):
        if len(z)==1:
            d=place(t,z,d)
            b=Find_unsolve_dic(d)
            c=Find_ans_dic(b)
            x=c.keys()
            y=c.values()
            count-=1
    if var==count:
        end=False
    else:
        var=count


b=Find_unsolve_dic(d)
c=Find_ans_dic(b)    
for i in range(9):
    print(f'{d[i][0]} {d[i][1]} {d[i][2]} | {d[i][3]} {d[i][4]} {d[i][5]} | {d[i][6]} {d[i][7]} {d[i][8]}')
    if i==2 or i==5:
        print(f'---------------------')