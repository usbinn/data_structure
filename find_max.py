def find_max_recursive(num_list):
  max_value 


def find_max_iterative(num_list):
  max_value = None
  for i in num_list:
    if max_value is None or i > max_value : max_value = i
  return max_value

num_list = [1,3,4,5,2,23]
print(find_max_iterative(num_list))