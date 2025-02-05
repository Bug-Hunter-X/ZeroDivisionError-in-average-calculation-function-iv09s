def calculate_average(numbers):
    if not numbers:  # Handle empty list
        return 0
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}")