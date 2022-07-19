from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list


def insert_at_tail(lst, value):
    # Write - Your - Code
    value = Node(value)
    if(lst.is_empty()):
        lst.head_node = value
        return lst

    temp = lst.get_head()
    while temp.next_element is not None:
        temp = temp.next_element
    temp.next_element = value
    return lst
    
