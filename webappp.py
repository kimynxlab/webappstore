from flask import Flask 

app = flask(__app__)


@app.route('/')
def hello_world():
    return 'Hello world' 


if __name__ == "__main__": 
    app.run() 
    