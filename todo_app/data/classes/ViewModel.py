class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def not_started_items(self):
        not_started_items = [item for item in self._items if item.status == 'Not Started']
        return not_started_items
    
    @property
    def done_items(self):
        done_items = [item for item in self._items if item.status == 'Done']
        return done_items