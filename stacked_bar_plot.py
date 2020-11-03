import csv
import matplotlib.pyplot as plt
import numpy as np

with open('mca_maharashtra.csv', 'r', encoding='latin-1') as csv_file:
    str9 = "Manufacturing (Metals & Chemicals, and products thereof)"
    csv_reader = csv.reader(csv_file)
    pba_dict = {}
    for line in csv_reader:
        if line[6] == 'DATE_OF_REGISTRATION':
            continue
        else:
            string = line[6]
            string = string[6:]
            if string == "":
                continue
            if int(string) >= 1990 and int(string) < 2000:
                if string not in pba_dict:
                    pba_dict[string] = [0, 0, 0, 0, 0, 0]
                else:
                    if line[11] == "Agriculture and Allied Activities":
                        pba_dict[string][0] += 1
                    if line[11] == "Trading":
                        pba_dict[string][1] += 1
                    if line[11] == str9:
                        pba_dict[string][2] += 1
                    if line[11] == "Finance":
                        pba_dict[string][3] += 1
                    if line[11] == "Construction":
                        pba_dict[string][4] += 1
                    pba_dict[string][5] += 1
# print(year_dict)
years = []
for i in pba_dict.keys():
    years.append(i)
years.sort()
# print(pba_dict)
sorted_pba_dict = sorted(pba_dict.items(), key=lambda t: t[0])
date = []
pba1 = []
pba2 = []
pba3 = []
pba4 = []
pba5 = []
pba6 = []
for i in range(len(sorted_pba_dict)):
    date.append(sorted_pba_dict[i][0])
    pba1.append(sorted_pba_dict[i][1][0])
    pba2.append(sorted_pba_dict[i][1][1])
    pba3.append(sorted_pba_dict[i][1][2])
    pba4.append(sorted_pba_dict[i][1][3])
    pba5.append(sorted_pba_dict[i][1][4])
    pba6.append(sorted_pba_dict[i][1][5])

x_indexes = np.arange(len(years))
width = 0.15
str1 = "Agriculture and Allied Activities"
str2 = "Trading"
str3 = "Manufacturing (Metals & Chemicals, and products thereof)"
str4 = "Finance"
str5 = "Construction"
str6 = "Year"
plt.bar(x_indexes, pba1, width=width, color="#FF5733", label=str1)
plt.bar(x_indexes + width, pba2, width=width, color="#FFF633", label=str2)
plt.bar(x_indexes-width, pba3, width=width, color="#8AFF33", label=str3)
plt.bar(x_indexes - width*2, pba4, width=width, color="#33FFCE", label=str4)
plt.bar(x_indexes + width*2, pba5, width=width, color="#339FFF", label=str5)
plt.bar(x_indexes + width*3, pba6, width=width, color="#7433FF", label=str6)
plt.legend()
plt.xticks(ticks=x_indexes, labels=years)
plt.xlabel("Years")
plt.ylabel("Total Companies")
plt.title("Companies from 1990 to 1999 in Maharashtra")
plt.tight_layout()
plt.savefig("graph4.png")
