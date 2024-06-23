import xmltodict
import json


filePath = "Data/LGD Latest/Andaman And Nicobar Islands/"

def check_empty_row(row):
    empty_status = False

    total_empty_cell = 0

    for cell in row:
        if cell == "":
            total_empty_cell = total_empty_cell + 1
    
    if total_empty_cell == len(row):
        empty_status = True

    return empty_status

def write_csv_file(data, file):

    csv_data = []

    for row in data:
        csv_data.append('"' + '","'.join(row) + '"')

    with open(file + '.csv', 'w') as f:
        f.write('\n'.join(csv_data))

def write_json_file(data, file):

    json_data = []

    for row in data:
        row_json = {}
        index = 0
        for cell in row:
            if index != 0:
                row_json |= {data[0][index]: cell}
            index = index + 1
            

        json_data.append(row_json)
        
    with open(file + '.json', "w") as json_file:
        json.dump(json_data, json_file, indent=4)

def get_csv_data( path, file, columns ):
    with open(path + file + '.xls', 'r') as f:
        xml_data = f.read()

    dict_data = xmltodict.parse(xml_data)

    rows = dict_data["Workbook"]["Worksheet"]["ss:Table"]["Row"]

    final_data = []

    for row in rows:
        if not isinstance(row, list):  # Check if "Row" is a list
            temp = []
            if row.get("Cell") and isinstance(row.get("Cell"), list):
                for data in row.get("Cell"):
                    if( data.get("Data") ):
                        a = data.get("Data").get("#text")
                        if a is None:
                            temp.append("")
                        else:
                            temp.append(a.replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("( ", "(").replace(" )", ")").replace("\n", " "))
                    else:
                        temp.append("")
            if( (len(temp) == columns) and (check_empty_row(temp) == False) ):
                final_data.append(temp)

    write_csv_file(final_data, file)
    write_json_file(final_data, file)

    return final_data

all_block_state_with_covered_village = get_csv_data(filePath, "allBlockStateWithCoveredVillage12024:06:23:00:50:11:325", 8)
block_of_specific_state = get_csv_data(filePath, "blockofspecificState2024:06:23:00:50:11:258", 7)
district_of_specific_state = get_csv_data(filePath, "districtofSpecificState2024:06:23:00:50:10:581", 7)
priLb_specific_state = get_csv_data(filePath, "priLbSpecificState2024:06:23:00:50:10:828", 8)
pri_wards = get_csv_data(filePath, "priWards2024:06:23:00:50:11:073", 10)
sub_district_of_specific_state = get_csv_data(filePath, "subDistrictofSpecificState2024:06:23:00:50:10:606", 9)
tlb_specific_state = get_csv_data(filePath, "tlbSpecificState2024:06:23:00:50:10:894", 8)
ulb_specific_state = get_csv_data(filePath, "ulbSpecificState2024:06:23:00:50:10:855", 9)
ulb_ward_for_state = get_csv_data(filePath, "uLBWardforState2024:06:23:00:50:10:920", 6)
ulb_ward_for_state_with_cov = get_csv_data(filePath, "uLBWardforStateWithCov2024:06:23:00:50:10:981", 10)
village_gram_panchayat_mapping = get_csv_data(filePath, "villageGramPanchayatMapping2024:06:23:00:50:11:226", 15)
village_of_specific_state = get_csv_data(filePath, "villageofSpecificState2024:06:23:00:50:10:782", 13)



