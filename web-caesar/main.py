
from flask import Flask, request
from caesar import rotate_string
#imports Flask class from flask module

app = Flask(__name__)
#app will be object created by constructor

app.config['DEBUG'] = True
#debug config for flask app is enabled

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            </style>
        </head>

                <body>
                <form method="post"/>
                    
                    
                    <label for="rot">Rotate by:</label>
                    <input name="rot" value="0" type="text"/>
                    <textarea type"text"{0} name="text"></textarea> 
                    
                <br>
                    <input type="submit">

            </form>
        </body>
    </html>
                    
                                 

"""

@app.route("/")

#creates mapping between path, "/" connects function is
#about to be defined

def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]
    encrypt_text = rotate_string(text=text, rot=rot)

    #encrypt_text = text.request(rotate_string)
    return "<h1>" + encrypt_text + "</h1>"          
#pass control to Flask object. Run function loops forever, 
#put this last. Acts out respsonbilities as web server,
#listens for requests and sending responses
app.run()


