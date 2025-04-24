

# *1. Create a CSV file readable in MS Excel*
import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([1, 'Alice', 85, 90, 88])
    writer.writerow([2, 'Bob', 78, 82, 80])


# *2. Read MS Excel data and convert to dictionary*

import pandas as pd

df = pd.read_excel('students.xlsx')
data = df.to_dict(orient='records')

for record in data:
    total = record['Subject1'] + record['Subject2'] + record['Subject3']
    record['Total'] = total

print(data)


### *3. Accept contact details and create a vCard*

name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

with open(f"{name}.vcf", "w") as f:
    f.write(vcard)




### *4. Create subdirectory and copy a file*

import os
import shutil

os.makedirs("new_subdir", exist_ok=True)
shutil.copy("source_folder/example.txt", "new_subdir/example.txt")




### *5. Copy file and convert lowercase to uppercase*

with open('source.txt', 'r') as src, open('destination.txt', 'w') as dst:
    for line in src:
        dst.write(line.upper())



### *6. Merge lines alternately from two files*

with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for l1, l2 in zip(lines1, lines2):
        out.write(l1.strip() + '\n')
        out.write(l2.strip() + '\n')
    longer = lines1[len(lines2):] if len(lines1) > len(lines2) else lines2[len(lines1):]
    out.writelines(longer)




### *7. Serialize and Deserialize Employee object*
import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

emp = Employee(101, 'John Doe', '2023-03-01', 60000)

# Serialize
with open('employee.dat', 'wb') as f:
    pickle.dump(emp, f)

# Deserialize
with open('employee.dat', 'rb') as f:
    emp_loaded = pickle.load(f)
    print(vars(emp_loaded))



### *8. Delete words 'a', 'an', and 'the' from a text file*

with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        for word in [' a ', ' an ', ' the ']:
            line = line.replace(word, ' ')
        fout.write(line)


