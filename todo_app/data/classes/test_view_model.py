from todo_app.data.classes.Item import Item
from todo_app.data.classes.ViewModel import ViewModel

def test_view_model_not_started_items_property_returns_items_with_status_not_started():
    # Arrange
    view_model_and_filtered_items = create_view_model_with_not_started_and_done_items()
    view_model = view_model_and_filtered_items['view_model']
    not_started_items = view_model_and_filtered_items['not_started_items']

    # Act 
    result = view_model.not_started_items

    # Assert
    assert result == not_started_items

def test_view_model_done_items_property_returns_items_with_status_done():
    # Arrange
    view_model_and_filtered_items = create_view_model_with_not_started_and_done_items()
    view_model = view_model_and_filtered_items['view_model']
    done_items = view_model_and_filtered_items['done_items']

    # Act 
    result = view_model.done_items

    # Assert
    assert result == done_items

def create_view_model_with_not_started_and_done_items():
    item_1 = Item('1', 'Test item 1', 'Not Started')
    item_2 = Item('2', 'Test item 2', 'Done')
    item_3 = Item('3', 'Test item 3', 'Not Started')
    item_4 = Item('4', 'Test item 4', 'Done')

    items = [item_1, item_2, item_3, item_4]

    view_model = ViewModel(items)

    not_started_items = [item_1, item_3]
    done_items = [item_2, item_4]

    return {
        'view_model': view_model,
        'not_started_items': not_started_items,
        'done_items': done_items
    }



