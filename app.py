from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    stats = {
        'location': 'Austin, TX (Tesla HQ)',
        'status': 'Has not read the poem yet',
        'tweets': 0,
        'reads': 0,
        'reading_speed': 0,
        'time_until': '∞',
        'recent_activities': [
            'Elon tweeted about Cybertruck instead of reading poem',
            'Posted 5 SpaceX memes while poem remained unread',
            'Changed Twitter name to "X" but still hasn\'t read poem',
            'Discussed Mars colonization without acknowledging poem'
        ]
    }
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
