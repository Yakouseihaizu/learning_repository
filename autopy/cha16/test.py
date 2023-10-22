# import csv
# import pprint
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# # exampleData = list(exampleReader)
# # pprint.pprint(exampleData)
# for row in exampleReader:
#     print('Row #'+str(exampleReader.line_num)+' '+str(row))
# exampleFile.close()


# import csv
# outputFile = open('output.csv','w',newline='')
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam','eggs','bacon','ham']))
# print(outputWriter.writerow(['Hello, world!','eggs','bacon','ham']))
# print(outputWriter.writerow([1,2,3.141592,4]))
# outputFile.close()

# import csv
# csvFile = open('example.csv','w',newline='')
# csvWriter = csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
# print(csvWriter.writerow(['apple','orange','grapes']))
# print(csvWriter.writerow(['eggs','bacon','ham']))
# print(csvWriter.writerow(['sapm','sapm','sapm','sapm','sapm','sapm']))
# csvFile.close()

# import csv
# exampleFile = open('example.csv')
# exampleDictReader = csv.DictReader(exampleFile,['time','name','amount'])
# for row in exampleDictReader:
#     print(row['time'],row['name'],row['amount'])

# import csv
# outputFile = open('outputDict.csv','w',newline='')
# outputDictWriter = csv.DictWriter(outputFile,['Name','Pet','Phone'])

# outputDictWriter.writeheader()
# outputDictWriter.writerow({'Name':'Alice','Pet':'cat','Phone':'555-1234'})
# outputDictWriter.writerow({'Name':'Bob','Phone':'555-9999'})
# outputDictWriter.writerow({'Phone':'555-5555','Name':'Carol','Pet':'dog'})

# outputFile.close()

# stringOfJsonData = '{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'
# import json
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

pythonValue = {'iscat':True,'miceCaught':0,'name':'Zophie','felineIQ':None}
import json
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)