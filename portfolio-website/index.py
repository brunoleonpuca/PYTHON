from flask import Flask , render_template

app = Flask(__name__, static_url_path='/static') 


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")