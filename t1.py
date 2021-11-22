import tkinter as tk
import math

# 事件處理
def calculate_bmi_number():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi_value = round(weight / math.pow(height/100, 2), 2)
    result = '你的身高{}公分，體重{}公斤，BMI 指數為：{} {}'.format(height, weight, bmi_value, get_bmi_status_description(bmi_value))
    result_label.configure(text=result)

def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'
    
window = tk.Tk()
window.title('BMI App')
window.geometry('400x200')
#window.configure(background='white')

labelfont = ('times', 20, 'bold')
#widget = Label(root, text='Hello config world')
#widget.config(bg='black', fg='yellow')  
#widget.config(font=labelfont)  

header_label = tk.Label(window, text='BMI 計算器')
labelfont = ('times', 16, 'bold')
height_label = tk.Label(window, text='身高（公分）')
weight_label = tk.Label(window, text='體重（公斤）')
height_entry = tk.Entry(window)
weight_entry = tk.Entry(window)
result_label = tk.Label(window, text='')
calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number)


header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
height_label.grid(row=1, column=0, padx=5, pady=5)
weight_label.grid(row=2, column=0, padx=5, pady=5)
height_entry.grid(row=1, column=1, padx=5, pady=5)
weight_entry.grid(row=2, column=1, padx=5, pady=5)
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
calculate_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
