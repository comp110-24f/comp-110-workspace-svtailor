"""Data related utility functions."""

__author__ = "730772504"

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted

def head(input: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = dict()

    for key in input:
        first_n_values: list[str] = []

        for num in range(0, rows):
            first_n_values.append(input[key][num])

        result[key] = first_n_values

    return result

def select(input: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = dict()

    for column in col_names:
        result[column] = input[column]

    return(result)
        

def concat(input_1: dict[str, list[str]], input_2: dict[str, list[str]]) -> dict[str, list[str]]: 
    result: dict[str, list[str]] = dict()

    for column_1 in input_1: 
        result[column_1] = input_1[column_1]
        for column_2 in input_2: 
            if column_1 == column_2: 
                result[column_1] = input_1[column_1] + input_2[column_2]
            else:
                result[column_2] = input_2[column_2]

    return result

def count(input_list: list[str]) -> dict[str, int]:
    count_values: dict[str,int] = dict()

    for item in input_list: 
        if item in count_values: 
            count_values[item] += 1

        else: 
            count_values[item]=1
    
    return count_values


def filtered(input_dict: dict[str, list[str]], col: str, val: int | str) -> dict[str, list[str]]:
    """Allows you to filter your table based on one column's values"""
    col_vals = input_dict[col]
    indices: list[int] = []
    result: dict[str, list[str]] = {}
    
    for i in range(0,len(col_vals)):
        if col_vals[i] == val:
            indices.append(i)

    for key in input_dict:
        result[key] = []
        for idx in indices:
            result[key].append(input_dict[key][idx])

    return result
        

def average(input_dict: dict[str, list[str]], col: str) -> float:
    sum: int = 0 
    for i in range(0, len(input_dict[col])):
        sum += int(input_dict[col][i])

    average = sum/len(input_dict[col])

    return (average)

