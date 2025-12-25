from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Basit bir HTML şablonu
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Müzik Arama</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #f4f4f4; }
        .song { background: white; margin: 10px auto; padding: 15px; width: 50%; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        img { border-radius: 4px; }
    </style>
</head>
<body>
    <h1>🎵 iTunes Müzik Arama</h1>
    <form method="GET" action="/">
        <input type="text" name="search" placeholder="Sanatçı veya şarkı..." value="{{ term }}">
        <button type="submit">Ara</button>
    </form>
    <hr>
    {% for track in tracks %}
    <div class="song">
        <img src="{{ track.artworkUrl100 }}" alt="Cover">
        <h3>{{ track.trackName }}</h3>
        <p>{{ track.artistName }}</p>
        <audio controls src="{{ track.previewUrl }}"></audio>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    term = request.args.get("search", "Tarkan")
    url = f"https://itunes.apple.com/search?term={term}&entity=song&limit=10"
    response = requests.get(url)
    tracks = response.json().get("results", [])
    return render_template_string(HTML_TEMPLATE, tracks=tracks, term=term)

if __name__ == "__main__":
    # Docker içinde çalışması için host='0.0.0.0' olmalı
    app.run(host='0.0.0.0', port=5000)
