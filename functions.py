import time

# def count(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
    
# count(0, 10)


# def add(*args):

#     total = 0
#     for num in args:
#         total += num
#     return total

# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#     for name in args:
#         print(name, end=" ")

# display_name("John", "Doe")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Main St", city="New York", state="NY")


# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     # for key, value in kwargs.items():
#     #     print(f"{key}: {value}")
#     print(f"Shipping to: {kwargs.get('street')}, {kwargs['city']}, {kwargs['state']} {kwargs['zip_code']}")
#     print(f"Weight: {kwargs['weight']} pounds")

# shipping_label("John", "Doe", "III", 
#                street = "123 Main St", 
#                city="New York", 
#                state="NY", 
#                zip_code="10001", 
#                weight=5)


# list comprehension formula = [expression for item in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# tripples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# print(doubles)

# numbers = [1, -2, 3, -4, 5, -6]

# positive_numbers = [num for num in numbers if num >= 0]
# negative_numbers = [num for num in numbers if num < 0]
# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 == 1]
# print(positive_numbers)


# match case statement

# def day_of_week(day):
#     match day:
        # case 1:
        #     return "Sunday"
        # case 2:
        #     return "Monday"
        # case 3:
        #     return "Tuesday"
        # case 4:
        #     return "Wednesday"
        # case 5:
        #     return "Thursday"
        # case 6:
        #     return "Friday"
        # case 7:
        #     return "Saturday"
        # case _:
        #     return "Invalid day number"

def is_weekend(day):
    match day: 
        case "Sunday" | "saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid day number"

print(is_weekend("Monday"))