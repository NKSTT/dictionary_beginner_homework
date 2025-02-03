def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    dict_value = data.values()
    return max(dict_value)
data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }
print (find_max_value(data=data))