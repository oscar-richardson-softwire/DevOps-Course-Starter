class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def not_started_items(self):
        item_is_not_started = lambda item : item.status == 'Not Started'
        not_started_items = list(filter(item_is_not_started, self._items))
        return not_started_items
    
    @property
    def done_items(self):
        item_is_done = lambda item : item.status == 'Done'
        done_items = list(filter(item_is_done, self._items))
        return done_items