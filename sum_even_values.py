def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    sum=0
    for i in data.values():
        if i%2==0:
            sum+=i
    return sum

data = {
    1: 23, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 4
  }
print(sum_even_values(data))