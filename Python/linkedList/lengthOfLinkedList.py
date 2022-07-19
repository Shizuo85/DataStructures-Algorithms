from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}


def length(lst):
    # Write - Your - Code
    if lst.is_empty(): return 0
    count =1
    temp = lst.head_node
    while temp.next_element:
        count+=1
        temp=temp.next_element
    return count
