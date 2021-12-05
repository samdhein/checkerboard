from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def rowcount(num=8):
    return render_template("index.html", num=int(num/2))	# return num 

@app.route('/<int:num>/<int:num2>')
def rowscolumns(num=8, num2=8):
    return render_template("index.html", num=int(num/2), num2=int(num2/2))	# return num and num2 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.