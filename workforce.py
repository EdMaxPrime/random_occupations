def parseCSV(csv, includeFirstLine):
    rows = csv.split("\n")
    if(not includeFirstLine):
        rows = rows[1:]
    valuesByRow = []
    for row in rows:
        row = row.strip()
        if(len(row) > 0):
            valuesByRow.append(row.split(","))
    print valuesByRow

file = open("occupations.csv", 'r')
parseCSV(file.read(), True)
file.close()
