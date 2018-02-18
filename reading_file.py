from flask import Flask

app = Flask(__name__)


@app.route('/read')

def read():
   s=open("/etc/passwd","r")
   s=s.readlines()
   s=str(s)
   return "%s" %s


if __name__ == '__main__':
   app.run('0.0.0.0',5000,debug=True)
