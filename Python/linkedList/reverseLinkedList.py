from Node import Node
from LinkedList import LinkedList
#Access head_node => list.get_head()
#Check if list is empty => list.is_empty()
#Delete at head => list.delete_at_head()
#Delete by value => list.delete(value)
#Search for element => list.search()
#Length of the list => list.length()
#Node class  { int data ; Node next_element;}

def reverse(lst):
  # Write your code here
  current= lst.head_node
  next = None
  previous = None

  while current:
    next = current.next_element
    current.next_element = previous
    previous = current

    lst.head_node=previous
    current = next
  return lst