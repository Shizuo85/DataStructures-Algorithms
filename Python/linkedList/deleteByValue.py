from LinkedList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}


def delete(lst, value):
    # Write your code here
    if lst.is_empty(): return False

    temp = lst.head_node
    if temp.data == value:
        temp.delete_at_head()
        return True

    while temp.next_element:
        if temp.next_element.data==value:
            temp.next_element = temp.next_element.next_element
            return True
        temp = temp.next_element
    return False
