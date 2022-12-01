from flask_login import current_user
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

     @property
     def user_role(self):
        return current_user.role     

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.title= name
        self.status = status
    

         