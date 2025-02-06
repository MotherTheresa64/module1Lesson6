# First Project: Manipulate Python Lists, their characteristics, and operations.


"""
Define a list called "fruits" containing the following items: "apple", "banana", "cherry", and "date".
A.) Print the first item in the list
B.) Print the last item using negative indexing.
"""
# Will reference this initial list for the whole program 
fruit_list = ["apple", "banana", "cherry", "date"]

print(fruit_list[0])
print(fruit_list[-1])

"""
Add and Insert Items:
A.) Use .append() to add "elderberry" to the end of the list.
B.) Use .insert() to add "blueberry" at index 1.
"""

fruit_list.append("elderberry")
fruit_list.insert(1, "blueberry")

"""
Remove Items:
A.) Use .remove() to remove "banana"
B.) Use del to delete the first item from the list.
"""
fruit_list.remove("banana")
fruit_list.pop(0)

"""
Slice the List: Create and print a subset of the list 
called citrus_fruits containing items from 
index 1 to 3 (inclusive of 1, exclusive of 3).
"""

citrus_fruits = fruit_list[1:3]


# <-----------------Final Challenge Below This Line----------------->
# Create a program that asks the user for their top 3 favorite books, stores them in a list, and prints the list in a sorted order.
# Steps:
# nitialize an Empty List.
# Prompt the User for Input.
# Store the Books in the List.
# Sort the List
# Print the Sorted List

books = []

book1 = input("Enter your first favorite book: ")
book2 = input("Enter your second favorite book: ")
book3 = input("Enter your third favorite book: ")

all_books = [book1, book2, book3]
books.append(all_books)
books.sort()
print(books)
print("What a neat list of books!")