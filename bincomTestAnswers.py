#!/bin/bash python3

from collections import Counter
from statistics import mode, median, variance

# Define the data for each day
colors = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE",
}

# Flatten all colors into a single list
all_colors = []
for day_colors in colors.values():
    all_colors.extend(day_colors.split(", "))

# 1. Determine the mean color (most common color)
most_common_color = mode(all_colors)

# 2. Determine the color mostly worn throughout the week
color_counts = Counter(all_colors)
most_worn_color = color_counts.most_common(1)[0][0]

# 3. Determine the median color
sorted_colors = sorted(all_colors)  # Sort alphabetically for a consistent median
median_color = median(sorted_colors)

# 4. Calculate variance (Bonus)
# Since colors are categorical, we assign arbitrary numerical values
color_map = {color: i for i, color in enumerate(sorted(set(all_colors)))}
numerical_colors = [color_map[color] for color in all_colors]
color_variance = variance(numerical_colors)

# 5. Probability of randomly selecting "RED" (Bonus)
red_count = color_counts["RED"]
total_colors = len(all_colors)
red_probability = red_count / total_colors

# Display the results
print(f"1. The mean color is: {most_common_color}")
print(f"2. The color mostly worn throughout the week is: {most_worn_color}")
print(f"3. The median color is: {median_color}")
print(f"4. The variance of the colors is: {color_variance:.2f}")
print(f"5. The probability of choosing 'RED' is: {red_probability:.2%}")


# 7. Recursive search for a number in a list:
def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return -1  # Target not found
    if lst[index] == target:
        return index  # Target found
    return recursive_search(lst, target, index + 1)

# 8. generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
from random import random
binary_number = "".join(str(random.randint(0, 1)) for _ in range(4))
base_10_number = int(binary_number, 2)

print(f"Generated binary number: {binary_number}")
print(f"Converted to base 10: {base_10_number}")


#.9 Sum the first 50 fibonacci numbers:
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

# Calculate and print the sum of the first 50 Fibonacci numbers
fib_sum = fibonacci_sum(50)
print(f"Sum of the first 50 Fibonacci numbers: {fib_sum}")



# ========= ANSWERS ============
# 1. The mean color is: BLUE
# 2. The color mostly worn throughout the week is: BLUE
# 3. The median color is: GREEN
# 4. The variance of the colors is: 9.16
# 5. The probability of choosing 'RED' is: 9.47%
# 8. Generated binary number: 0001
    # Converted to base 10: 1
# 9. Sum of the first 50 Fibonacci numbers: 20365011073
