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

# Function to find the nth node from end of Linked List


def find_nth(lst, n):
    # Write your code heresaq   
    items = lst.length()
    start  = lst.get_head()
    index = 0
    while index < (items-n):
        start = start.next_element
        index += 1
    return start
