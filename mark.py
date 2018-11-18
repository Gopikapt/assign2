from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/student',methods=['GET','POST'])    
def Stud():
    if(request.method=='POST'):
        getname=(request.form['name'])
        getrno=request.form['regno']
        getsem=request.form['sem']
        getclg=request.form['clg']

        getsub1=request.form['sub1']
        getm1=int(request.form['m1'])
        gettm1=int(request.form['t1'])

        getsub2=request.form['sub2']
        getm2=int(request.form['m2'])
        gettm2=int(request.form['t2'])

        getsub3=request.form['sub3']
        getm3=int(request.form['m3'])
        gettm3=int(request.form['t3'])

        getsub4=request.form['sub4']
        getm4=int(request.form['m4'])
        gettm4=int(request.form['t4'])


    def grade(percent):
                if(percent>=90):
                        return 'A'
                elif(percent>=80):
                        return 'B'
                elif(percent>=70):
                        return 'C'
                elif(percent>=60):
                        return 'D'
                else:
                        return 'F'

        
    p1=(getm1/gettm1)*100
    p2=(getm2/gettm2)*100
    p3=(getm3/gettm3)*100
    p4=(getm4/gettm4)*100 

    g1=grade(p1)
    g2=grade(p2)
    g3=grade(p3)
    g4=grade(p4)

    if((g1!='F')and(g2!='F')and(g3!='F')and(g4!='F')):
            status=" Passed"
    else:
            status=" Failed"


    return render_template('student.html', getname=getname,getrno=getrno,getsem=getsem,getclg=getclg,getsub1=getsub1,getmark1=getm1,gettm1=gettm1,getsub2=getsub2,getmark2=getm2,gettm2=gettm2,getsub3=getsub3,getmark3=getm3,gettm3=gettm3,getsub4=getsub4,getmark4=getm4,gettm4=gettm4,g1=g1,g2=g2,g3=g3,g4=g4,status=status)

if(__name__=='__main__'):
    app.run(debug=True)

