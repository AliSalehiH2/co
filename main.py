#imports
import tkinter as tk
import customtkinter as cs
import codecs as cc
import xlsxwriter


#vars
Check=[]
TXT=[]
counter=[]
check_size_A=""
#def cheack box
def checkboxer():
    pass

class locator():
#locator.locator.arrange and create butttons
    def arrange(filepath,tab,com):
        f=cc.open(filepath , "r", "utf-8")
        A=f.readlines()
        count=len(A)
        Xcounter=1
        Ycounter=0
        if tab=="نوع":
            a=a
        else:
            for i in range (count):
                temp=A[i]
        
                temp=temp.replace("\r\n","")
                Bmaker (tab,temp,(com),(100),(10),1.05-((120/1200)*Xcounter),0.1+Ycounter)
                if i>0 and i%10==9:
                    Ycounter=Ycounter+0.1
                    Xcounter=1
                else:
                    Xcounter=Xcounter+1

#def checkbox creator
    def Cmaker(defult,tab,filepath,com):
        global check_size_A
        tv.add(tab)
        global Check
        f=cc.open(filepath , "r", "utf-8")
        A=f.readlines()
        count=len(A)
        
        Xcounter=1
        Ycounter=0
        
        for i in range (count):
            temp=A[i]
            temp=temp.replace("\r\n","")
            check_size_A = cs.StringVar(value=defult)
            
            check_A=cs.CTkCheckBox(tv.tab(tab) , text=temp ,command=checkboxer, variable=check_size_A, onvalue="on" , offvalue="off")
            check_A.place(relx=(1-((120/1200)*Xcounter)) , rely=0.1+Ycounter)
            Check.append(check_size_A)
            if i>0 and i%10==9:
                Ycounter=Ycounter+0.1
                Xcounter=1
            
                
            else:
                Xcounter=Xcounter+1
        check_size_A = cs.StringVar(value="off")
            
        check_A=cs.CTkCheckBox(tv.tab(tab) , text="ندارد" ,command=checkboxer, variable=check_size_A, onvalue="on" , offvalue="off")
        check_A.place(relx=(1-((120/1200)*Xcounter)) , rely=0.1+Ycounter)
        Check.append(check_size_A)
        Bmaker (tab,"ارسال",com,100,10,0.5,0.2+Ycounter)
        tv.set(tab)
        global counter
        counter.append(count+1)



#def button creator
def Bmaker (tab,txt,com,w,h1,x,y):
    b1= cs.CTkButton(tv.tab(tab), text=txt,command=com ,width=w ,height=h1)
    b1.place(relx=x, rely=y, anchor = tk.CENTER)

def Type_1_shir():
    locator.Cmaker("off","دسته4نوع","Data/valves/type 1.txt",sizeshir)
    
def brand_shir():
    locator.Cmaker("off","دسته3برند","Data/valves/manufacturer.txt",Type_1_shir)
def sizeshir():
    global Check
    locator.Cmaker("off","سایز","Data/valves/size.txt",feshar_shir)
   
def feshar_shir():
    global Check
    locator.Cmaker("off","فشار","Data/valves/pressure.txt",gate_material)
    
def gate_material():
    global Check
    locator.Cmaker("off","جنس‌زبانه‌یادریچه","Data/valves/gate material.txt",noe_shir)
text=str    
global textbox 
def noe_shir():
    global textbox
    global text
    tv.add("نوع")
    textbox = cs.CTkTextbox(tv.tab("نوع"))
    textbox.grid(row=1 , column=0 , padx=640 , pady=150)
    
    Bmaker("نوع", "ارسال",operatorshir,100,10,0.5,0.5)
    
    tv.set("نوع")
def operatorshir():
    global TXT
    global text
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    TXT.append(text)
    locator.Cmaker("off","عملگر","Data/valves/operator.txt",flangshir)
def flangshir():
    locator.Cmaker("off","فاصله فلنج","Data/valves/flange dis.txt",Ringshir)
def Ringshir():
    locator.Cmaker("off","رینگ","Data/valves/ring.txt",sealingshir)
def sealingshir():
    locator.Cmaker("off","آب‌بندی","Data/valves/sealing.txt",maxtempshir)
def maxtempshir():
    locator.Cmaker("off","حداکثردما","Data/valves/max temp.txt",bodymaterialshir)
def bodymaterialshir():
    locator.Cmaker("off","جنس‌بدنه","Data/valves/body material.txt",type3shir)
def type3shir():
    global text
    global textbox
    tv.add("مدل")
    textbox = cs.CTkTextbox(tv.tab("مدل"))
    textbox.grid(row=1 , column=0 , padx=640 , pady=150)
    
    Bmaker("مدل", "ارسال",connectionshir,100,10,0.5,0.5)
    tv.set("مدل")
def connectionshir():
    global TXT
    global text
    global textbox
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    TXT.append(text)
    locator.Cmaker("off","اتصال","Data/valves/connection.txt",holecountshir)
def holecountshir():
    locator.Cmaker("off","سوراخ کاری","Data/valves/hole count.txt",finishershir)
def oanda(filepath,allcount,pl,pc,alphabet,fornot,ty):
    global worksheet
    global p21
    global p22
    global p23
    global p24
    global p15
    global p16
    global p17
    global p18
    global p19
    global p110
    global p111
    global p112
    global p113
    global p114
    global p5
    global p6
    p1_1=[]
    f=cc.open(filepath, "r", "utf-8")
    A=f.readlines()
    xcounter=1
    if pl[-1] !="on" :
        ad=0
        for ii in range(len(pl)):
                if pl[ii]=="on":
                    temp=A[ii]
                    temp=temp.replace("\r\n","")
                    p1_1.append(temp)
        if ty==1:
          for ii in range(len(p1_1)):
                for i in range(int(allcount/pc)):
                    w=alphabet+str(xcounter)
                    worksheet.write(w,p1_1[ii])
                    w=w.replace(str(xcounter),str(xcounter+1))
                    xcounter=xcounter+1
        if ty==2:
            for i in range(p21*p22):
                
                for ii in range(int(allcount/p21/p22)):
                
                    w=alphabet+str(xcounter)
                    worksheet.write(w,p1_1[ad])
                    w=w.replace(str(xcounter),str(xcounter+1))
                    xcounter=xcounter+1
                if (ad+1)==len(p1_1):
                    ad=0
                else:
                    ad=ad+1
        if ty==3:
            
           
    
            
            for i in range(p21*p22*p23):
                for ii in range(int(allcount/p21/p22/p23)):

                    w=alphabet+str(xcounter)
                
     
                   
                    worksheet.write(w,p1_1[ad])
                    w=w.replace(str(xcounter),str(xcounter+1))
             
                    xcounter=xcounter+1
                if (ad+1)==len(p1_1):
                    ad=0
                else:
                    ad=ad+1
               
                
        if ty==4:
            ad1=0
       
            ff=cc.open("Data/valves/pressure.txt", "r", "utf-8")
            AA=ff.readlines()
            p1_2=[]
            for ii in range(len(p5)):
                if p5[ii]=="on":
                    temp=AA[ii]
                    temp=temp.replace("\r\n","")
                    p1_2.append(temp)
            if p5[-1]!="on":
                B1=1
            ff2=cc.open("Data/valves/gate material.txt", "r", "utf-8")
            AA2=ff2.readlines()
            p1_3=[]
            for ii in range(len(p6)):
                if p6[ii]=="on":
                    temp=AA2[ii]
                    temp=temp.replace("\r\n","")
                    p1_3.append(temp)
            if p6[-1]!="on":
                B=1
            ad2_1=0
            ad2_2=0

            for ii in range(int(allcount)):
                if (ad+1)==len(p1_1):
                    ad=0
                    ad1=ad1+1
                    
                    ad2_1=ad2_1+1
                    if ad2_1==p16:
                        ad2_1=0
                        ad2_2=ad2_2+1
                    if ad1==p15:
                        ad1=0
                   
                elif(ii!=0):
                    ad=ad+1
                
                w=alphabet+str(xcounter)
                w2="I"+str(xcounter)
                w3="J"+str(xcounter)
                if B1==1:

                    worksheet.write(w2,p1_2[ad1])
                worksheet.write(w,p1_1[ad])
                if B==1:
                    if ad2_2%2==0:

                        worksheet.write(w3,p1_3[ad2_1])
                    else:
                        worksheet.write(w3,p1_3[-(ad2_1)-1])
                w=w.replace(str(xcounter),str(xcounter+1))
                w2=w2.replace(str(xcounter),str(xcounter+1))
                w3=w3.replace(str(xcounter),str(xcounter+1))
                xcounter=xcounter+1

    if fornot =="f":
        close()
def close():
    global workbook
    workbook.close()
f=cc.open("Data/valves/counter.txt", "r", "utf-8")
A=f.readline()
temp=A[0]
temp=temp.replace("\r\n","")
workbook = xlsxwriter.Workbook("Shir"+temp+".xlsx")
worksheet = workbook.add_worksheet()
f.close()
f=cc.open("Data/valves/counter.txt" , "w", "utf-8")
f.write(str(int(temp)+1))
f.close()
#var c

p21=0
p22=0
p23=0
p24=0
p15=0
p16=0
p17=0
p18=0
p19=0
p110=0
p111=0
p112=0
p113=0
p114=0

p5=[]
p6=[]
def finishershir():
    global Check
    global TXT
    global workbook
    global worksheet
    global p21
    global p22
    global p23
    global p24
    global p15
    global p16
    global p17
    global p18
    global p19
    global p110
    global p111
    global p112
    global p113
    global p114
    global p5
    global p6
    #deviding cheker for shir
    global counter
    Check2=[]
    for i in range(len(Check)):
        Check2.append(Check[i].get())
    print(Check2)
    p1=[]
    p21=0
    for i in range(counter[0]):
        p1.append(Check2[0])
        Check2.pop(0)
        if p1[i]=="on":
            p21=p21+1
    if p1[-1]=="on":
        p21=1
    if p21==0 :
        p21=1
    p2=[]
    p22=0
    for i in range(counter[1]):
        p2.append(Check2[0])
        Check2.pop(0)
        if p2[i]=="on":
            p22=p22+1
    if p2[-1]=="on":
        p22=1
    if p22==0 :
        p22=1
    p3=[]
    p23=0
    for i in range(counter[2]):
        p3.append(Check2[0])
        Check2.pop(0)
        if p3[i]=="on":
            p23=p23+1
    if p3[-1]=="on":
        p23=1
    if p23==0 :
        p23=1
    p4=[]
    p24=0
    for i in range(counter[3]):
        p4.append(Check2[0])
        Check2.pop(0)
        if p4[i]=="on":
            p24=p24+1
    if p4[-1]=="on":
        p24=1
    if p24==0 :
        p24=1
    
    p5=[]
    p15=0
    for i in range(counter[4]):
        p5.append(Check2[0])
        Check2.pop(0)
        if p5[i]=="on":
            p15=p15+1
    if p5[-1]=="on":
        p15=1
    if p15==0 :
        p15=1
    p6=[]
    p16=0
    for i in range(counter[5]):
        p6.append(Check2[0])
        Check2.pop(0)
        if p6[i]=="on":
            p16=p16+1
    if p6[-1]=="on":
        p16=1
    if p16==0 :
        p16=1
    p7=[]
    p17=0
    for i in range(counter[6]):
        p7.append(Check2[0])
        Check2.pop(0)
        if p7[i]=="on":
            p17=p17+1
    if p7[-1]=="on":
        p17=1
    if p17==0 :
        p17=1
    p8=[]
    p18=0
    for i in range(counter[7]):
        p8.append(Check2[0])
        Check2.pop(0)
        if p8[i]=="on":
            p18=p18+1
    if p8[-1]=="on":
        p18=1
    if p18==0 :
        p18=1
    p9=[]
    p19=0
    for i in range(counter[8]):
        p9.append(Check2[0])
        Check2.pop(0)
        if p9[i]=="on":
            p19=p19+1
    if p9[-1]=="on":
        p19=1
    if p19==0 :
        p19=1
    p10=[]
    p110=0
    for i in range(counter[9]):
        p10.append(Check2[0])
        Check2.pop(0)
        if p10[i]=="on":
            p110=p110+1
    if p10[-1]=="on":
        p110=1
    if p110==0 :
        p110=1
    p11=[]
    p111=0
    for i in range(counter[10]):
        p11.append(Check2[0])
        Check2.pop(0)
        if p11[i]=="on":
            p111=p111+1
    if p11[-1]=="on":
        p111=1
    if p111==0 :
        p111=1
    p12=[]
    p112=0
    for i in range(counter[11]):
        p12.append(Check2[0])
        Check2.pop(0)
        if p12[i]=="on":
            p112=p112+1
    if p12[-1]=="on":
        p112=1
    if p112==0 :
        p112=1
    p13=[]
    p113=0
    for i in range(counter[12]):
        p13.append(Check2[0])
        Check2.pop(0)
        if p13[i]=="on":
            p113=p113+1
    if p13[-1]=="on":
        p113=1
    if p113==0 :
        p113=1
    p14=[]
    p114=0
    for i in range(counter[13]):
        p14.append(Check2[0])
        Check2.pop(0)
        if p14[i]=="on":
            p114=p114+1
    if p14[-1]=="on":
        p114=1
    if p114==0 :
        p114=1
    templ=[]
    print(TXT)
    templ2=[]
    temp=TXT[0]
    temp2=""
    for ii in range(len(temp)):
        if (temp[ii]+temp[ii-1]==".."):
            templ.append(temp2)
            temp2=""
        elif(temp[ii]!="."):
            temp2=temp2+str(temp[ii])
    temp=TXT[1]
    temp2=""
    for ii in range(len(temp)):
        if (temp[ii]+temp[ii-1]==".."):
            templ2.append(temp2)
            temp2=""
        elif(temp[ii]!="."):
            temp2=temp2+str(temp[ii]) 
    
    p1_1=[]
    f=cc.open("Data/valves/material.txt", "r", "utf-8")
    A=f.readlines()
    for ii in range(len(p1)):
        if p1[ii]=="on":
            temp=A[ii]
            temp=temp.replace("\r\n","")
            p1_1.append(temp)
    if len(templ)==0:
        templ.append("1")
    if len(templ2)==0:
        templ2.append("2")
    c=(p21*p22*p23*p24*p15*p16*p17*p18*p19*p110*p111*p112*p113*p114*len(templ)*len(templ2))
    
    for i in range (int(c)):
        w="A"+str(i+1)
        worksheet.write(w,"شیرآلات")
    oanda("Data/valves/material.txt",c,p1,p21,"B",1,2)
    oanda("Data/valves/manufacturer.txt",c,p2,p22,"C",1,1)
    oanda("Data/valves/type 1.txt",c,p3,p23,"H",1,3)
    oanda("Data/valves/size.txt",c,p4,p24,"G",1,4)
  
    oanda("Data/valves/operator.txt",c,p7,p17,"L",1,1)
    oanda("Data/valves/flange dis.txt",c,p8,p18,"M",1,1)
    oanda("Data/valves/ring.txt",c,p9,p19,"N",1,1)
    oanda("Data/valves/sealing.txt",c,p10,p110,"O",1,1)
    oanda("Data/valves/max temp.txt",c,p11,p111,"P",1,1)
    oanda("Data/valves/body material.txt",c,p12,p112,"Q",1,1)
    oanda("Data/valves/connection.txt",c,p13,p113,"S",1,1)
    oanda("Data/valves/hole count.txt",c,p14,p114,"T",'f',1)
   

    
    


            
#defs 2
def shir():
    locator.Cmaker("off","دسته2(اصلی)","Data/valves/material.txt",brand_shir)



#sys setting
cs.set_appearance_mode("System")
cs.set_default_color_theme("blue")

#frames
app=cs.CTk()
app.title("صفحه اصلي")
app.geometry("1500x800")
#Tables and Layers
tv =cs.CTkTabview(master=app , width=1500 , height=800)
tv.pack(padx=0, pady=0)
tv.add("دسته1(اصلی)")


#T1 Buttons
locator.arrange("Data/cat.txt","دسته1(اصلی)",shir)

app.mainloop()


