import tkinter as tk  #调用工具箱并且重命名

words=[]
def on_add_click():
    print("按钮被点击了")
    word = word_entry.get()
    print(word)
    if word=="":
        print("请输入单词")
        return
    word_list.insert(tk.END, word)
    words.append(word)
    word_entry.delete(0, tk.END)


root=tk.Tk()   #Tk为工具箱中的一个创建主窗口的工具
root.title("我的单词记录本")
root.geometry("500x500") #初始化窗口像素大小
word_entry=tk.Entry(root)
word_entry.pack(pady=20,padx=8)
add_button=tk.Button(root,text="添加",command=on_add_click)
add_button.pack(pady=20,padx=8)
word_list = tk.Listbox(root)
word_list.pack(pady=20,padx=8)
root.mainloop()#表示窗口保持在桌面上,放最后写
