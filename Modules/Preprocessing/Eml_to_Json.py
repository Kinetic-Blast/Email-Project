import json
import eml_parser
import os
import datetime

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

def convert_eml_to_json(eml_file_path, save_as_file=False):
    ep = eml_parser.EmlParser(include_raw_body=True, include_attachment_data=True)

    try:
        temp_mail = ep.decode_email(eml_file_path)
        if save_as_file:
            output_path = os.path.splitext(eml_file_path)[0] + ".json"
            with open(output_path, "w") as json_file:
                json.dump(temp_mail, json_file, default=str, indent=2)
            print(f"JSON file saved successfully at {output_path}")
        return temp_mail
        
    except FileNotFoundError:
        print(f"Error: File not found - {eml_file_path}")
    except Exception as e:
        print(f"Error: An error occurred - {e}")
