from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.get('/')
def index_get():
    items = get_items()
    return render_template('index.html', items=items)

@app.post('/')
def index_post():
    item = request.form.get('item')
    add_item(item)
    return redirect("/")
