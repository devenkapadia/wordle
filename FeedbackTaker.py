from tkinter import *
import tkinter.messagebox as tmsg


def main():
    root = Tk()
    root.geometry("455x233")
    root.title("Feedback")
    root.config(bg="#292F3F")
    root.iconbitmap('fbicon.ico')

    def feedback(t):
        print(f"Thank you for your feedback")
        t.destroy()
        tmsg.showinfo("Feedback recieved!", f"Thank you for your feedback")
        with open("Feedback.txt","a") as f:
            f.write(f"Feedback recieved : {myslider2.get()}\n")
            f.write(f"Remarks: {other.get()}\n")

    # myslider = Scale(root, from_=0, to=100)
    # myslider.pack()
    txt = "Give your feedback here:"
    Label(root, text=txt.upper() ,bg="#8CD4C9",padx=8,font="Vardana 10 bold").pack(pady=8)
    myslider2 = Scale(root,bg="grey", from_=0, to=10, orient=HORIZONTAL, tickinterval=5)
    myslider2.set(9)
    myslider2.pack(pady=5)

    Label(root,text="Anything else you want to mention".upper(),bg="#8CD4C9",font="Vardana 10 bold",padx=20).pack(pady=10)
    other = StringVar()
    # other.set("None")
    other_fb = Entry(root,textvariable=other).pack(fill=X,padx=20,pady=5)

    Button(root, text="Rate",bg="#8CD4C9",font="Vardana 9 bold", pady=4,height=1,width=8, command=lambda : feedback(root)).place(x=155,y=190)
    Button(root, text="Back",bg="#8CD4C9",font="Vardana 9 bold", pady=4,height=1,width=8, command=lambda : root.destroy()).place(x=240,y=190)

    root.mainloop()

if __name__ == '__main__':
    main()