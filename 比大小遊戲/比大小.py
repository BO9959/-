#模組
import tkinter
import tkinter.messagebox as msg
import random
import time

money =1000
a=0
def click_btn():
    
    cp = int(chips.get())
    
    global money
    if cp>money:
      exit()
    test=money-cp
    money=test
    text.delete("1.0",tkinter.END)
    text.insert("1.0","你目前的錢包有"+str(money)+"禁咒幣\n下注:"+str((int(cp)))+"\n下注後剩餘:"+str(int(test)))

    
      
   
    guide=[
       [0,0],
       [0,0]
    ]
    for y in range(2):
      for x in range(2):
        guide[y][x]=random.randint(1,6)     
        canvas.create_image( 200,500,image=img_dice[guide[0][1]])
        canvas.create_image( 800,500,image=img_dice[guide[1][0]])
    

    if guide[0][1]>guide[1][0]:
           bet.delete("1.0",tkinter.END)
           bet.insert("1.0","  "+"玩家贏")
           add = (cp*2)
           money = test + (add)
           wlt.delete("1.0",tkinter.END)
           wlt.insert("1.0","恭喜你贏得:"+str(add)+"幣\n目前共有:"+str(money)+"枚禁咒幣")

    if guide[0][1]<guide[1][0]:
           bet.delete("1.0",tkinter.END)
           bet.insert("1.0","  "+"莊家贏")
           money = test 
           wlt.delete("1.0",tkinter.END)
           wlt.insert("1.0","遺憾你輸了:"+str(int(cp))+"幣\n目前共有:"+str(money)+"枚禁咒幣")
         
    if guide[0][1]==guide[1][0]:
           bet.delete("1.0",tkinter.END)
           bet.insert("1.0","  "+"平手")
           money = test + cp
           wlt.delete("1.0",tkinter.END)
           wlt.insert("1.0","酷ㄟ平手 獲得:"+str(int(cp))+"幣\n目前共有:"+str(money)+"枚禁咒幣")
           
      


#介面設定    
root = tkinter.Tk()
root.title("比大小")
root.resizable(False,False)
canvas=tkinter.Canvas(root,width=1000,height=1000,bg="pink",bd=10)
canvas.pack()
#籌碼輸入
chips = tkinter.StringVar(None,'0')
ents = tkinter.Entry(root,width=30,textvariable=chips,bg="pink" )
ents.place(x=30,y=100)
#開始按鈕
button = tkinter.Button(text="擲骰子",font=("Times New Roman",24),bg="skyblue",command=click_btn)
button.place(x=450,y=300)
#骰子圖片
img_dice=[
  None,
  tkinter.PhotoImage(file="dice1.png"),
  tkinter.PhotoImage(file="dice2.png"),
  tkinter.PhotoImage(file="dice3.png"),
  tkinter.PhotoImage(file="dice4.png"),
  tkinter.PhotoImage(file="dice5.png"),
  tkinter.PhotoImage(file="dice6.png")
 ]
#顯示錢包字串與下注中
text = tkinter.Text(width=30,height=3,font=("Times New Roman",12),bg="pink",bd=5)
text.place(x=30,y=20)
bet = tkinter.Text( width=10,height=1,font=("Times New Roman",18),bg="pink",bd=5)
bet.place(x=450,y=500)
wlt = tkinter.Text(width=30,height=3,font=("Times New Roman",12),bg="pink",bd=5)
wlt.place(x=390,y=550)
root.mainloop()
