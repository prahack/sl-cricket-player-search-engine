import flask
from search import search


app = flask.Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('search.html',
        original_input='Search here',
                                     result=None,
                                     ))
    if flask.request.method == 'POST':
        text = flask.request.form['name']
        print(text)
        result = search(text)
        return (flask.render_template('search.html',
                                     original_input=text,
                                     result=result,
                                     items = len(result)
                                     ))
if __name__ == '__main__':
    app.run()