def process_numbers(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0
    doubled_numbers = [num * 2 for num in numbers]
    return total_sum, average, doubled_numbers