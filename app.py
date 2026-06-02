from flask import Flask, render_template
import os

app = Flask(__name__)  # ← nama variabelnya harus "app"

@app.route('/')
def index():
    return render_template('form.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
