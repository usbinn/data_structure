def find_max_recursive(num_list):
  max_value = None
  num = num_list.pop()
  print(num_list)
  if max_value is None or num > max_value : max_value = num
  if num_list == []:
    return max_value
  else:
    return find_max_recursive(num_list)


def find_max_iterative(num_list):
  max_value = None
  for i in num_list:
    if max_value is None or i > max_value : max_value = i
  return max_value

num_list = [10,30,14,51,21,33]
# print(find_max_iterative(num_list))
print(find_max_recursive(num_list))