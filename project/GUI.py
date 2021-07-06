import tkinter as tk
from tkinter import ttk

def click_me():
    # configure 함수로 속성을 변경 할 수 있음.
    action.configure(text = "** I have been Clicked! **") ## 버튼 텍스트 변경
    a_label.configure(foreground='red') ## 레이블 색상 변경
    a_label.configure(text = 'A Red Label') ##레이블 택스트 변경 

win = tk.Tk()

## 창 이름
win.title("Python GUI")

##레이블 추가
a_label = ttk.Label(win, text = "A Label")
a_label.grid(column = 0, row = 0)
##버튼 추가
action = ttk.Button(win, text = "Click Me!", command = click_me)
action.grid(column = 1 , row = 0)

win.mainloop()


# 창조절 win.resizable(False,False) Widtg, Height
