from datetime import datetime, date
from flask import Flask

app = Flask(__name__)


def gettime():
    now = datetime.now()
    dt = str(datetime.now()) + "-00.00"
    d = str(date.today())
    t = (str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))

    json = {
        'datetime': dt,
        'date': d,
        'time': t
    }

    return json


@app.route("/")
def main():
    return gettime()
