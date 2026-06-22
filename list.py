#write  program to remove duplicates in the list
my_list = [ 10, 90, 80, 80, 90, 1, 1, 2, 3, 4, 5]
new_list = list(dict.fromkeys(my_list))
new_list.sort()
print(new_list)

'''the list is sorted means it works in ascending order and also the list duplicates
 can be removd by using li dict.fromkeys() and another way of doing is changing brackets
 # Example
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print(unique_list)'''
#sort() == is for ascending order in list
#reverse() == is used for descending order in the list
#append() ==  adding elements in the list at the end
#insert () is used to insert elements based on the index and object
#example of insert is insert (1 , 100) which will replace the index one element with 100
#pop() to remove last element from the list
#clear () for clearing the list or emptying

#matrix is a 2 dimensional list

"""matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(matrix)

to mention or get output of any number in the matrix 

we need to define using matrix [1] [1] -- first refers to list and second to index"""
