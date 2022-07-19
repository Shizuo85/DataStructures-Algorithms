from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1
    visited = []
    temp = list1.head_node

    while temp.next_element:
        visited.append(temp.data)
        temp = temp.next_element

    visited.append(temp.data)
   
    temp2 = list2.head_node
    while temp2:
        if temp2.data not in visited:
            visited.append(temp2.data)
            temp.next_element = temp2
            temp = temp.next_element
        temp2=temp2.next_element

    return list1


# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here
    if list1.is_empty() or list2.is_empty():
        return None
    visited = []
    temp = list1.head_node

    while temp.next_element:
        visited.append(temp.data)
        temp = temp.next_element

    visited.append(temp.data)
   
    temp2 = list2.head_node
    while temp2 and temp2.data not in visited:
        list2.head_node = temp2.next_element
        temp2 = list2.head_node
    while temp2:
        if temp2.next_element and temp2.next_element.data not in visited:
            temp2.next_element = temp2.next_element.next_element

        temp2=temp2.next_element

    return list2
