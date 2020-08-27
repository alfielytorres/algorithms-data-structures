"""
As an integrated example that uses collections
as well as reading and writing to files this
module contains (the backend of) a health app
that allows a user to track their nutrional intake
based on recording their eaten foods. The nutrition
values for this example are taken from
http://www.foodnutritiontable.com/ .

For this module to run we need in same folder:
- module with homework functions (homework.py)
- nutr_table.csv
- food_diary.csv
"""

from homework import scaled_row, sum_of_rows

def list_from_file(filename):
    """
    Reads a text file into a list of strings.
    """
    file = open(filename)
    res = []
    for line in file:
        res = res + [line.strip()]
    file.close()
    return res


def table_from_file(filename, num_cols=[]):
    """
    Reads a table from a csv file.

    Input:
    - name of csv file containing table in the follow format
      * first line contains column names (first entry is ignored,
        there has to be at least one line)
      * following lines contain actual data rows
      * first entry per line is considered the id of the row
    - list of column indices (counting id column), which are
      to be converted to floats

    Output:
    - data table
    - list of column names
    - list of ids
    """
    lines = list_from_file(filename)
    cols = lines[0].split(',')[1:]
    ids, tab = [], []
    for i in range(1, len(lines)):
        entries = lines[i].split(',')
        ids = ids + [entries[0]]
        row = []
        for i in range(1, len(entries)):
            datum = float(entries[i]) if i in num_cols else entries[i]
            row = row + [datum]
        tab = tab + [row]
    return tab, cols, ids


def as_str(lst):
    """Converts lst of objects to list of strings."""
    res = []
    for x in lst:
        res.append(str(x))
    return res


def table_to_file(vals, cols, ids, filename):
    """
    Writes a table with column names and ids to csv file.

    Input : table (vals) with column names (cols), and
            row ids (ids), name of output file (filename)
    Output: None; writes table to file
    """
    file = open(filename, 'w')
    header = 'id,' + ','.join(cols) + '\n'
    file.write(header)
    for i in range(len(vals)):
        line = str(ids[i]) + ',' + ','.join(as_str(vals[i])) + '\n'
        file.write(line)
    file.close()

nutr_vals, nutrient_names, foods = table_from_file('nutr_table.csv', range(1, 8))

def nutrients(food, quantity):
    """
    Determines nutrient intake for indiviudal meal.

    Input : string with name of food (food),
            quantitiy of food eaten
    Output: list of nutrional values for meal
            corresponding to scaled entry
            in nutritional value table
    """
    for i in range(len(foods)):
        if foods[i]==food:
            nutr_100g = nutr_vals[i]
            return scaled_row(nutr_100g, quantity/100)
        

def intake_per_day(food_diary):
    """
    Converts food diary into table with intake per day.

    Input : table of eaten foods with columns
            - day (integer)
            - food (string)
            - quantity (float or integer)
    Output: table of eaten nutrients,
            list of row ids
    """
    days, intake = [], []
    for day, food, quantity in food_diary:
        nutr = nutrients(food, quantity)
        if len(days) == 0 or days[-1] != day:
            days.append(day)
            intake.append(nutr)
        else:
            intake[-1] = sum_of_rows(intake[-1], nutr)
    return intake, days


if __name__=='__main__':
    food_diary, _, _ = table_from_file('food_diary.csv', [3])
    intake, days = intake_per_day(food_diary)
    table_to_file(intake, nutrient_names, days, 'intake_per_day.csv')
