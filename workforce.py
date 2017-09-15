def parseCSV(csv, includeFirstLine):
    rows = csv.split("\n")
    if(not includeFirstLine):
        rows = rows[1:]
    valuesByRow = []
    for row in rows:
        row = row.strip()
        if(len(row) > 0):
            columns = [""]
            quote = False
            for c in row:
                if(c == '"' and quote == False):
                    quote = True
                elif(c == '"' and quote == True):
                    quote = False
                elif(c == ',' and quote == False):
                    columns.append("")
                else:
                    columns[-1] += c
            valuesByRow.append(columns)
    return valuesByRow

file = open("occupations.csv", 'r')
parseCSV(file.read(), True)
file.close()
