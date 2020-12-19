from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import os
root = Tk()
#p1 = PhotoImage(file = "clear.png")
root.geometry('570x400')
root.title('QR_Code Generator')
root.configure(bg='blue')
#photo=PhotoImage(file='generatedqr.png')
#root.tk.call('wm','iconphoto',root._w,photo)
#root.iconbitmap('Translator.ico')
#####################################functions
def generate_qr():     #function for generate qr code
    qr_name = qr_name_entry_box.get()
    qr_id   = qr_id_entry_box.get()
    qr_message = qr_message_entry_box.get()
    #print(qr_name,qr_id,qr_message)
    message_qr = 'Name :'+qr_name+'\n' + 'id :'+qr_id+'\n'+'Message :'+qr_message
    #print(message_qr)
    url = pyqrcode.create(message_qr)
    #pp = r"/home/skillstarprince/Desktop/qrcode/"  #create path for qr code
    #l1 = os.listdir(pp)
    pp= os.path.abspath(r"allqr/qr_")
    cc = "{}{}{}.png".format(pp,qr_id,qr_name)   #create name of qr code
    l1=os.listdir(os.getcwd())
    if('{}{}.png'.format(qr_id,qr_name) in l1):
        messagebox.showinfo('Notification','Please Choose another id or name')
    else:
        url.png(cc,scale=10)  #size of qr code
        mm = "qr code saved as : "+qr_id+qr_name+'.png'
        qr_notification_message_label.configure(text = mm)
        res = messagebox.askokcancel('Notification','qr code is generated and want to see it then Yes:')
        if(res == True):
            top = Toplevel()
            top.geometry('400x400')  #declare size of new window
            top.configure(bg='white') #background colour for new window
            img = PhotoImage(file = cc)
            label1 = Label(top,image = img,bg='white')
            label1.place(x=10,y=10)   #size of qr code
            top.mainloop()




def clear_id_name():
    qr_id_entry_box.delete(0,'end')
    qr_message_entry_box.delete(0,'end')
    qr_name_entry_box.delete(0,'end')
    qr_notification_message_label.configure(text='')


def quit_root():
    res = messagebox.askokcancel('Notification','Are you sure you want to quit ?') #'res' is variable here
    if(res ==True):
        root.destroy()
    else:
        pass

############################### label
qr_id_label = Label(master=root,text='Enter your id:',bg='powder blue',fg='red',width=20,height =2,
                    font=('times',12,'italic bold'))
qr_id_label.place(x=10,y=20)

qr_name_label = Label(master=root,text='Enter your Name:',bg='powder blue',fg='red',width=20,height =2,
                    font=('times',12,'italic bold'))
qr_name_label.place(x=10,y=80)

qr_message_label = Label(master=root,text='Enter your Message:',bg='powder blue',fg='red',width=20,height =2,
                    font=('times',12,'italic bold'))
qr_message_label.place(x=10,y=140)


qr_notification_label = Label(master=root,text='Notification:',bg='powder blue',fg='red',width=20,height =2,
                    font=('times',15,'bold underline'))
qr_notification_label.place(x=10,y=350)

qr_notification_message_label = Label(master=root,text='',bg='powder blue',fg='red',width=30,height =2,
                    font=('times',15,'bold'))
qr_notification_message_label.place(x=250,y=350)
############################ entry boxes
qr_id_entry_box = Entry(master=root,width=23,bd=5,bg='pink',font=('times',15,'italic bold'))
qr_id_entry_box.place(x=250,y=20)

qr_name_entry_box = Entry(master=root,width=23,bd=5,bg='pink',font=('times',15,'italic bold'))
qr_name_entry_box.place(x=250,y=80)

qr_message_entry_box = Entry(master=root,width=23,bd=5,bg='pink',font=('times',15,'italic bold'))
qr_message_entry_box.place(x=250,y=140)
###########################button logo

generate_qrimage = PhotoImage(file="qrcode.png")
generate_qrimage = generate_qrimage.subsample(2,2)

clear_id_name_image= PhotoImage(file="rubber.png")
clear_id_name_image = clear_id_name_image.subsample(2,2)

quit_root_image = PhotoImage(file = 'close.png')
quit_root_image = quit_root_image.subsample(2,2)
######################### button
generate_qr_image_button= Button(master=root,text='Generate',width=100,font=('times',10,'bold'),bd=10,command= generate_qr,
                            activebackground='blue',bg='powder blue',image = generate_qrimage,compound = RIGHT)
generate_qr_image_button.place(x=10,y=250)

clear_id_name_button= Button(master=root,text='Clear',width=100,font=('times',10,'bold'),bd=10,command = clear_id_name,
                            activebackground='blue',bg='powder blue',image = clear_id_name_image,compound = RIGHT)
clear_id_name_button.place(x=210,y=250)

quit_root_button= Button(master=root,text='Quit',width=100,font=('times',10,'bold'),bd=10, command = quit_root,
                            activebackground='blue',bg='powder blue',image = quit_root_image,compound = RIGHT)
quit_root_button.place(x=410,y=250)


########################################Hover effects

def generate_qr_image_buttonenter(e):
    generate_qr_image_button['bg'] = 'purple2'

def generate_qr_image_buttonleave(e):
    generate_qr_image_button['bg'] = 'powder blue'

def clear_id_name_buttonenter(e):
    clear_id_name_button['bg'] = 'purple2'

def clear_id_name_buttonleave(e):
    clear_id_name_button['bg'] = 'powder blue'

def quit_root_buttonenter(e):
    quit_root_button['bg'] = 'purple2'

def quit_root_buttonleave(e):
    quit_root_button['bg'] = 'powder blue'




generate_qr_image_button.bind('<Enter>',generate_qr_image_buttonenter)
generate_qr_image_button.bind('<Leave>',generate_qr_image_buttonleave)

clear_id_name_button.bind('<Enter>',clear_id_name_buttonenter)
clear_id_name_button.bind('<Leave>',clear_id_name_buttonleave)

quit_root_button.bind('<Enter>',quit_root_buttonenter)
quit_root_button.bind('<Leave>',quit_root_buttonleave)

root.mainloop()
