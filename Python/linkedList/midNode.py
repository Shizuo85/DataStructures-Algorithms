from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def find_mid(lst):
    # Write your code here
    current_node = lst.head_node
    mid_node = lst.head_node
    if(current_node == None):
        return -1;
    elif (current_node.next_element == None):
        return current_node.data
    
    current_node = current_node.next_element.next_element
    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
            current_node = current_node.next_element
    return mid_node.data