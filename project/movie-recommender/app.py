from flask import Flask, render_template, request, session, redirect, url_for, flash
import pandas as pd
import requests

app = Flask(__name__)
app.secret_key = "cine_matrix_vault_99"

# --- OMDb CONFIG ---
OMDB_API_KEY = "8ffcf7f3" 
OMDB_URL = "http://www.omdbapi.com/"

# Load Dataset
try:
    movies = pd.read_csv('movies.csv')
except:
    movies = pd.DataFrame({'title': ['Inception'], 'genres': ['Action|Sci-Fi']})

def get_omdb_data(title, full_plot=False):
    clean_title = title.split(' (')[0].strip()
    params = {'t': clean_title, 'apikey': OMDB_API_KEY}
    if full_plot: params['plot'] = 'full'
    try:
        r = requests.get(OMDB_URL, params=params, timeout=2)
        return r.json()
    except:
        return {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form.get('username')
    session['watchlist'] = [] # Initialize empty watchlist
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session: return redirect('/')
    
    genre = request.args.get('genre')
    search = request.args.get('search')
    
    if search:
        results = movies[movies['title'].str.contains(search, case=False)].head(8)
    elif genre:
        results = movies[movies['genres'].str.contains(genre, case=False)].sample(min(8, len(movies)))
    else:
        results = movies.sample(8)

    movie_list = []
    for _, row in results.iterrows():
        data = get_omdb_data(row['title'])
        movie_list.append({
            'title': row['title'],
            'genre': row['genres'].replace('|', ' • '),
            'poster': data.get('Poster', 'https://via.placeholder.com/300x450?text=No+Poster')
        })
        
    return render_template('dashboard.html', movies=movie_list, user=session['username'], current_genre=genre)

@app.route('/movie/<path:title>')
def details(title):
    if 'username' not in session: return redirect('/')
    data = get_omdb_data(title, full_plot=True)
    return render_template('details.html', m=data, user=session['username'])

# --- WATCHLIST LOGIC ---
@app.route('/add_to_watchlist/<path:title>')
def add_to_watchlist(title):
    if 'username' not in session: return redirect('/')
    
    watchlist = session.get('watchlist', [])
    if title not in watchlist:
        watchlist.append(title)
        session['watchlist'] = watchlist
    
    return redirect(url_for('view_watchlist'))

@app.route('/watchlist')
def view_watchlist():
    if 'username' not in session: return redirect('/')
    
    watchlist_titles = session.get('watchlist', [])
    movie_details = []
    for title in watchlist_titles:
        data = get_omdb_data(title)
        movie_details.append({
            'title': data.get('Title', title),
            'poster': data.get('Poster'),
            'genre': data.get('Genre')
        })
    
    return render_template('watchlist.html', movies=movie_details, user=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
