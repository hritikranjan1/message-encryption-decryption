from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        key = request.form["key"]
        mode = request.form["mode"]
        
        if mode == "e":
            result = encode(key, message)
        elif mode == "d":
            result = decode(key, message)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
