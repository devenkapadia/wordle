from FeedbackTaker import main
from  tkinter import ttk
from wordle3 import *
from wordle4 import *
from wordle5 import *

str = "string"

def play(t):
    t.destroy()

    def scoreSort():
        sc = Tk()
        sc.title('High Scores')
        sc.geometry('250x150')
        sc.config(bg='#292F3F')
        game_frame = Frame(sc, bg="#292F3F")
        game_frame.pack()
        style = ttk.Style(game_frame)
        # style.theme_use("clam")
        style.theme_use("alt")
        # style.theme_use("vista")
        # style.theme_use("default")
        style.configure("Treeview",
                        background="#292F3F",
                        foreground="White",
                        fieldbackground="#292F3F"
                        )
        my_game = ttk.Treeview(game_frame)
        my_game['columns'] = ('Rank', 'player_name', 'Attemps', 'min', 'sec')

        my_game.column("#0", width=0, stretch=NO)
        my_game.column("Rank", anchor=CENTER, width=40)
        my_game.column("player_name", anchor=CENTER, width=70)
        my_game.column("Attemps", anchor=CENTER, width=55)
        my_game.column("min", anchor=CENTER, width=40)
        my_game.column("sec", anchor=CENTER, width=40)

        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("Rank", text="Id", anchor=CENTER)
        my_game.heading("player_name", text="Name", anchor=CENTER)
        my_game.heading("Attemps", text="Attemps", anchor=CENTER)
        my_game.heading("min", text="min", anchor=CENTER)
        my_game.heading("sec", text="sec", anchor=CENTER)

        wb = load_workbook('score.xlsx')
        global n
        temp = clicked.get()
        n = temp[9]
        global str
        if (int(n) == 5):
            ws = wb.worksheets[0]
        elif (int(n) == 4):
            ws = wb.worksheets[1]
        else:
            ws = wb.worksheets[2]

        r = ws.max_row
        l1 = []
        for i in range(2, r + 1):
            l2 = []
            for j in range(2, 5):
                c = ws.cell(row=i, column=j).value
                l2.append(c)
            l1.append(l2)
        print(r - 1)
        k = 0
        if (r < 6):
            while (k < r - 1):
                a = 6
                m = 60
                s = 60
                p = 0
                for i in range(len(l1)):
                    if int(l1[i][0]) == a:
                        if int(l1[i][1]) == m:
                            if int(l1[i][2]) <= s:
                                a = int(l1[i][0])
                                p = i
                                m = int(l1[i][1])
                                s = int(l1[i][2])
                        elif int(l1[i][1]) < m:
                            a = int(l1[i][0])
                            p = i
                            m = int(l1[i][1])
                            s = int(l1[i][2])
                    elif int(l1[i][0]) < a:
                        a = int(l1[i][0])
                        p = i
                        m = int(l1[i][1])
                        s = int(l1[i][2])
                    else:
                        continue
                name = ws.cell(row=p + 2, column=1).value
                print(
                    f"Rank {k + 1} goes to {name} with completing game in {a} attempts in {m} minutes and {s} seconds")
                my_game.insert(parent='', index='end', text='',
                               values=(f"{k + 1}", f"{name}", f"{a}", f"{m}", f"{s}"))


                l1[p][0] = 7
                k = k + 1
        else:
            while (k < 5):
                a = 6
                m = 60
                s = 60
                p = 0
                for i in range(len(l1)):
                    if int(l1[i][0]) == a:
                        if int(l1[i][1]) == m:
                            if int(l1[i][2]) <= s:
                                a = int(l1[i][0])
                                p = i
                                m = int(l1[i][1])
                                s = int(l1[i][2])
                        elif int(l1[i][1]) < m:
                            a = int(l1[i][0])
                            p = i
                            m = int(l1[i][1])
                            s = int(l1[i][2])
                    elif int(l1[i][0]) < a:
                        a = int(l1[i][0])
                        p = i
                        m = int(l1[i][1])
                        s = int(l1[i][2])
                    else:
                        continue
                name = ws.cell(row=p + 2, column=1).value
                print(
                    f"Rank {k + 1} goes to {name} with completing game in {a} attempts in {m} minutes and {s} seconds")
                my_game.insert(parent='', index='end', text='',
                               values=(f"{k + 1}", f"{name}", f"{a}", f"{m}", f"{s}"))

                l1[p][0] = 7
                k = k + 1
        Button(sc, text="Back", bg="light blue", font="Vardana 9", pady=4, height=1, width=6,
               command=lambda: sc.destroy()).place(x=100, y=100)
        my_game.pack()
        sc.mainloop()

    def start(t):
        global n
        temp = clicked.get()
        n = temp[9]
        global str
        if(int(n)==5):
            gamePlay5(t)
            str = returnStr5()

        elif(int(n)==4):
            gamePlay4(t)
            str = returnStr4()
        else:
            gamePlay3(t)
            str = returnStr3()
        endpage()

    def ins():
        ins = Tk()
        ins.title("How to Play")
        ins.iconbitmap("htp.ico")
        f2 = Frame(ins, bg="#292F3F", pady=10)
        lbl1 = Label(f2, text="Instructions :", bg="light blue", font="Helvetica 20 bold", pady=5)
        lbl1.pack()
        str2 = "1. You can choose the mode to play 3,4 or 5 letter wordle\n2. When the letter is available in the word and the position is also correct than the letter will be coloured green\n3. When the letter is available in the word and but the position is not correct than the letter will be coloured yellow\n4. When the letter is not available in the word, than it will be coloured black\n5. You will get 6 trials"
        rules = Label(f2, text=str2, bg="#8CD4C9", font="TimesNewRoman 15", justify="left")
        rules.pack(pady=8, padx=14)
        btn = Button(f2, text="Back", font="Vardana 12 bold", width=8, height=1, bg="#8CD4C9",
                     command=lambda: dest(ins))
        btn.pack()
        f2.pack()
        ins.mainloop()

    def dest(t):
        t.destroy()

    def endpage():
        # t.destroy()
        global str
        end = Tk()
        end.title("Thank you")
        end.iconbitmap('wordle.ico')
        end.config(bg="#292F3F")
        # end.geometry("300x300")
        f1 = Frame(width=250, height=100, bg="#292F3F")
        f1.pack(pady=10, padx=10)
        Label(f1, text="Game over!!", fg="black", font="Vardana 15").pack(pady=8)
        res = Label(f1, text=str, bg="#8CD4C9", fg="black", font="Vardana 12")
        res.pack(padx=5, pady=10)

        # Label(f1,text="Do you wanna play again???", bg="yellow",font="Vardana 15").pack(pady=10,padx=10)
        btn = Button(f1, text="OK", font="Vardana 12", width=8, height=1, bg="#8CD4C9",
                     command=lambda: play(end))
        btn.pack(padx=20, pady=10)
        end.mainloop()


    home = Tk()
    home.title("WORDLE")
    home.iconbitmap('wordle.ico')
    home.config(bg="#292F3F")
    home.geometry("230x350")
    # home.overrideredirect(True)
    f = Frame(home, bg="#292F3F", pady=10)

    clr = "#8CD4C9"
    clr2 = "#292F3F"
    clicked = StringVar()
    clicked.set("Letters: 5")
    mode = OptionMenu(f, clicked, "Letters: 5", "Letters: 4", "Letters: 3")
    mode.config(bg=clr,fg=clr2)
    btn = Button(f, text="Play", font="Vardana 12", width=8, height=1,fg=clr2, bg=clr, command=lambda:start(home))
    btn2 = Button(f, text="How to Play", font="Vardana 12", width=10, height=1,fg=clr2, bg=clr, command=lambda: ins())
    btn5 = Button(f, text="Best", font="Vardana 12", width=10, height=1,fg=clr2, bg=clr, command=lambda: scoreSort())
    btn3 = Button(f, text="Rate Us", font="Vardana 12", width=8, height=1, bg=clr,fg=clr2, command=lambda: main())
    btn4 = Button(f, text="Exit", font="Vardana 12", width=8, height=1, bg=clr,fg=clr2, command=lambda: home.destroy())

    # btn.place(x=110,y=350)
    mode.pack(pady=10)
    btn.pack(pady=10)
    btn2.pack(pady=10)
    btn5.pack(pady=10)
    btn3.pack(pady=10)
    btn4.pack(pady=10)
    f.pack(pady=10)
    home.mainloop()

if __name__ == '__main__':
    r = Tk()
    play(r)
    r.mainloop()