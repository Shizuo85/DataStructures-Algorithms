from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Searches a value in the given list.


def search(lst, value):
    # Write your code here
    if lst.is_empty(): return False
    temp = lst.head_node
    
    while temp.next_element is not None:
        if temp.data == value:
            return True
        temp = temp.next_element
    return temp.data == value
