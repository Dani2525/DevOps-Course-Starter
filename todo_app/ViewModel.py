class ViewModel :
     def __init__(self, alltodoitems) :
         self._todo = alltodoitems

     @property
     def my_item(self) :
         return self._todo   

     @property 
     def done_items(self):
         result = []
         for doneitem in self._todo:
             if doneitem.status == 'Done':
              result.append(doneitem)

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.title= name
        self.status = status
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
         