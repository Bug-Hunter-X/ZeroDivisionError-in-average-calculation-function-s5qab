def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"Average: {average}")

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"Average: {average}") 