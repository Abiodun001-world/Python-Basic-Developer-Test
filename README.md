# Python Basic Developer Test

This repository contains a Python program that analyzes the colors of dresses worn by Bincom ICT Solutions staff members throughout the week. The program answers the following questions:

1. Which color of shirt is the mean color?
2. Which color is mostly worn throughout the week?
3. Which color is the median?
4. **BONUS** Get the variance of the colors.
5. **BONUS** If a color is chosen at random, what is the probability that the color is red?
6. Save the colors and their frequencies in a PostgreSQL database.
7. **BONUS** Write a recursive searching algorithm to search for a number entered by the user in a list of numbers.
8. Write a program that generates random 4-digit numbers of 0s and 1s and converts the generated number to base 10.
9. Write a program to sum the first 50 Fibonacci sequence numbers.

## Prerequisites

- Python 3.x
- PostgreSQL installed and running
- `psycopg2` library installed (`pip install psycopg2`)

## Usage

1. Clone the repository or download the `bincom_test.py` file.
2. Open the `bincom_test.py` file and modify the `connect` function with your PostgreSQL database credentials.
3. Run the `bincom_test.py` file using the following command:

```
python bincom_test.py
```

The program will output the following:

- The mean color of the dresses worn throughout the week.
- The color that is mostly worn throughout the week.
- The median color of the dresses worn throughout the week.
- The variance of the colors (if the bonus question is attempted).
- The probability of randomly selecting a red dress (if the bonus question is attempted).
- The colors and their frequencies will be saved in the PostgreSQL database.
- A recursive searching algorithm to search for a number entered by the user in a list of numbers (if the bonus question is attempted).
- A program that generates random 4-digit numbers of 0s and 1s and converts them to base 10.
- The sum of the first 50 Fibonacci sequence numbers.

## Notes

- The program assumes that the PostgreSQL server is running and accepting connections on the default port (5432).
- The program uses regular expressions to parse the HTML page containing the dress colors.
- The program follows the provided requirements and hints.
- The bonus questions are marked as such in the code and can be uncommented if desired.

## Acknowledgments

This program was created as part of the Bincom ICT Solutions Python Basic Developer Test.