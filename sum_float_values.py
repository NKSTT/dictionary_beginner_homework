# def sum_float_values(data: dict) -> float:
#     '''
#     Return the sum of all float values in dictionary.
#     Args:
#         data (dict): A dictionary of values
#     Returns:
#         float: The sum of all float values in the dictionary.
#     '''
#     sum = 0
#     for i in data.values():
#         if type(i)==float:
#             sum += i
#     return sum
# data = {
#     1: 22.4, 
#     2: 3.5, 
#     4: 1, 
#     6: 7.6, 
#     5: 2, 
#     7: 3
#   }
# print(sum_float_values(data))

def quote(fighter):
    name = fighter.lower()
    a = "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    mc = 'conor mcgregor'
    gsp = 'george saint pierre'
    if name == mc:
        return a
    elif name == gsp:
        return  "I am not impressed by your performance."
print (quote('geOrgE SaiNt PIERRE'))