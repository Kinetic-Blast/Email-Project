import os
import json
import email.header
import eml_parser
import datetime

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

def convert_eml_to_json(eml_file_path):
    output_path = eml_file_path.replace(".eml", ".json")
    
    ep = eml_parser.EmlParser(include_raw_body=True, include_attachment_data=True)

    try:
        temp_Mail = ep.decode_email(eml_file_path)
        with open(output_path, "w") as json_file:
            json.dump(temp_Mail, json_file, default=json_serial, indent=4)
    except:return

def main():
    eml_folder = 'email'
    eml_files = [f for f in os.listdir(eml_folder) if f.endswith('.eml')]

    for eml_file in eml_files:
        eml_file_path = os.path.join(eml_folder, eml_file)
        print(f"Converting: {eml_file}")
        convert_eml_to_json(eml_file_path)
        print("=" * 50)

if __name__ == "__main__":
    main()