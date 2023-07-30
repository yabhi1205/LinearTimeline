from tkinter import *
import time
abhi = {"canvas_width": 1200, "canvas_height": 500, }


dots=[0,100,150,200,300,1500,1000,800,700]


root = Tk()
root.geometry("1300x720")
# root.attributes('-fullscreen', True)
root.state('zoomed') 
myCanvas = Canvas(root, width=abhi["canvas_width"],
                  height=abhi["canvas_height"], bg="green")

h_line = myCanvas.create_line(
    0, abhi["canvas_height"]/2, abhi["canvas_width"], abhi["canvas_height"]/2, fill="#ffff99", width=2)
h_line = myCanvas.create_line(
    0, abhi["canvas_height"]/2, abhi["canvas_width"]//2, abhi["canvas_height"]/2, fill="#ffff99", width=4)


# vline = myCanvas.create_line(
#     abhi['canvas_width']//2,0,abhi['canvas_width']//2,abhi['canvas_height']
# )


def shift():
    global after_id
    # myCanvas.move("all",-.5,0)
    for i in temp:
        myCanvas.move(i[0],-.5,0)  
        myCanvas.move(i[1],-.5,0)  
        myCanvas.move(i[2],-.5,0)  
        coords = myCanvas.coords(i[0])
        # print(coords)
        if (coords[0]+coords[2])/2<(abhi['canvas_width']/2):
            myCanvas.itemconfig(i[1],fill="white")
    # myCanvas.move(innercircle,-.5,0)
    after_id = root.after(10,shift)
    button['state']=DISABLED
    delete['state']=NORMAL

def delete():
    global my_canvas
    delete['state']=DISABLED
    button['state']=NORMAL
    root.after_cancel(after_id)


temp,up=[],False
for i in dots:
    outercircle = myCanvas.create_oval((abhi['canvas_width']//2)-10+i,(abhi['canvas_height']//2)-10,(abhi['canvas_width']//2)+10+i,(abhi['canvas_height']//2)+10,width=2,outline="white")
    innercircle = myCanvas.create_oval((abhi['canvas_width']//2)-5+i,(abhi['canvas_height']//2)-5,(abhi['canvas_width']//2)+5+i,(abhi['canvas_height']//2)+5,width=0)
    circletext = myCanvas.create_text((abhi['canvas_width']//2)+i,(abhi['canvas_height']//2)+(25 if up else -25),text="Abhinav",fill="white")
    up=not(up)
    temp.append([outercircle,innercircle,circletext])


# for i in dots:
button = Button(root,text="Click This",bg="grey",fg="white",command=shift)
button.grid(row=1,column=0)
delete = Button(root,text="Delete This",bg="grey",fg="white",command=delete,state=DISABLED)
delete.grid(row=2,column=0)
myCanvas.grid(row=0, column=0,padx=100,pady=30)

root.mainloop()
