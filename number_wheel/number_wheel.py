

def get_user() -> list:
    returnList = []
    lock = str(input("List char:"))
    vals = []
    while(lock != "q"):
        returnList.append(lock)
        raw_val = str(input("List vals for the input character seperated by a space: "))
    
        
        raw_val = list(raw_val.split(" "))
        vals.append(raw_val)
        lock = str(input("List char: "))

    return returnList,vals
def user_preprocess(returned_char,returned_vals):
    return {char:vals for char,vals in zip(returned_char,returned_vals)}
def traverse(hash_map,list_vals):
    for i in range(len(list_vals)):
        if list_vals[i].isalpha():
            traverse(hash_map,hash_map[list_vals[i]])
        else:
            print(list_vals[i],end=" " )
def algo(hash_map):
    for keys,vals in hash_map.items():
        traverse(hash_map,vals)
returned_char,returned_vals = get_user()
final_input_dict = user_preprocess(returned_char,returned_vals)
print(final_input_dict,"\n Generates: ",end = " " )
algo(final_input_dict)


