import csv
with open('pmaths10.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    names = [row[0][1:-1] for row in reader][1:]
    ids = [hex(hash(name))[3:11] for name in names]
    both = []
for i in range(len(names)):
    both.append([names[i], ids[i]])

with open('pmaths10-ids.csv', 'w') as file:
    write=csv.writer(file)
    write.writerows(both)
