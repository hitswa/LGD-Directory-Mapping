import xmltodict
import json


filePath = "Data/LGD Latest/Andaman And Nicobar Islands/"

def checkEmptyRow(arrRow):
    emptyStatus = False

    totalEmptyCell = 0

    for cell in arrRow:
        if cell == "":
            totalEmptyCell = totalEmptyCell + 1
    
    if totalEmptyCell == len(arrRow):
        emptyStatus = True

    return emptyStatus

def writeCsvFile(data, file):

    csvData = []

    for row in data:
        csvData.append('"' + '","'.join(row) + '"')

    with open(file + '.csv', 'w') as f:
        f.write('\n'.join(csvData))

def writeJsonFile(data, file):

    jsonData = []

    for row in data:
        rowJson = {}
        index = 0
        for cell in row:
            if index != 0:
                rowJson |= {data[0][index]: cell}
            index = index + 1
            

        jsonData.append(rowJson)
        
    with open(file + '.json', "w") as json_file:
        json.dump(jsonData, json_file, indent=4)

def getCsvData( path, file, columns ):
    with open(path + file + '.xls', 'r') as f:
        xml_data = f.read()

    dict_data = xmltodict.parse(xml_data)

    rows = dict_data["Workbook"]["Worksheet"]["ss:Table"]["Row"]

    finalData = []

    for row in rows:
        if not isinstance(row, list):  # Check if "Row" is a list
            temp = []
            if row.get("Cell"):
                if isinstance(row.get("Cell"), list):
                    for data in row.get("Cell"):
                        if( data.get("Data") ):
                            a = data.get("Data").get("#text")
                            if a is None:
                                temp.append("")
                            else:
                                temp.append(a.replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("( ", "(").replace(" )", ")").replace("\n", " "))
                        else:
                            temp.append("")
            if( len(temp) == columns ):
                if( checkEmptyRow(temp) == False):
                    finalData.append(temp)

    writeCsvFile(finalData, file)
    writeJsonFile(finalData, file)

    return finalData

allBlockStateWithCoveredVillage = getCsvData(filePath, "allBlockStateWithCoveredVillage12024:06:23:00:50:11:325", 8)
blockofspecificState = getCsvData(filePath, "blockofspecificState2024:06:23:00:50:11:258", 7)
districtofSpecificState = getCsvData(filePath, "districtofSpecificState2024:06:23:00:50:10:581", 7)
priLbSpecificState = getCsvData(filePath, "priLbSpecificState2024:06:23:00:50:10:828", 8)
priWards = getCsvData(filePath, "priWards2024:06:23:00:50:11:073", 10)
subDistrictofSpecificState = getCsvData(filePath, "subDistrictofSpecificState2024:06:23:00:50:10:606", 9)
tlbSpecificState = getCsvData(filePath, "tlbSpecificState2024:06:23:00:50:10:894", 8)
ulbSpecificState = getCsvData(filePath, "ulbSpecificState2024:06:23:00:50:10:855", 9)
uLBWardforState = getCsvData(filePath, "uLBWardforState2024:06:23:00:50:10:920", 6)
uLBWardforStateWithCov = getCsvData(filePath, "uLBWardforStateWithCov2024:06:23:00:50:10:981", 10)
villageGramPanchayatMapping = getCsvData(filePath, "villageGramPanchayatMapping2024:06:23:00:50:11:226", 15)
villageofSpecificState = getCsvData(filePath, "villageofSpecificState2024:06:23:00:50:10:782", 13)



