from flask import Flask, render_template_string, request
import base64

app = Flask(__name__)
latest_image = ""

HTML = '''
<!DOCTYPE html>
<html><head><title>Vista Remota</title></head><body>
<h2>Captura en tiempo real</h2>
<img id="img" src="" width="100%" />
<script>
setInterval(() => {
    fetch("/latest").then(res => res.text()).then(data => {
        document.getElementById("img").src = "data:image/jpeg;base64," + data;
    });
}, 500);
</script>
</body></html>
'''

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/upload", methods=["POST"])
def upload():
    global latest_image
    latest_image = request.json['image']
    return "OK"

@app.route("/latest")
def latest():
    return latest_image

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
