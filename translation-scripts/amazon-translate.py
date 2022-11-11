import boto3
import csv

translate = boto3.client(service_name='translate', region_name='us-east-2', use_ssl=True)

input_csv_name = "processed-occupations.csv"
output_csv_name = "amazon-translate-output-sp.csv"

with open(input_csv_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    output_csv = open(output_csv_name, 'w')
    writer = csv.writer(output_csv)
    for row in csvreader:
        occupation = row[1]
        result = translate.translate_text(Text = occupation,
                    SourceLanguageCode="en", TargetLanguageCode="es")
        # print(result.get('TranslatedText'))
        # text, translation = translate_text(target_language, occupation)
        writer.writerow([occupation, result.get('TranslatedText')])

    output_csv.close()
