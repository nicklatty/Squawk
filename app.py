from flask import Flask, request
import subprocess
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    photo_folder = os.path.join(app.static_folder, "photos")
    photo_files = [
        "photos/" + filename
        for filename in os.listdir(photo_folder)
        if filename.lower().endswith((".jpg", ".jpeg", ".png"))
        and not filename.endswith('_remix.jpg') and not filename.endswith('_remix.png')
    ]
    photo_files.sort()
    return render_template("about.html", photos=photo_files)


if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)


@app.route('/update', methods=['POST'])
def webhook():
    try:
        subprocess.Popen(['git', 'pull'], cwd='/home/squawkLYT/mysite')
        # Reload web app
        subprocess.Popen(
            ['touch', '/var/www/squawklyt_pythonanywhere_com_wsgi.py'])
        return 'Update triggered successfully.', 200
    except Exception as e:
        return f'Error: {str(e)}', 500
