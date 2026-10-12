from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
VIDEO_DIR = Path(app.static_folder) / "video"


@app.route("/")
def index():
    videos = sorted(path.name for path in VIDEO_DIR.glob("*.mp4"))
    return render_template("index.html", videos=videos)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
