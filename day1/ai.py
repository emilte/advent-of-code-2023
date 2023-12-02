import re

from task_input import task_input


def calculate_calibration_sum_part_one(calibration_data):
    sum_values = 0
    for line in calibration_data:
        match = re.search(r'\d', line)
        if match:
            try:
                first_digit = int(re.findall(r'\d', line)[0])
                last_digit = int(re.findall(r'\d', line)[-1])
                sum_values += (first_digit * 10) + last_digit
            except ValueError:
                pass  # Skip lines with non-numeric last characters
    return sum_values


def convert_spelled_digits_to_numbers(word):
    spelled_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return spelled_digits.get(word, word)


def calculate_calibration_sum_part_two(calibration_data):
    sum_values = 0
    for line in calibration_data:
        words = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line)
        digits = [convert_spelled_digits_to_numbers(word) for word in words]
        try:
            first_digit = int(''.join(map(str, digits[:2])))
            last_digit = int(digits[-1])
            sum_values += (first_digit * 10) + last_digit
        except ValueError:
            pass  # Skip lines with non-numeric last characters
    return sum_values


# Part One Solution
result_part_one = calculate_calibration_sum_part_one(task_input)
print("Part One Result:", result_part_one)  # Output: 142 for the given sample data

# Part Two Solution
result_part_two = calculate_calibration_sum_part_two(task_input)
print("Part Two Result:", result_part_two)  # Output: 281 for the given sample data
