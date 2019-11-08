# Number Wheels

----
## Task:
see [Description](http://rosettacode.org/wiki/Intersecting_Number_Wheels)



Given the wheels:

     A: 1 B 2 

     B: 3 4

The series of numbers generated starts:

     1, 3, 2, 1, 4, 2, 1, 3, 2, 1, 4, 2, 1, 3, 2...
Another example:

     A: 1 D D


     D:  6 7 8


   Generates:
       
   
      1 6 7 1 8 6 1 7 8 1 6 7 1 8 6 1 7 8 1 6 ...    


----
## Code
Takes input from command line for any number of characters, and defines that list with subsequent user input.

Stores these user inputs into a hashmap: in 

    def user_preprocess(returned_char,returned_vals):
      return {char:vals for char,vals in zip(returned_char,returned_vals)}

Then call function algo to start the generation of the strings. 

    def algo(hash_map):
      for keys,vals in hash_map.items():
        traverse(hash_map,vals)

function traverse actually parses the number/character defined list.

    def traverse(hash_map,list_vals):
      for i in range(len(list_vals)):
        if list_vals[i].isalpha():
            traverse(hash_map,hash_map[list_vals[i]])
        else:
            print(list_vals[i],end=" " )

If a letter, then recursively call traverse, else just print the number!

