import json


def jsonToCSV(jsonFilePath, csvFilePath):
    # reading json file.
    with open(jsonFilePath, 'r') as jsonFile:
        data = json.load(jsonFile)

    # getting the headers.
    headers = list(data[0].keys())
    headersCommaJoined = ','.join(headers)
    csvString = headersCommaJoined

    # getting the values.
    for object in data:
        values = list(object.values())
        valuesStringified = [str(value) for value in values]
        valuesCommaJoined = '\n' + ','.join(valuesStringified)
        csvString += valuesCommaJoined

    # writing csv file.
    with open(csvFilePath, 'w') as csvFile:
        csvFile.write(csvString)


JSON_FILE = './test/input.json'
CSV_FILE = './test/output.csv'

if __name__ == '__main__':
    jsonToCSV(JSON_FILE, CSV_FILE)