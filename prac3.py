
# coding: utf-8

# # Introduction to Artificial Intelligence for Non Computing

# ## Practical 3 (weeks 5 - 6)

# The following links provide additional information about data analysis , machine learning and Numpy

# Python data analysis: https://www.imooc.com/learn/843
# machine learning: https://www.imooc.com/learn/717
# Numpy :https://www.imooc.com/learn/943

# #### Theory Questions

# 1\.Which of the following are true and which are false? Give brief explanations.
# - a. In a fully observable, turn-taking, zero-sum game between two perfectly rational players,it does not help the first player to know what strategy the second player is using—that is, what move the second player will make, given the first player's move.
# - b. In a partially observable, turn-taking, zero-sum game between two perfectly rational players, it does not help the first player to know what move the second player will make, given the first player's move.
# - c. A perfectly rational backgammon agent never loses.
# 
# See textbook Chapter6 24.6

# 
# a is true, b,c are false. Since in zero-sum game it does not help the first player to know what strategy the second player is using and not to predict. However, in a partially observable game, knowing the second player’s move tells the first player additional information about the game state that would otherwise be available only to the second player. The interests of all parties are mutually antagonistic. In order to gain the upper hand in the game and gain more benefits, they do not want the other party to understand their own solutions to the problem and guess the countermeasures they choose. Therefore, the outcome of the game is always uncertain.
# ***

# 2\.Define in your own words the terms constraint, backtracking search, arc consistency,backjumping, min-conflicts, and cycle cutset.
# 
# See textbook Chapter6 6.16

# constraint：A constraint is a restriction on the possible values of two or more variables
# The backtracking search starts from a starting state along a path, either reaching the goal or reaching the dead end. If it reaches the dead end, it goes back to the nearest node on the path that has not yet analyzed the sibling. This backtracking idea is applied to other algorithms. 
#  arc consistency: If for all values x in the current domain of vi, there is a value y in the current domain of vj such that vi=x and vj=y are allowed by the constraint between vi and vj, then the arc (vi, vj) is The arc is consistent.
#  backjumping is a technique that reduces search space, therefore increasing efficiency. While backtracking always goes up one level in the search tree when all values for a variable have been tested, backjumping may go up more levels. 
#  min-conflicts: Given an initial assignment of values to all the variables of a CSP, the algorithm randomly selects a variable from the set of variables with conflicts violating one or more constraints of the CSP.Then it assigns to this variable the value that minimizes the number of conflicts. If there is more than one value with a minimum number of conflicts, it chooses one randomly. This process of random variable selection and min-conflict value assignment is iterated until a solution is found or a pre-selected maximum number of iterations is reached.
#  cycle cutset: A cycle cutset is a set of variables which when removed from the constraint graph make it acyclic . When the variables of a cycle cutset are instantiated the remainder of the CSP can be solved in linear time.
# 
# 
# ***

# 3\.Explain why it is a good heuristic to choose the variable that is most constrained but the value that is least constraining in a CSP search.
# 
# See textbook Chapter6 6.9

# The most constrained variable makes sense because it chooses a variable that can cause failure (all other conditions are the same) and it is more efficient to fail as early as possible (thus pruning most of the search space). The least limit value heuristic is meaningful because it allows for the greatest opportunity for future allocations to avoid conflicts.
# ***

# 4\.Consider the following procedure for choosing moves in games with chance nodes: 
# - 1、Generate some dice-roll sequences (say, 50) down to a suitable depth (say, 8).
# - 2、With known dice rolls, the game tree becomes deterministic. For each dice-roll sequence,solve the resulting deterministic game tree using alpha-beta.
# - 3、Use the results to estimate the value of each move and to choose the best.Will this procedure work well? Why (or why not)?
# 
# See textbook Chapter5 5.19

# This process will give incorrect results. Mathematically, this process is equivalent to assuming that the average communicates with the minimum and maximum values, not. Intuitively, each player's choices made in the deterministic tree are based on a comprehensive understanding of future scorpions and are not necessarily related to actions without such knowledge.
# 
# ***

# 5\. Now,please consider this game:  there are three plates A, B and C, each plate has three bills. A puts 1, 20, 50; B puts 5, 10, 100; C puts 1, 5, 20. All units are "Yuan". There are two persons A and B, and two of them can check out three plates and banknotes .（ A is ourself, The other is B）
# The game is divided into three steps: 
# - 1、A select a plate from three plate.
# - 2、B take out two banknotes from A selected plate,and give the  banknotes to A.  
# - 3、A take one of the two banknotes, and take it away.among,A want to get the max banknotes, B want to let A to get the min.
# 
# Try to understand the minimax algorithm，you can click the link:https://blog.csdn.net/tangchenyi/article/details/22920031

# _your answer here..._ 
# 
# ***

# ### Programming Excercises

# 1\. Guess number(Single number): please generate a randomly number  with the function (random), then ask someone to guess the number,I think we should give the corresponding hint, otherwise it will be very difficult to guess the number.the game will be over untill you get the right number.

# In[ ]:


import random
random_number=random.randint(1,50)
 

print('我已经想好了一个1到50之间的数字')
#设定参数
n=0
is_guess=1
while(is_guess):    
    guess_number=int(input('猜一猜吧，是多少:'))
    n=n+1
    if guess_number==random_number:
        print('恭喜你，猜对了,',name,'! 你共猜了 ',n,'次。')
        is_guess=0
    if guess_number>random_number:
        print('你猜的数太高了.')
    if guess_number<random_number:
        print('你猜的数太低了.')


# 2\.if you had understand the guess single number games,Congratulates,next is the guess three number games,Maybe you can do it well.But this is a different way of thinking. 
# first : we need generate three numbers,there are most ten times chances give  you to guess the number,of course,we also give you some cue.
# 
# - 'When I say:-->It means:
# - 'error--> The 3 numbers are not in the mystical numbers.'
# - 'Only the number is correct --> the number is right , but the position is not right.'
# - 'Absolutely right--> numbers is right and the position also right.'
# 
# Maybe it's better for you to understand the rule well through see the picture.
# <div style="float:left;" ><img src="img/p1.png" width="400" height="300" >

# In[4]:


import random
NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # Returns a random string numbers of non repeating that consisting of NUM_DIGITS .
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns a string that is completely correct, digitally correct and erroneous, used to prompt users.
    if guess == secretNum:
        return 'Congratulations!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Absolutely right')
        elif guess[i] != secretNum[i] and guess[i] in secretNum:
            clues.append('Only the number is correct')
        else:
            clues.append("error")
    return clues

print('there are  %s numbers，please Guess what it is.' % (NUM_DIGITS))
print('The clue I gave is:')
print('When I say:                     It means:')
print('error                           The 3 numbers are not in the mystical numbers.')
print('Only the number is correct      the number is right , but the position is not right..')
print('Absolutely right                numbers is right and the position also right.')

while True:
    secretNum = getSecretNum()
    print('there are  %s numbers，You have  %s  chance to guess it.' % (NUM_DIGITS,MAX_GUESS))
    guessesTaken = 1
    #judge the game if continue.
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS:
            print()
            guess = input('This is the %s time: ' % (guessesTaken))
        print(getClues(guess, secretNum))
        guessesTaken += 1
        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You lost the game,the right answer is  %s.' % (secretNum))
    m = input('Do you want to play again? (yes or no)')
    if not m.lower().startswith('y'):
        break


# 3\.please try using Python's Tkinter to make a visual interface（GUI）.if you don't know anything.Maybe you can refer to the below interface.and implement it by code.
# 
# <div style="float:left;" ><img src="img/p2.png" width="200" height="200" >

# In[ ]:


import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

root = tk.Tk()  # 生成主窗口
root.title("窗体测试程序")   # 窗体名称
root.geometry("400x300")   # 指定窗体大小

label = ttk.Label(root, text="hello world")
label.pack()

# 事件
def click(event):
    messagebox.showinfo("hello world", "this is a some info")

button1 = tk.Button(root, text="tk-button")
button1.bind("<Button-1>", click)
button1.pack(side=tk.LEFT)

button2 = ttk.Button(root, text="ttk-button")
button2.bind("<Button-1>", click)
button2.pack(side=tk.RIGHT)

root.mainloop()  # 消息循环


# 4\.Through the initial trial of Tkinter,    please write a simple calculator.
# 
# <div style="float:left;" ><img src="img/p3.png" width="180" height="200" center="left"></div>
# <div style="float:left;" ><img src="img/p4.png" width="180" height="200" center="right" ></div>

# In[8]:


import tkinter
import tkinter.messagebox
import math
root = tkinter.Tk()
root.title('简易计算器')
root.minsize(350,400)
# 设置菜单
# 设置总菜单
allmenu = tkinter.Menu()

# 添加子菜单
look = tkinter.Menu(tearoff = 0)  # 查看
edit = tkinter.Menu(tearoff = 0)  # 编辑
help = tkinter.Menu(tearoff = 0)  # 帮助
auther = tkinter.Menu(tearoff = 0)# 作者

'''
向子菜单中添加选项卡未作！！！！
'''
# 将子菜单加入总菜单
allmenu.add_cascade(menu = look, label = '查看')
allmenu.add_cascade(menu = edit, label = '编辑')
allmenu.add_cascade(menu = help, label = '帮助')
allmenu.add_cascade(menu = auther, label = '作者')

# 摆放总菜单
root.config(menu = allmenu)

# 文本输入框
v = tkinter.StringVar()
v.set('0')
label = tkinter.Label(textvariable = v, bg = 'white',font =('黑体',20),
                       bd = 5, anchor = 'se')
label.place(x = 30, y = 15, width = 290, height = 60)

# 声明一个用于保存运算过程的容器
operationlist = []

# 声明一个是否按下运算符号的变量
ispresssign = False

# 声明一个是否按下等于键的变量
ispressflag = False

# 声明一个是否允许按下'.'键的变量
isdot = True

# 按下数字的函数
def pressnum(num):
    # 全局化变量
    global ispresssign
    global operationlist
    global ispressflag
    global isdot
    # 判断是否按下等于键
    if ispressflag == True:
        # 将数字归0
        v.set('0')
        # 重置判断符
        ispressflag = False
    # 判断是否按下运算的符号
    if ispresssign == True:
        # 将数字归0
        v.set('0')
        # 重置运算符
        ispresssign = False

    # 获取面板原有数字
    oldnum = v.get()
    # 判断原数字是否为0
    if oldnum == '0':   # 直接显示按下的数字
        if num == '.' and isdot == True:
            v.set('0' + '.')
            isdot = False
        else:
            v.set(num)

        # 判断是否按下1/x键
        if num == '1/x':
            if oldnum == '0':
                v.set('除数不能为0')
            else:
                result = 1 / float(oldnum)
                v.set(result)

        # 判断是否按下撤销键（ ← 键）
        if num == '←':
            operationlist.clear()
            v.set('0')
    else:  # 将原数字与当前数字拼和
        # 判断是否按下正负号
        if num == '±':
            if oldnum.startswith('-'):
                v.set(oldnum[1:])
            else:
                v.set('-' + oldnum)

        else:
            v.set(oldnum + num)

        # 判断是否按下撤销键（ ← 键）
        if num == '←':
            if len(oldnum) == 1:
                v.set('0')
            else:

             v.set(oldnum[:-1])

        # 判断是否按下根号键
        if num == '√':
            result = math.sqrt(float(oldnum))
            v.set(result)

    # 判断是否按下了清空键 （C 或者CE键）
    if num == 'C' or num == 'CE':
        operationlist.clear()
        v.set('0')

# 按下运算符号的函数
def presssign(sign):
    # 全局化变量
    global ispresssign
    global operationlist
    global isdot

    if ispresssign == True:
        operationlist[-1] = sign
    else:
         # 获取页面中的原有数字
        oldnum = v.get()
        # 将页面原有数字保存到列表中
        operationlist.append(oldnum)
        # 保存运算符号
        operationlist.append(sign)
        # 设置按下运算符的标志
        ispresssign = True
    isdot = True

# 按下等号的函数
def pressequal():
    # 全局化
    global operationlist
    global ispressflag
    # 获取界面中的数字
    oldnum = v.get()
    if oldnum == '0' and '/' in operationlist:
        operationlist.clear()
        v.set('除数不能为0')
        ispressflag = True
    else:
    # 将列表中的运算组合到一起
        operationlist.append(oldnum)
    #print(operationlist)

    # 将列表中的步骤组合成字符串使用eval运算
        result = eval(''.join(operationlist))

    # 显示结果
        v.set(result)

    # 清空运算列表
        operationlist.clear()
        ispressflag = True

# 按钮
btnchexiao = tkinter.Button(text = '←', command = lambda : pressnum('←'))
btnchexiao.place(x = 30, y = 90, width = 50, height = 40)

btnCE = tkinter.Button(text = 'CE', command = lambda : pressnum('C'))
btnCE.place(x = 90, y = 90, width = 50, height = 40 )

btnC = tkinter.Button(text = 'C', command = lambda :pressnum('CE'))
btnC.place(x = 150, y = 90, width = 50, height = 40 )

btnflag = tkinter.Button(text = '±', command = lambda : pressnum('±'))
btnflag.place(x = 210, y = 90, width = 50, height = 40 )

btngen = tkinter.Button(text = '√', command = lambda : pressnum('√'))
btngen.place(x = 270, y = 90, width = 50, height = 40 )

btn7 = tkinter.Button(text = '7', command = lambda : pressnum('7'))
btn7.place(x = 30, y = 140, width = 50, height = 40 )

btn8 = tkinter.Button(text = '8', command = lambda : pressnum('8'))
btn8.place(x = 90, y = 140, width = 50, height = 40 )

btn9 = tkinter.Button(text = '9', command = lambda : pressnum('9'))
btn9.place(x = 150, y = 140, width = 50, height = 40 )

btnchu = tkinter.Button(text = '/',command = lambda : presssign('/'))
btnchu.place(x = 210, y = 140, width = 50, height = 40 )

btnyu = tkinter.Button(text = '%', command = lambda : presssign('%'))
btnyu.place(x = 270, y = 140, width = 50, height = 40 )

btn4 = tkinter.Button(text = '4', command = lambda : pressnum('4'))
btn4.place(x = 30, y = 190, width = 50, height = 40 )

btn5 = tkinter.Button(text = '5', command = lambda : pressnum('5'))
btn5.place(x = 90, y = 190, width = 50, height = 40 )

btn6 = tkinter.Button(text = '6', command = lambda : pressnum('6'))
btn6.place(x = 150, y = 190, width = 50, height = 40 )

btncheng = tkinter.Button(text = '*', command = lambda : presssign('*'))
btncheng.place(x = 210, y = 190, width = 50, height = 40 )

btndao = tkinter.Button(text = '1/x', command = lambda : pressnum('1/x'))
btndao.place(x = 270, y = 190, width = 50, height = 40 )

btn1 = tkinter.Button(text = '1', command = lambda : pressnum('1'))
btn1.place(x = 30, y = 240, width = 50, height = 40 )

btn2 = tkinter.Button(text = '2', command = lambda : pressnum('2'))
btn2.place(x = 90, y = 240, width = 50, height = 40 )

btn3 = tkinter.Button(text = '3', command = lambda : pressnum('3'))
btn3.place(x = 150, y = 240, width = 50, height = 40 )

btnjian = tkinter.Button(text = '-', command = lambda : presssign('-'))
btnjian.place(x = 210, y = 240, width = 50, height = 40 )

btndeng = tkinter.Button(text = '=', command = pressequal)
btndeng.place(x = 270, y = 240, width = 50, height = 90 )

btnling = tkinter.Button(text = '0', command = lambda : pressnum('0'))
btnling.place(x = 30, y = 290, width = 110, height = 40 )

btndot = tkinter.Button(text = '.', command = lambda : pressnum('.'))
btndot.place(x = 150, y = 290, width = 50, height = 40 )

btnjia = tkinter.Button(text = '+', command = lambda : presssign('+'))
btnjia.place(x = 210, y = 290, width = 50, height = 40 )

def look():
    tkinter.messagebox.showinfo(title = '嘿嘿嘿～～',message = '想得美，滚蛋滚蛋！！')

btnlook = tkinter.Button(text = '点击查看源代码', bg = 'black', fg = 'white', bd = 5, command = look)
btnlook.place(x = 90, y = 350, width = 170, height = 30)


root.mainloop()


# this is a step:how to install the matplotlib,you can reference this link:https://blog.csdn.net/not_give_up_/article/details/79058272
# 1. Ball Class
#     draw is responsible for moving Ball
#     Collision detection, bounce, Ball detection of Paddle 
# 2. Paddle Class
#     draw is responsible for moving Paddle
#     Collision detection to determine whether or not to continue ,Monitor keyboard events
# 3. main cycle
#     Drawing the Ball and Paddle

# In[11]:


from tkinter import *
import random
import time
 
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        startx = [-3, -2, -1, 1, 2, 3]
        random.shuffle(startx)
        self.x = startx[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)#top-left bottom-right
        if (pos[1] <= 0 or self.hit_paddle(pos) == True):
            self.y = -self.y
        if (pos[0] <= 0 or pos[2] >= self.canvas_width):
            self.x = -self.x
        if (pos[3] >= self.canvas_height):
            self.hit_bottom = True
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]):
            if (pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
                return True
        return False
 
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.x = 0
        self.canvas.move(self.id, 200, 300)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<Key-Left>", self.turn_left)
        self.canvas.bind_all("<Key-Right>", self.turn_right)
    def draw(self):
        pos = self.canvas.coords(self.id)
        if (pos[0] + self.x >= 0 and pos[2] + self.x <= self.canvas_width):
            self.canvas.move(self.id, self.x, 0)
        #self.x = 0
    def turn_left(self, event):
        self.x = -4
    def turn_right(self, event):
        self.x = 4
 
 
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)#not resizable
tk.wm_attributes("-topmost", 1)#at top
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()#init
 
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
 
 
while 1:
    if (ball.hit_bottom == False):
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


