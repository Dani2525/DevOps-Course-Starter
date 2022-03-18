

class ViewModel :
     def __init__(self, alltodoitems) :
         self._todo = alltodoitems

     @property
     def my_items(self) :
         return self._todo   

     @property 
     def done_items(self):
         result = []
         for doneitem in self._todo:
             if doneitem.status == 'Done':
              result.append(doneitem)
         return result

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.title= name
        self.status = status
         