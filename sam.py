from flask import Flask, redirect, url_for, render_template
import subprocess

app = Flask(__name__)

@app.route('/today/<b>/<a>')
def hello(b,a):
   if b == "praveen":
      out = subprocess.Popen(['mkdir',"/tmp/%s"%a], stdout=subprocess.PIPE)
      output = out.communicate()[0]
  
      return "%s"%output
   else:
      return "improper input"


@app.route('/yesterday')
def yesterday():
   return redirect(url_for('hello',a="sam2",b="praveen"))

@app.route('/loading')
def loading():
   return render_template('index.html')


if __name__ == '__main__':
   app.run('0.0.0.0',5000,debug=True)
