import csv


def remove_all_other(word):
    index = word.find(", All Other")
    if index != -1:
        return word[:index]

    return word


def plural_to_singular(word):
    if word[-1] == 's':
        return word[: -1]

    return word


with open("occupations.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    output_csv = open("processed-occupations.csv", 'w')
    writer = csv.writer(output_csv)
    for row in csvreader:
        occupation = row[1]
        if occupation.find(",") == -1 and occupation.find("and") == -1:
            occupation_no_all_other = remove_all_other(occupation)
            singular_occupation = plural_to_singular(occupation_no_all_other)
            text = "The " + singular_occupation
            writer.writerow([row[0], text])

    output_csv.close()
