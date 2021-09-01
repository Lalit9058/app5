
from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__,template_folder='template')
b=[]
c= []
s = []
d = []
e =[]
f=[]
g=[]
h= []
t1 =[]
l =-1
t2 = []
per = []
stat = []
gra = []
@app.route("/")
def index():
  return render_template("index.html")


@app.route('/login',methods = ['POST', 'GET'])
def home():
    name = ''
    roll =''
    physics = ''
    chemistry = ''
    maths = ''
    english = ''
    physical = ''

    total =""
    total2 = ""
    percentage = ""
    grade = ""
    status = ""
    average = ''
    temp = ''

    
    global b
    global c
    global l
    global s
    global e
    global f
    global g
    global h
    global t1
    global t2 
    global per 
    global stat 
    global gra 
    # global d
    
    if request.method =='POST':
        name= request.form.get('name')
        roll = request.form.get('roll number')
        physics =request.form.get('physics mark') 
        chemistry =request.form.get('chemistry mark') 
        maths =request.form.get('maths mark') 
        english =request.form.get('english mark') 
        physical =request.form.get('physical mark') 
        total =float(request.form.get('total mark')) 
        total2 = float(physics) +float(chemistry) +float(maths) +float(english) +float(physical)
        temp = float(total2/(5*total))
        percentage= float(temp*100)
        average  = float(total2)/5
        if average >= 90:
          grade = 'A'
        elif average >= 80 and average < 90:
          grade = 'B'
        elif average >= 70 and average < 80:
          grade = 'C'
        elif average >= 60 and average < 70:
           grade = 'D'
        else:
           grade = 'E'
        if(percentage<33):
            status = "Fail"
        else:
            status = "Pass"
        l = l+1
        
        b.append(name)
        c.append(roll)
        s.append(physics)
        e.append(chemistry)
        f.append(maths)
        g.append(english)
        h.append(physical)
        # t1.append(total)
        t2.append(total2)
        per.append(percentage)
       
        gra.append(grade)
        stat.append(status)
        
        d.append(l)
        l = len(c)
       

    return render_template("login.html",t2 =t2,per = per,gra = gra,stat=stat ,c=c,b=b,g=g, d=d,s=s,e=e,h=h ,f=f,t1=t1)

	




if __name__ == "__main__":
    app.run(debug=True)

