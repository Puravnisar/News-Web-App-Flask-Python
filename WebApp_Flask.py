#Purav Nisar
from flask import Flask, render_template 

    
@app.route("/Purav")
def Purav():
    return "Hello, Purav"
    
if __name__ == "__main__":
    app.run(debug=True)