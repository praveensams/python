from flask import Flask, render_template
import re

app = Flask(__name__)

@app.route('/display/<word>')

def display(word):
   var=1
   s=open("/etc/passwd","r")
   for i in s.readlines():
      search = re.search(r'%s'%word,i)
      if search:
         var="yes"
   if var == 1:
      var=2
   return render_template('index.html',var=var,word=word)


if __name__ == '__main__':
   app.run('0.0.0.0',5000,debug=True)
