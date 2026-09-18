class MyNumber:
  def __init__(self,value):
    self.value = 7

  def __abs__(self):
    """Return the absolute value.
    Matches: abs(number) -> number """
    return abs(self.value)
    
    print(abs.__doc__)

