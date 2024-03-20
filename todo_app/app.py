from flask import Flask, render_template, request, redirect
from todo_app.data.classes.ViewModel import ViewModel
from todo_app.data.trello_items import get_items, add_item, update_item_status
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.get('/')
def index_get():
    items = get_items()
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)

@app.post('/')
def index_post():
    item = request.form.get('item')
    add_item(item)
    return redirect("/")

@app.post('/update-item-status')
def update_item_status_post():
    id = request.form.get('id')
    new_status = request.form.get('new-status')
    update_item_status(id, new_status)
    return redirect("/")