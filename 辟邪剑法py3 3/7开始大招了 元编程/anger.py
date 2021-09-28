class User:
  def __init__(self):
    pass

  @property
  def name(self): 
    return "fxxk you {}".format(self.bossname) 

  @name.setter
  def name(self, name):
    self.bossname = name

  def __get__(self, instance, owner):
    return self.age
  

  def __set__(self, instance, value):
    self.age = value


    

if __name__ == "__main__":

  user = User()
  user2 = User()
  user.name = "Miles" 
  user2 = "60"
  print(user2)
  print(user.name)