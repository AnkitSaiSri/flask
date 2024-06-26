from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def homepage():
    return "<h2>Hello, Welcome to infinite possibilities<h2>"

@app.route("/welcome")
def welcome():
    return "you are most welcome to visit real estate expo"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/success/<int:score>")
def success(score):
    return "Your marks are "+ str(score) + " and you have passed :) "

@app.route("/fail/<int:score>")
def fail(score):
    return "Your marks are "+ str(score) + " and you have failed :( "

@app.route("/calculate",methods=["POST",'GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        avg_mk=(maths+science+history)/3
        result=''
        if avg_mk>=50:
            result='success'
        else:
            result='fail'
        #return redirect(url_for(result,score=avg_mk))
        return render_template('result.html',results=avg_mk)



if __name__=="__main__":
    app.run(debug=True)