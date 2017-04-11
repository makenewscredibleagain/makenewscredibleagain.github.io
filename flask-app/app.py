from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/app')
def input():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
	app.debug = True
	app.run()
	app.run(debug = True)
