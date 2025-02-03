def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    count = 0
    dict_data = data.keys()
    for item in dict_data:
        if type(item) == int:
            count += 1
    return count
data = {
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
  }
print (find_int_keys(data=data))