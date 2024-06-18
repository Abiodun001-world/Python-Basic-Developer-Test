import re
import random
import psycopg2
from statistics import median, mean, variance

# Connect to the PostgreSQL database
def connect():
    try:
        conn = psycopg2.connect("dbname=bincom_test_py user=abiodun password=abiodun001")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)

# Parse the HTML page and extract the colors
def get_colors(html_content):
    colors = re.findall(r'[A-Z]+', html_content)
    return [color.lower() for color in colors if color != 'ARSH']

# Calculate the mean color
def find_mean_color(colors):
    color_counts = {color: colors.count(color) for color in set(colors)}
    mean_count = mean(color_counts.values())
    mean_colors = [color for color, count in color_counts.items() if count == mean_count]
    return ', '.join(mean_colors)

# Find the most frequent color
def find_most_frequent_color(colors):
    color_counts = {color: colors.count(color) for color in set(colors)}
    most_frequent_color = max(color_counts, key=color_counts.get)
    return most_frequent_color

# Calculate the median color
def find_median_color(colors):
    sorted_colors = sorted(colors)
    median_index = len(sorted_colors) // 2
    if len(sorted_colors) % 2 == 0:
        median_color = sorted_colors[median_index - 1]
    else:
        median_color = sorted_colors[median_index]
    return median_color

# Calculate the variance of colors (BONUS)
def find_color_variance(colors):
    color_counts = [colors.count(color) for color in set(colors)]
    return variance(color_counts)

# Calculate the probability of randomly selecting a red dress (BONUS)
def find_red_probability(colors):
    red_count = colors.count('red')
    total_count = len(colors)
    return red_count / total_count

# Save colors and frequencies to the database
def save_to_database(colors):
    conn = psycopg2.connect("dbname=bincom_test_py user=abiodun password=abiodun001")
    cur = conn.cursor()
    colors_dict = {color: colors.count(color) for color in set(colors)}
    for color, frequency in colors_dict.items():
        cur.execute("INSERT INTO colors (name, frequency) VALUES (%s, %s)", (color, frequency))
    conn.commit()
    cur.close()
    conn.close()

# Recursive searching algorithm (BONUS)
def recursive_search(arr, target):
    if not arr:
        return False
    if arr[0] == target:
        return True
    return recursive_search(arr[1:], target)

# Generate random 4-digit binary number and convert to decimal
def generate_binary_and_convert():
    binary_str = ''.join(str(random.randint(0, 1)) for _ in range(4))
    decimal = int(binary_str, 2)
    return binary_str, decimal

# Sum the first 50 Fibonacci numbers
def sum_fibonacci(n):
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    return sum(fib(i) for i in range(n))

# Read the HTML content from the file
with open('python_class_question.html', 'r') as file:
    html_content = file.read()

# Extract the colors from the HTML content
colors = get_colors(html_content)

# Find the mean color
mean_color = find_mean_color(colors)
print("Mean color:", mean_color)

# Find the most frequent color
most_frequent_color = find_most_frequent_color(colors)
print("Most frequent color:", most_frequent_color)

# Find the median color
median_color = find_median_color(colors)
print("Median color:", median_color)

# Find the variance of colors (BONUS)
color_variance = find_color_variance(colors)
print("Variance of colors:", color_variance)

# Find the probability of randomly selecting a red dress (BONUS)
red_probability = find_red_probability(colors)
print("Probability of randomly selecting a red dress:", red_probability)

# Save colors and frequencies to the database
save_to_database(colors)

# Recursive searching algorithm (BONUS)
numbers = [1, 3, 5, 7, 9]
target = 5
found = recursive_search(numbers, target)
print("Target found:", found)

# Generate random 4-digit binary number and convert to decimal
binary_str, decimal = generate_binary_and_convert()
print("Binary number:", binary_str)
print("Decimal equivalent:", decimal)

# Sum the first 50 Fibonacci numbers
fibonacci_sum = sum_fibonacci(50)
print("Sum of the first 50 Fibonacci numbers:", fibonacci_sum)