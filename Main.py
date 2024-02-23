from Modules.Preprocessing import Eml_to_Json
from Modules.processing.AIProcessing import AIAnalysis
from Modules.processing.VirusTotalChecks import CommonCheckDataCollection

#quick version need to make a gui version and clean it up more but it works for now for user reading will work on a score system

def read_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def check_attachments(email_data, api_key):
    attachments = email_data.get("attachment", [])

    if not attachments:
        print("No Attachments")
        return

    print("____________ Attachment Report ____________\n")

    for attachment in attachments:
        filename = attachment.get("filename", "Unknown")
        extension = attachment.get("extension", "Unknown")
        hash_md5 = attachment["hash"].get("md5", "")
        print("File Name: ", filename)
        print("File Extension: ", extension)
        data = CommonCheckDataCollection.get_file_hash_report(hash_md5, api_key)

        if data:
            data = data.get("data", {}).get("attributes", {})
            print("Current Virus Total Stats: ", data.get("total_votes", "Not available"))
            print("Virus Total Reputation: ", data.get("reputation", "Not available"))
            print("Submitted Count: ", data.get("times_submitted", "Not available"))
            print("Last Virus Total Stats: ", data.get("last_analysis_stats", "Not available"))
            trid_info = data.get("trid", [])

            for trid in trid_info:
                file_type = trid.get("file_type", "")
                probability = trid.get("probability", "")
                print("File TrID:", file_type, " ", probability)

        else:
            print('No Data From Virus Total')

        print("\n")

def check_body(email_data):
    print("___________________ Body Text Check _________________\n")
    bodies = email_data.get("body", [])

    if not bodies:
        print("No Body Text")
        return

    for body in bodies:
        content = body.get("content", "")
        content_type = body.get("content_type", "Unknown")
        uri = body.get("uri", [])
        domain = body.get("domain", [])

        print("AI Body text output: ", AIAnalysis.ai_bodytext_analysis(content))
        print("Content Type: ", content_type)
        print("URLs in Email: ", uri)
        print("URL Scans: Not working yet")
        print("Domains Listed: ", domain)
        print("Domain Virus Total Scans: Not working yet")  # To Do

        print("\n")

def main():
    email_to_analyse = Eml_to_Json.convert_eml_to_json("Emails/test 2.eml")
    api_key = read_api_key("Creds/VirusTotalAPI.txt")
    check_attachments(email_to_analyse, api_key)
    check_body(email_to_analyse)

if __name__ == "__main__":
    main()
