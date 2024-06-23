import pandas as pd
import json

file_location = "Data/output/Andaman And Nicobar Islands/"
output_location = "Data/output/Andaman And Nicobar Islands/"

df_01 = pd.read_csv( file_location + 'tlbSpecificState2024:06:23:00:50:10:894.csv')

df_01_tribal_council = df_01[df_01["Local Body Type Name"]=="Tribal Council"]


finalData = [["Local Body Code","Local Body Version","Local Body Name (In English)","Local Body Name (In Local)","Local Body Type Code","Local Body Type Name", "_Local Body Code", "_Local Body Version", "_Local Body Name (In English)", "_Local Body Name (In Local)", "_Local Body Type Code", "_Local Body Type Name"]]

for index, row in df_01_tribal_council.iterrows():
    temp = df_01[df_01["Parent Localbody Code"]==row["Local Body Code"]]


    for index, row1 in temp.iterrows():
        newRow = []

        newRow.append(str(row["Local Body Code"]))
        newRow.append(str(row["Local Body Version"]))
        newRow.append(str(row["Local Body Name (In English)"]))
        newRow.append(str(row["Local Body Name (In Local)"]))
        newRow.append(str(row["Localbody Type Code"]))
        newRow.append(str(row["Local Body Type Name"]))
        newRow.append(str(row1["Local Body Code"]))
        newRow.append(str(row1["Local Body Version"]))
        newRow.append(str(row1["Local Body Name (In English)"]))
        newRow.append(str(row1["Local Body Name (In Local)"]))
        newRow.append(str(row1["Localbody Type Code"]))
        newRow.append(str(row1["Local Body Type Name"]))

        finalData.append(newRow)



def write_csv_file(data, file):

    csv_data = []

    for row in data:
        csv_data.append('"' + '","'.join(row) + '"')

    with open(output_location + file + '.csv', 'w') as f:
        f.write('\n'.join(csv_data))


write_csv_file(finalData, 'merge_local_govt_rural_traditional_local_body')
