from tkinter import *
import mysql.connector

root=Tk()
root.title('database')
root.geometry('600x600')

current_label=[]

def clear_label():
     global current_label
     for label in current_label:
         label.destroy()
     current_label=[]

def show():
    global current_label
    clear_label()
    
    k=mysql.connector.connect(host="localhost",user="root",password="2000")
    v=k.cursor()
    v.execute("show databases")
    x=[z[0] for z in v]
    i=3
    z=0
    for j in range(len(x)):
        entry1=Entry(root,width=20)#
        entry1.insert(0,x[j])
        z=i+j
        entry1.grid(row=z,column=0,columnspan=1)
        current_label.append(entry1)
    
    label1=Label(root,text=' select the database to open',width=60)#
    label1.grid(row=z+1,column=0,columnspan=4)
    current_label.append(label1)

    i=z

    def opitionselect(x):
        global i
        global j
        
        
        
        k1=mysql.connector.connect(host="localhost",user="root",password="2000",database=clicked.get())
        v1=k1.cursor()
        v1.execute("show tables")
        x1=[m[0] for m in v1]
        i=z+3
        label2=Label(root,text=' select the table to open',width=60)#
        label2.grid(row=i+1,columnspan=4)
        current_label.append(label2)

        i=i+2
        
        def optiontable(x):
            global i
            global j
            global list1

            list1=[]
            f=LabelFrame(root,text='data in table')
            f.grid(row=20,columnspan=10)
            current_label.append(f)
            list1.append(f)
            
            k22=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
            v22=k22.cursor()
            v22.execute(f'desc {click.get()}')
            j=0
             
            for i in v22:
                #for j in range(len(i)):
                #print(7)
                entry=Entry(f,width=10)
                entry.grid(row=0,column=j)
                entry.insert(0,i[0])
                current_label.append(entry)
                list1.append(entry)
                #print(i)
                #print(entry)
                j=j+1

            k2=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
            v2=k2.cursor()
            v2.execute('select * from ' + click.get())
            result=v2.fetchall()
            x2=[xy for xy in result]
            j=1
            #g=[]
            
            '''print(x2)
            print(len(x2))
            print(len(x2[0]))'''
            
            for i in range(len(x2)):
                for k in range (len(x2[0])):                    
                    entry2=Entry(f,width=10)#
                    if not x2[i][k]:
                        entry2.insert(0,'none')
                        entry2.grid(row=j,column=k)
                        current_label.append(entry2)
                        list1.append(entry2)
                        #g.append(j)
                    else:
                        entry2.insert(0,x2[i][k])
                        entry2.grid(row=j,column=k)
                        current_label.append(entry2)
                        list1.append(entry2)
                        #g.append(j)
                j=j+1

                #print(current_label)

            #globals(['g'])
            '''f1=Frame(root)
            f1.grid(fill=BOTH,expand=1)
                
            mycanvas=Canvas(f1)
            mycanvas.grid(side=LEFT,fill=BOTH,expand=1)

            yscrollbar=ttk.Scrollbar(f1,orient=VERTICAL,command=my_canvas.yview)
            yscrollbar.GRID(side=RIGHT,fill=Y)

            mycanvas.configure(yscrollcommand=yscrollbar.set)
            mycanvas.bind('<configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

            myframe=Frame(mycanvas)

            mycanvas.create_window((0,0),window=myframe,anchor='nw')'''
            
            clear_d() 
        click=StringVar()
        click.set('select the table')
        options=[z for z in x1]
        table=OptionMenu(root,click,*options,command=optiontable)#
        table.grid(row=i+2,columnspan=4)
        current_label.append(table)
        i=i+3
        
    
    clicked=StringVar()
    clicked.set('select the database')
    option=[op for op in x]
    x=OptionMenu(root,clicked,*option,command=opitionselect)#
    x.grid(row=z+2,columnspan=4)
    current_label.append(x)

    #to clear the data
    def clear_d():
        def clear_data():
            for data in list1:
               data.destroy()
        label3=Label(root,text='clear table before seeing other table')
        clear=Button(root,text='clear data',padx=40,pady=10,command=clear_data)
            #print(g)
        label3.grid(row=100,columnspan=2)
        clear.grid(row=100,column=3)

        current_label.append(label3)
        current_label.append(clear)
    
    #current_label.extend([m,m1,m2,label1,click,clear,x,clicked,table])



            
current_entry = 0
x1=0
ja=[]
def insert1():
    global current_label
    clear_label()

    def create():

        def table_name(x):
            
            tablee_name=Label(root,text='enter the table name')
            table_entry=Entry(root,width=20)
            current_label.append(tablee_name)
            current_label.append(table_entry)
            
            tablee_name.grid(row=4,column=2)
            table_entry.grid(row=4,column=3)
            

            def next_1():
                

                def next_2():
                    list_column=[]
                    i=7
                    if  True:
                        label2=Label(root,text=f'enter the columnname and datatype')
                        label2.grid(row=i,columnspan=2)
                        current_label.append(label2)
                                
                        column_name1=Entry(root,width=20)
                        column_name1.grid(row=i,column=2)
                        current_label.append(column_name1)
                                
                        click=StringVar()
                        click.set('select datatype')
                        option=['int',
                               'varchar(20)',
                               'varchar(50)',
                               'varchar(100)',
                               'date',
                               'float']                  
                        option_bar2=OptionMenu(root,click,*option)
                        option_bar2.grid(row=i,column=3)
                        current_label.append(option_bar2)
     
                        def next_4():
             
                            label2.grid(row=i,columnspan=2)
                            list_column.append(column_name1.get())
                            list_column.append(click.get())
                            print(list_column)
                            click.set('select datatype')
                            column_name1.delete(0,END)


                            def finished():

                                list_column1=[]
                                for i in range(0,len(list_column),2):
                                    list_column1.append(f"{list_column[i]} {list_column[i+1]}")
                                list_column2=','.join(list_column1)
                                x=table_entry.get()
                                v=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                                k=v.cursor()
                                k.execute(f"create table {x} ({list_column2})")
                                k.close()

                                label_3=Label(root,text='table has sucessfully crated')
                                label_3.grid(row=10,columnspan=4)
                                current_label.append(label_3)

                              #crated to display the headings  
                                label_4=Label(root,text='enter the ddata to insert into table')
                                label_4.grid(row=11,columnspan=4)
                                current_label.append(label_4)
                                print(list_column)
                                
                                name=len(list_column)//2
                                print(name)
                                values=[]
                                print(values)
                                #global current_entry
                                #current_entry = 0
                                total_entry=name
                                #x=0
                                def data_entry1():
                                    global x1
                                    global current_entry
                                    entry=entry2.get()
                                    values.append(entry)
                                    entry2.delete(0,END)
                                    current_entry += 1
                                    
                                    if current_entry<total_entry:
                                        x1=x1+2
                                        label_name.config(text=f'enter the {list_column[x1]}')
                                        
                                    else:
                                        label_name.config(text='all the entrys are stored')
                                        entry2.config(state='disabled')
                                        button.config(state='disabled')
                                        current_entry=0
                                        print(values)
                                        
                                print(list_column)         
                                label_name=Label(root,text=f'enter the {list_column[0]}')
                                label_name.grid(row=12,columnspan=2)
                                current_label.append(label_name)

                                entry2=Entry(root,width=20)
                                entry2.grid(row=12,column=2)
                                current_label.append(entry2)

                                button=Button(root,text='enter',command=data_entry1)
                                button.grid(row=13,column=3 )
                                current_label.append(button)
                                     

                                def data_entry():
                                     v=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                                     k=v.cursor()
                                     column_name=[]
                                     values_name=[]
                                     for i in range(int(name)):
                                         column_name.append(list_column[i*2])
                                         values_name.append('%s')

                                     column_name1=','.join(column_name)
                                     values_name1=','.join(values_name)
                                         
                                     m=f"insert into {x} ({column_name1}) values ({values_name1})"
                                     print(m)
                                     print(values)
                                     v1=[int(x) if x.isdigit() else x for x in values]
                                     k.execute(m,v1)
                                     print(v1)
                                     v.commit()
                                     k.close()

                                     label=Label(root,text='data was successfully inserted')
                                     label.grid(row=20,columnspan=4)
                                     current_label.append(label)
                                

                                next_but=Button(root,text='finished',command=data_entry)
                                next_but.grid(row=30,column=1)
                                current_label.append(next_but)
     
                            next_but=Button(root,text='finished',command=finished)
                            next_but.grid(row=9,column=3)
                            current_label.append(next_but)

                        next_but=Button(root,text='next',command=next_4)
                        next_but.grid(row=9,columnspan=4)
                        current_label.append(next_but)
                     

                next_but=Button(root,text='next',command=next_2)
                next_but.grid(row=9,columnspan=4)
                current_label.append(next_but)
                

            next_but=Button(root,text='next',command=next_1)
            next_but.grid(row=9,columnspan=4)
            current_label.append(next_but)
                            
        
        
        k=mysql.connector.connect(host='localhost',user='root',password='2000')
        v=k.cursor()
        v.execute('show databases')

        clicked=StringVar()
        clicked.set('select database to create')
        options=[a[0] for a in v]
        #print(options)
        database=OptionMenu(root,clicked,*options,command=table_name)
        database.grid(row=4,column=0,columnspan=2)
        current_label.append(database)

    def insert():
        global current_label
        clear_label()
        def table_name(x):
            
            k1=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
            v1=k1.cursor()
            v1.execute(f'show tables')
            
            def data(d):
                 k22=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                 v22=k22.cursor()
                 v22.execute(f'desc {clicke.get()}')
                 ja=[]
                 
                 for i in v22:
                      ja.append(i[0:2])
                 x=len(ja)
                 print(ja)
                 print(x)
                 z=[]
                 def data_entry1():
                      global x1
                      global current_entry
                      entry=entry2.get()
                      z.append(entry)
                      entry2.delete(0,END)
                      current_entry += 1
                                     
                      if current_entry<x:
                          x1=x1+1
                          print(x1)
                          label_name.config(text=f'enter the {ja[x1]}')
                                         
                      else:
                          label_name.config(text='all the entrys are stored')
                          entry2.config(state='disabled')
                          button.config(state='disabled')
                          current_entry=0
                          x1=0
                          print(z)
                                    
                 print(z)
                 label_name=Label(root,text=f'enter the {ja[0]}')
                 label_name.grid(row=12,columnspan=2)
                 current_label.append(label_name)

                 entry2=Entry(root,width=20)
                 entry2.grid(row=12,column=2)
                 current_label.append(entry2)

                 button=Button(root,text='enter',command=data_entry1)
                 button.grid(row=13,column=3)
                 current_label.append(button)
                      
                 def data_entry():
                      v=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                      k=v.cursor()
                      column_name=[]
                      values_name=[]
                      
                      for i in range(int(x)):
                          column_name.append(ja[i][0])
                          values_name.append('%s')

                      column_name1=','.join(column_name)
                      values_name1=','.join(values_name)

                      print(column_name)
                                     
                      m=f"insert into {clicke.get()} ({column_name1}) values ({values_name1})"
                      print(m)
                      
                      v1=[int(x) if x.isdigit() else x for x in z]
                      print(v1)
                      k.execute(m,v1)
                      print(v1)
                      v.commit()
                      k.close()

                      label=Label(root,text='data was successfully inserted')
                      label.grid(row=20,columnspan=4)
                      current_label.append(label)
                             

                 next_but=Button(root,text='finished',command=data_entry)
                 next_but.grid(row=30,column=1)
                 current_label.append(next_but)



                 
            clicke=StringVar()
            clicke.set('select database to create')
            optio=[a[0] for a in v1]
            #print(options)
            databas=OptionMenu(root,clicke,*optio,command=data)
            databas.grid(row=4,column=3)
            current_label.append(databas)
            

        k=mysql.connector.connect(host='localhost',user='root',password='2000')
        v=k.cursor()
        v.execute('show databases')

        clicked=StringVar()
        clicked.set('select database to create')
        options=[a[0] for a in v]
        #print(options)
        database=OptionMenu(root,clicked,*options,command=table_name)
        database.grid(row=4,column=0,columnspan=2)
        current_label.append(database) 

        
    z=Button(root,text='create',command=create)
    z.grid(row=3,column=0)
    current_label.append(z)

    z1=Button(root,text='insert',command=insert)
    z1.grid(row=3,column=2)
    current_label.append(z1)


def alter():
    global current_label
    clear_label()
     
    def table_select(x):
        def add_column(y):

            label1=Label(root,text='adding a column')
            label1.grid(row=5,columnspan=1)
            current_label.append(label1)

            label2=Label(root,text='enter the column name')
            label2.grid(row=6,column=1)
            current_label.append(label2)

            entry=Entry(root,width=20)
            entry.grid(row=6,column=2)
            current_label.append(entry)

            def add(m):
                
                k2=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v2=k2.cursor()
                v2.execute(f'alter table {click.get()} add {entry.get()} {clic.get()}')
                v2.close()

                label2=Label(root,text='column was succesfully added')
                label2.grid(row=7,columnspan=4)
                current_label.append(label2)

            clic=StringVar()
            clic.set('enter datatype')
            opt=['int',
                'varchar(100)',
                'date',
                'float']
            datatype=OptionMenu(root,clic,*opt,command=add)
            datatype.grid(row=6,column=3)
            current_label.append(datatype)


            label3=Label(root,text='remove of column')
            label3.grid(row=7,column=0)
            current_label.append(label3)

            def remove_column(x):
                k3=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v3=k3.cursor()
                v3.execute(f'alter table {click.get()} drop column {cl.get()}')

                label4=Label(root,text='column was removed sucessfully')
                label4.grid(row=7,columnspan=4)
                current_label.append(label4)


            label5=Label(root,text=' update a row both num')
            label5.grid(row=8,column=0)
            current_label.append(label5)
            
            column_name=Entry(root,width=20)
            column_name.insert(0,'current column name')
            column_name.grid(row=9,column=0)
            current_label.append(column_name)

            column_name1=Entry(root,width=20)
            column_name1.insert(0,'changing row value')
            column_name1.grid(row=9,column=1)
            current_label.append(column_name1)

            column_name2=Entry(root,width=20)
            column_name2.insert(0,' column name')
            column_name2.grid(row=9,column=2)
            current_label.append(column_name2)

            column_name3=Entry(root,width=20)
            column_name3.insert(0,'current row value')
            column_name3.grid(row=9,column=3)
            current_label.append(column_name3)

            def update_row1():   

                k4=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v4=k4.cursor()
                v4.execute(f" update {click.get()} set {column_name.get()} = {column_name1.get()} where {column_name2.get()} = {column_name3.get()}")
                k4.commit()
                k4.close()

                label5=Label(root,text='row was sucessfully updated')
                label5.grid(row=10,columnspan=4)
                current_label.append(label5)

            button=Button(root,text='update',command=update_row1)
            button.grid(row=11,columnspan=4)
            current_label.append(button)

            label6=Label(root,text=' updating both string')
            label6.grid(row=20,column=0)
            current_label.append(label6)
            
            column_name4=Entry(root,width=20)
            column_name4.insert(0,'current column name')
            column_name4.grid(row=21,column=0)
            current_label.append(column_name4)

            column_name5=Entry(root,width=20)
            column_name5.insert(0,'changing row value')
            column_name5.grid(row=21,column=1)
            current_label.append(column_name5)

            column_name6=Entry(root,width=20)
            column_name6.insert(0,' column name')
            column_name6.grid(row=21,column=2)
            current_label.append(column_name6)

            column_name7=Entry(root,width=20)
            column_name7.insert(0,'current row value')
            column_name7.grid(row=21,column=3)
            current_label.append(column_name7)

            def update_row2():   

                k4=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v4=k4.cursor()
                v4.execute(f" update {click.get()} set {column_name4.get()} = '{column_name5.get()}' where {column_name6.get()} = '{column_name7.get()}'")
                k4.commit()
                k4.close()

                label7=Label(root,text='row was sucessfully updated')
                label7.grid(row=22,columnspan=4)
                current_label.append(label7)

            button=Button(root,text='update',command=update_row2)
            button.grid(row=23,columnspan=4)
            current_label.append(button)


            label8=Label(root,text=' updating string and int')
            label8.grid(row=12,column=0)
            current_label.append(label8)
            
            column_name8=Entry(root,width=20)
            column_name8.insert(0,'current column name')
            column_name8.grid(row=13,column=0)
            current_label.append(column_name8)

            column_name9=Entry(root,width=20)
            column_name9.insert(0,'changing row value')
            column_name9.grid(row=13,column=1)
            current_label.append(column_name9)

            column_name10=Entry(root,width=20)
            column_name10.insert(0,' column name')
            column_name10.grid(row=13,column=2)
            current_label.append(column_name10)

            column_name11=Entry(root,width=20)
            column_name11.insert(0,'current row value')
            column_name11.grid(row=13,column=3)
            current_label.append(column_name11)

            def update_row3():   

                k4=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v4=k4.cursor()
                v4.execute(f" update {click.get()} set {column_name8.get()} = '{column_name9.get()}' where {column_name10.get()} = {column_name11.get()}")
                k4.commit()
                k4.close()

                label9=Label(root,text='row was sucessfully updated')
                label9.grid(row=14,columnspan=4)
                current_label.append(label9)

            button=Button(root,text='update',command=update_row3)
            button.grid(row=15,columnspan=4)
            current_label.append(button)

            label10=Label(root,text=' updating int and string')
            label10.grid(row=16,column=0)
            current_label.append(label10)
            
            column_name12=Entry(root,width=20)
            column_name12.insert(0,'current column name')
            column_name12.grid(row=17,column=0)
            current_label.append(column_name12)

            column_name13=Entry(root,width=20)
            column_name13.insert(0,'changing row value')
            column_name13.grid(row=17,column=1)
            current_label.append(column_name13)

            column_name14=Entry(root,width=20)
            column_name14.insert(0,' column name')
            column_name14.grid(row=17,column=2)
            current_label.append(column_name14)

            column_name15=Entry(root,width=20)
            column_name15.insert(0,'current row value')
            column_name15.grid(row=17,column=3)
            current_label.append(column_name15)

            def update_row4():   

                k4=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v4=k4.cursor()
                v4.execute(f" update {click.get()} set {column_name12.get()} = {column_name13.get()} where {column_name14.get()} = '{column_name15.get()}'")
                k4.commit()
                k4.close()

                label11=Label(root,text='row was sucessfully updated')
                label11.grid(row=18,columnspan=4)
                current_label.append(label11)

            button=Button(root,text='update',command=update_row4)
            button.grid(row=19,columnspan=4)
            current_label.append(button)



            label12=Label(root,text=' deleting reference by number')
            label12.grid(row=24,columnspan=2)
            current_label.append(label12)
            
            column_name16=Entry(root,width=20)
            column_name16.insert(0,'column name')
            column_name16.grid(row=25,column=1)
            current_label.append(column_name16)

            column_name17=Entry(root,width=20)
            column_name17.insert(0,'row number')
            column_name17.grid(row=25,column=2)
            current_label.append(column_name17)

            def delete1():
                k4=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v4=k4.cursor()
                v4.execute(f"delete from {click.get()} where {column_name16.get()} = {column_name17.get()}")
                k4.commit()
                k4.close()

                label11=Label(root,text='row was sucessfully deleted')
                label11.grid(row=26,columnspan=4)
                current_label.append(label11)

            button=Button(root,text='delete',command=delete1)
            button.grid(row=27,columnspan=4)
            current_label.append(button)


            label12=Label(root,text='deleting reference by string')
            label12.grid(row=28,columnspan=2)
            current_label.append(label12)
            
            column_name18=Entry(root,width=20)
            column_name18.insert(0,'column name')
            column_name18.grid(row=29,column=1)
            current_label.append(column_name18)

            column_name19=Entry(root,width=20)
            column_name19.insert(0,'row string')
            column_name19.grid(row=29,column=2)
            current_label.append(column_name19)

            def delete2():
                k4=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v4=k4.cursor()
                v4.execute(f"delete from {click.get()} where {column_name18.get()} = '{column_name19.get()}'")
                k4.commit()
                k4.close()

                label11=Label(root,text='row was sucessfully deleted')
                label11.grid(row=30,columnspan=4)
                current_label.append(label11)

            button=Button(root,text='delete',command=delete2)
            button.grid(row=31,columnspan=4)
            current_label.append(button)


            k2=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
            v2=k2.cursor()
            print(click.get())
            v2.execute(f'desc {click.get()}')

            cl=StringVar()
            cl.set('select column name')
            op=[a[0] for a in v2 ]
            print(op)
            datatype=OptionMenu(root,cl,*op,command=remove_column)
            datatype.grid(row=7,column=3)
            current_label.append(datatype)
    
 
        k1=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
        v1=k1.cursor()
        v1.execute('show tables')
        
        click=StringVar()
        click.set('select table')
        option=[a[0] for a in v1]
        database1=OptionMenu(root,click,*option,command=add_column)
        database1.grid(row=4,column=2)
        current_label.append(database1)

    
    k=mysql.connector.connect(host='localhost',user='root',password='2000')
    v=k.cursor()
    v.execute('show databases')
     
    clicked=StringVar()
    clicked.set('select database')
    options=[a[0] for a in v]
    print(options)
    database=OptionMenu(root,clicked,*options,command=table_select)
    database.grid(row=4,column=0,columnspan=2)
    current_label.append(database)


def delete():
    global current_label
    clear_label()
            
    def table_name1(x):
        def table_name(x):
            def drop_table():

                k1=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
                v1=k1.cursor()
                #print(clicked.get())
                #print(click.get())
                v1.execute(f"drop table {click.get()}")
                k1.commit()
                v1.close()

                label=Label(root,text='sucessfully deleted')
                label.grid(row=5,columnspan=4)
                current_label.append(label)

            button=Button(root,text='delete',command=drop_table)
            button.grid(row=4,column=3)
            current_label.append(button)


        label1=Label(root,text='description of table',bg='red')
        label1.grid(row=6,column=0)
        current_label.append(label1)


        def desc():
            k2=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
            v2=k2.cursor()
            v2.execute(f'desc {click.get()}')
            j=7
            for i in v2:
                #print(7)
                entry=Entry(root,width=50)
                entry.grid(row=j,columnspan=4)
                entry.insert(0,i)
                current_label.append(entry)
                #print(i)
                #print(entry)
                j=j+1

        button1=Button(root,text='show',command=desc)
        button1.grid(row=6,column=3)
        current_label.append(button1)
        
            
        k1=mysql.connector.connect(host='localhost',user='root',password='2000',database=clicked.get())
        v1=k1.cursor()
        v1.execute('show tables')
        
        click=StringVar()
        click.set('select table')
        option=[a[0] for a in v1]
        #print(option)
        database1=OptionMenu(root,click,*option,command=table_name)
        database1.grid(row=4,column=2)
        current_label.append(database1)

    k=mysql.connector.connect(host='localhost',user='root',password='2000')
    v=k.cursor()
    v.execute('show databases')

    clicked=StringVar()
    clicked.set('select database to create')
    options=[a[0] for a in v]
    #print(options)
    database=OptionMenu(root,clicked,*options,command=table_name1)
    database.grid(row=4,column=0,columnspan=2)
    current_label.append(database)

    #current_label.extend([label,button,entry,button1,click,option,database,label])

#creating of main button
show=Button(root,text='show',padx=50,pady=10,command=show)
insert=Button(root,text='insert',padx=50,pady=10,command=insert1)
alter=Button(root,text='alter',padx=50,pady=10,command=alter)
delete=Button(root,text='delete',padx=50,pady=10,command=delete)

#placing on main buttons
show.grid(row=1,column=0)
insert.grid(row=1,column=1)
alter.grid(row=1,column=2)
delete.grid(row=1,column=3)
