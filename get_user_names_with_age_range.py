def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    ls2 = []
    ls = []
    a = range(min_age,max_age)
    for i in data:
        ls.append(i['age'])
    for i in ls:
        if i in a:
            ls2.append(i)
    x = ls.index(ls2[0])
    y = ls.index(ls2[1])
    return data[x]['name'], data[y]['name']
data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
min_age = 18
max_age = 25
print (get_user_names_with_age_range(data,min_age,max_age))