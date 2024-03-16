from flask import Flask, render_template, request, redirect
from todo_app.data.trello_items import get_items, add_item, complete_item
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

@app.post('/complete-item')
def complete_item_post():
    id = request.form.get('id')
    complete_item(id)
    return redirect("/")