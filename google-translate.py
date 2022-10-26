from google.cloud import translate_v2 as translate
import csv

"""
instructions for running this script:
run pip install google-cloud-translate==2.0.1 before running this script
run export GOOGLE_APPLICATION_CREDENTIALS="<path to service account json file>"
to get the service account json file, reach out to a member of the bias team

for reference, refer to the google translation api setup documentation:
https://cloud.google.com/translate/docs/setup
"""


def translate_text(target, text):
    """
    translates text into the target language.
    text must be a string.
    target must be an ISO 639-1 language code.
    language codes can be found here: 
    https://cloud.google.com/translate/docs/languages
    """
    translate_client = translate.Client()

    result = translate_client.translate(text, target_language=target)

    text = result["input"]
    translation = result["translatedText"]

    return text, translation


def translate_csv(input_csv_name, output_csv_name, target_language):
    """
    opens the input csv file, creates an output csv file, translates the words 
    in the input csv to the target language and stores those translations in the
    output csv.
    """
    with open(input_csv_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        output_csv = open(output_csv_name, 'w')
        writer = csv.writer(output_csv)
        for row in csvreader:
            occupation = row[1]
            text, translation = translate_text(target_language, occupation)
            writer.writerow([text, translation])

        output_csv.close()


# example of how to run the translate_csv function using arabic translation
translate_csv("occupations.csv", "google-translate-output-ar", "ar")
