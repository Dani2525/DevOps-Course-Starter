from todo_app.ViewModel import Item, ViewModel

item1 = Item('id-1', 'test1', 'To Do')
item2 = Item('id-2', 'test2', 'Done')
item3 = Item('id-3', 'test3', 'Done')
item4 = Item('id-4', 'test4', 'To Do')
item5 = Item('id-5', 'test5', 'To Do')

def test_done_items():
    items = [item1,item2,item3,item4,item5]
    view_model = ViewModel(items)
    done_items = view_model.done_items

    assert done_items == [item2,item3]