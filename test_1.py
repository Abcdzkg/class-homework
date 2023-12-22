from tkinter import filedialog
import xlrd
import tkinter as tk
from tkinter import ttk

#选择文件
def openfile():
    sfname = filedialog.askopenfilename(title='选择dat文件', filetypes=[('*.dat', '*.dat'), ('All Files', '*')])
    return sfname

"输入文件名，返回数据"
def read_data(sfname):  
    try:  
        # 读取表格数据  
        book = xlrd.open_workbook(sfname)  
        sheet1 = book.sheets()[0]  
        nrows = sheet1.nrows  
        print('表格总行数', nrows)  
        ncols = sheet1.ncols  
        print('表格总列数', ncols)  
  
        values = []  
        for i in range(nrows):  
            row_values = sheet1.row_values(i)  
            values.append(row_values)  
        return values  
    except Exception as e:  
        print("Error reading file:", e)  
        return None  

def showdata(frame,data):
    # 定义树状图表格函数
    '''
    frame:容器
    data：数据，数据类型为列表

    '''

    nrows = len(data)

    ncols = len(data[0])
    columns = [""]
    for i in range(ncols):
        columns.append(str(i))
    heading = columns

    """
        定义Treeview
        self.Frame2为父容器
        columns为列名集合
        show="headings"表示显示表头
    """
    tree = ttk.Treeview(frame, columns=columns, show="headings")


    # 定义各列列宽及对齐方式
    for item in columns:
        tree.column(item, width=50, anchor="center")

    tree.heading(heading[0], text=heading[0])  #第一列的表头为空

    # 定义表头
    for i in range(1, len(columns)):
        tree.heading(heading[i], text=str(i))



    # 设置表格内容
    i = 0
    for v in data:
        v.insert(0, i + 1)    #第一列的显示内容(序号)
        tree.insert('', i, values=(v))
        i += 1

    # 放置控件，rel*表示使用相对定位，相对于父容器的定位
    # tree.place(relx=0, rely=0, relwidth=1, relheight=1)

    return tree




#打开文件并以树状表格形式显示
def openshow():
    global  root
    filename=openfile()
    data=read_data(filename)
    tree=showdata(root,data)
    tree.place(relx=0.03,rely=0.2,relheight=0.7,relwidth=0.9)


def main():
    global root
    root = tk.Tk()
    root.title("打开文件")
    root.geometry("600x400")
    B1 = tk.Button(root, text="打开文件", command=openshow)
    B1.place(relx=0.03,rely=0.05)
    root.mainloop()



if __name__=='__main__':
    main()




