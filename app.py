from flask import Flask, render_template, request
import os

# Configuration

app = Flask(__name__)

# # testing:
# @app.route('/')
# def index():
#     return("hello world")

# Routes 
# homepage
@app.route('/')
def root():
    return render_template('index.html')


# employees
# @app.route('employees.html')
# def employees():
#     return render_template('./employees.html') 
    
# projects
# @app.route('./projects.html')
# def projects():
#     return render_template('./projects.html')

# clients
# @app.route('./clients.html')
# def employees():
#     return render_template('./clients.html')

# managers
# @app.route('./managers.html')
# def managers():
#     return render_template('./managers.html') 


# Listener

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 35562)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port)