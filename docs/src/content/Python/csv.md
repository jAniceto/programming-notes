Title: CSV files
Date: 2018-04-19 16:57
Authors: José Aniceto


CSV (Comma Separated Values) is a very popular import and export data format used in spreadsheets and databases. Each line in a CSV file is a data record. Each record consists of one or more fields, separated by commas. While CSV is a very simple data format, there can be many differecies, such as different delimiters, new lines, or quoting characters.

## Reading CSV files 
Reading of CSV files into memory:

```
# example1.csv
1/2/2014,5,8,red
1/3/2014,5,2,green
1/4/2014,9,1,blue
```

```python
import csv

with open('example1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
```

### DictReader 
The `csv.DictReader` class operates like a regular reader but maps the information read into a dictionary. The keys for the dictionary can be passed in with the fieldnames parameter or inferred from the first row of the CSV file.

```
# example2.csv
min,avg,max
1, 5.5, 10
2, 3.5, 5
```

```python
import csv

with open('values.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['min'], row['avg'], row['max'])
```

## Writing to CSV files
The `csv.writer()` method returns a writer object which converts the user's data into delimited strings on the given file-like object.

```python
import csv

nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

with open('numbers2.csv', 'w') as f:
    writer = csv.writer(f)
    for row in nms:
        writer.writerow(row)
```

### DictWriter

The csv.DictWriter class operates like a regular writer but maps Python dictionaries into CSV rows. The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary passed to the writerow() method are written to the CSV file.
```python
import csv

with open('names.csv', 'w') as f:
    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)    

    writer.writeheader()  # writes the headers to the CSV file.
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})
```

## Quoting CSV Files
With the CSV module, you can also perform a variety of quoting functions.

They are:

* `csv.QUOTE_ALL` - Quote everything, regardless of type.
* `csv.QUOTE_MINIMAL` - Quote fields with special characters
* `csv.QUOTE_NONNUMERIC` - Quote all fields that are not integers or floats
* `csv.QUOTE_NONE` - Do not quote anything on output
