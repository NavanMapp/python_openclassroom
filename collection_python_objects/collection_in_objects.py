# Write your code here
def dictionary_masher(dict_a, dict_b):
    for k in dict_b.keys():
        dict_a[k] = dict_b[k]
    return dict_a    
    
# Test your function using the code below
if __name__ == '__main__':
    print(dictionary_masher({"name": "Amos"}, {"age": 100}))
