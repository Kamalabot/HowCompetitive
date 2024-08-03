""" Sorting Student Records by Grades:

In this example, we have a list of student records, each containing a student's name and grade. We want to sort these records based on the students' grades in ascending order.
 """
def sort_students_by_grades(student_records):
    # Sort the student records by grades using the Bubble Sort algorithm
    n = len(student_records)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if student_records[j][1] > student_records[j + 1][1]:
                student_records[j], student_records[j + 1] = student_records[j + 1], student_records[j]
    return student_records

student_records = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 65)]
sorted_records = sort_students_by_grades(student_records)
print(sorted_records)

""" Sorting a List of Names:

In this example, we have a list of names, and we want to sort them in lexicographic (dictionary) order.

 """
def sort_names(names):
    # Sort the list of names using the Insertion Sort algorithm
    for i in range(1, len(names)):
        key = names[i]
        j = i - 1
        while j >= 0 and key < names[j]:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key
    return names

names = ["John", "Alice", "Bob", "Charlie", "David"]
sorted_names = sort_names(names)
print(sorted_names)

""" Sorting a List of Products by Price:

Suppose you have a list of products, each with a name and a price, and you want to sort the products by their prices in ascending order.
 """
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def sort_products_by_price(products):
    # Sort the list of products by price using the Merge Sort algorithm
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left_half = products[:mid]
    right_half = products[mid:]

    left_half = sort_products_by_price(left_half)
    right_half = sort_products_by_price(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].price < right[j].price:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

products = [Product("Laptop", 800), Product("Phone", 500), Product("Tablet", 300), Product("Headphones", 100)]
sorted_products = sort_products_by_price(products)
for product in sorted_products:
    print(f"{product.name}: ${product.price}")