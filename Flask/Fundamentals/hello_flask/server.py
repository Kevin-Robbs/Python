from ctypes.wintypes import INT
from flask import *  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following

def return_index():
    return render_template('index.html')

@app.route('/play/<num_divs>')          # The "@" decorator associates this route with the function immediately following

def return_play(num_divs):
    num_divs = int(num_divs)
    return render_template('div_game.html', times = num_divs)

@app.route('/play/<num_divs>/<div_color>')

def return_color(num_divs, div_color):
    num_divs = int(num_divs)
    return render_template('div_game.html', times = num_divs, my_color = div_color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

