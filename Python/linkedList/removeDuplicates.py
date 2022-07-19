from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def remove_duplicates(lst):
    oneStep = lst.head_node
    data = []

    while oneStep:
        data.append(oneStep.data)
        if oneStep and oneStep.next_element and oneStep.next_element.data in data:
            oneStep.next_element = oneStep.next_element.next_element
        oneStep = oneStep.next_element
            
    return lst
