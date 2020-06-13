from flask import Flask, render_template, request, flash, redirect, url_for
import re
import API_Key
import json
from urllib.request import urlopen

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.form['name'] == '':
        flash("Field can't be in blank", 'error')
        return redirect(url_for('index'))
    else:
        movie = request.form['name']
        list = SearchMovie(movie)

        try:
            if list.data['Response']:
                flash("No results found, try another name", 'error')
                return redirect(url_for('index'))
        except:
            pass
    return render_template('results.html', list=list, keyword=movie)


@app.route('/moredetails/<imdbid>', methods=['GET', 'POST'])
def more_details(imdbid):
    list = get_full_description(imdbid)
    return render_template('moredetails.html', list=list)


class SearchMovie:
    def __init__(self, movie):
        movie = str(re.sub(' ', '+', movie)).lower().strip()
        self.get_movie(movie)

    def get_movie(self, movie):
        data = f'http://www.omdbapi.com/?s={movie}&apikey={API_Key.API_key}'
        response = urlopen(data)

        # Convert bytes to string type and string type to dict
        string = response.read().decode('utf-8')
        self.data = json.loads(string)
        if self.data['Response'] == "True":
            self.data = self.data['Search']
        return self.data


def get_full_description(imdbid):
    full_data = f'http://www.omdbapi.com/?i={imdbid}&plot=full&apikey={API_Key.API_key}'
    response = urlopen(full_data)

    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    full_data = json.loads(string)
    return full_data


if __name__ == '__main__':
    app.run()
