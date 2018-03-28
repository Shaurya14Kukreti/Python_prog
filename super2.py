class Country():
  def __init__(self,count):
    print((count), 'is my country.')
    
class India(Country):
  def __init__(self):
    print('India is a beautiful country ')
    super().__init__('India')
    
d1 = India()
