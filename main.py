from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    title = 'My Flask App'
    name = 'Home'
    return render_template('home.html', title=title, name=name)
    


@app.route('/events')
def events():
    title = 'Events'
    name = 'Events'
    return render_template('events.html', title=title, name=name)

@app.route('/search')
def search():
    title = 'Search Results'
    name = 'Search Results'
    query = request.args.get('query')
    return render_template('search.html', title=title, name=name, query=query)

if __name__ == '__main__':
    app.run()
