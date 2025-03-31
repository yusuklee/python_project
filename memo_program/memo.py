import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title('메모장')
root.geometry('600x400')

text_area = tk.Text(root,wrap='char')
text_area.pack(expand=True,fill='both')

def open_file():
    file_path= filedialog.askopenfilename(
        defaultextension='.txt',
        filetypes=[('text','*.txt'),('all','*.*')])
    if file_path:
        try:
            with open(file_path,'r',encoding='utf-8')as file:
                content = file.read()
                text_area.delete(1.0,tk.END)
                text_area.insert(1.0,content)
        except Exception as e:
            messagebox.showerror(f"파일 저장 중 오류발생:\n{e}")
    
    

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text Files','*.txt'),('All Files','*.*')]
    )
    if file_path:
        try:
            with open(file_path,'w',encoding='utf-8')as file:
                content = text_area.get(1.0,tk.END)
                file.write(content)
        except Exception as e:
            messagebox.showerror('오류',f"파일 저장 중 오류 발생:\n{e}")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='파일',menu=file_menu)
file_menu.add_command(label='열기',command=open_file)
file_menu.add_command(label='저장',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='종료',command=root.quit)

root.config(menu=menu_bar)

root.mainloop()