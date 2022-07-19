from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def detect_loop(lst):
    # Write your code here
    oneStep = lst.head_node
    twoStep = lst.head_node

    while(oneStep and twoStep and twoStep.next_element):
        oneStep = oneStep.next_element
        twoStep = twoStep.next_element.next_element

        if oneStep == twoStep:
            return True
    return False
