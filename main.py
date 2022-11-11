from tkinter import *




root = Tk()
root.geometry('800x500+500+100')
root.title('Linear System Calculator')
root.iconbitmap('Images/1.ico')
root.minsize(300,300)


fr2= Frame(width='390',height='499',bg='white')
fr2.place(x=1,y=1)
fr1= Frame(width='390',height='499',bg='#CACFD2')
fr1.place(x=1,y=1)


lbl1=Label(fr1,text='Number Of Rows: ',fg='white',bg='#34495E')
lbl1.place(x=10,y=20)
lbl2=Label(fr1,text='Number Of Columns: ',fg='white',bg='#34495E')
lbl2.place(x=10,y=50)

en1=Entry(fr1,justify='center')
en1.place(x=150,y=20)
en2=Entry(fr1,justify='center')
en2.place(x=150,y=50)
en3=Entry(fr1,justify='center',width='40')
en3.place(x=10,y=100)
bt1=Button(fr1,text='Done',fg='white',bg='#34495E',width='7')
bt1.place(x=325,y=95)
bt1=Button(fr1,text='Add',fg='white',bg='#34495E',width='7')
bt1.place(x=260,y=95)


bt1=Button(fr1,text='Enter',fg='white',bg='#34495E',width='7')
bt1.place(x=300,y=20)
bt2=Button(fr1,text='Enter',fg='white',bg='#34495E',width='7')
bt2.place(x=300,y=50)

root.mainloop()

