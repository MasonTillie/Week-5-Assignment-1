from contextlib import redirect_stderr
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    favorites = ['Hip-Hop', 'Rock', 'NBA', 'NFL', 'Games'] 
    return render_template('home.html', names=favorites)

@app.route('/hiphop')
def hiphop():
    hiphopArtist = ['Kendrick Lamar - To Pimp A Butterfly', 'Biggie Smalls - Ready to Die', 'Westside Gunn - Pray for Paris', 'Pusha T - Daytona', 'MF DOOM - Operation DOOMsday']
    return render_template('hiphop.html', hhartist=hiphopArtist)
    
@app.route('/rock')
def rock():
    rockArtists = ['Alice in Chains - Dirt', 'Blink 182 - Enema Of The State', 'Green Day - Dookie', 'Tennis - Swimmer', 'Black Sabbath - Paranoid']
    return render_template('rock.html', rArtist=rockArtists)

@app.route('/nfl')
def nfl():
    nflPlayers = ['Michael Vick QB #7 - Atlanta Falcons', 'LaDanian Tomlinson RB #21 - San Diego Chargers', 'Julio Jones #11 - Atlanta Falcons', 'Warren Sapp DT #99 - Tampa Bay Succaneers', 'Antonio Cromartie CB #31 - San Diego Chargers']
    return render_template('nfl.html', fbPlayers=nflPlayers)

@app.route('/nba')
def nba():
    nbaPlayers = ['Carmelo Anthony SF #7 - New York Knicks', 'Allen Iverson SG #3 - Philadelphia 76ers', 'Kareem Abdul-Jabbar C #33 - Los Angeles Lakers', 'Luka Doncic PG #77 - Dallas Mavericks', 'DeMarcus Cousins C #15 - Sacramento Kings']
    return render_template('nba.html', bbPlayers=nbaPlayers)

@app.route('/games')
def games():
    favoriteGames = ['God of War 3', 'Grand Theft Auto V', 'Apex Legends', 'NBA 2k', 'WWE Smackdown vs Raw 2006']
    return render_template('games.html', favgames=favoriteGames)
