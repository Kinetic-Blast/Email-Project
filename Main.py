from Modules.Preprocessing import Eml_to_Json
from Modules.processing.AIProcessing import AIAnalysis
from Modules.processing.VirusTotalChecks import CommonCheckDataCollection

email_to_analyse = Eml_to_Json.convert_eml_to_json("Emails/test 2.eml")


#quick version need to make a gui version and clean it up more but it works for now for user reading will work on a score system


################ API Key ############################

def read_api_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


################ Attachments #######################
def check_Attachments(email_to_analyse,apikey):

    if "attachment" in email_to_analyse:
        print("____________ Attachment Report ____________ \n")
        for attachment in email_to_analyse["attachment"]:

            print ("File Name: ",attachment["filename"])
            print("File extension: ",attachment["extension"])
            data = CommonCheckDataCollection.get_file_hash_report(attachment["hash"]["md5"],apikey)

            if data != "":
                data=data["data"]["attributes"]
                print("Current Virus Total Stats: ",data["total_votes"])
                print("Virus Total reputation: ",data["reputation"])
                print("Submitted Count: ", data["times_submitted"])
                print("Last Virus Total Stats",data["last_analysis_stats"])
                

                if "trid" in data:
                    for trid in data["trid"]:
                        print("File TrID:",trid["file_type"]," ",trid["probability"])

            else:
                print('No Data From Virus Total')

            print("\n")

    else:
        return "No Attachments"


################ Body ##############################


def check_Body(email_to_analyse,apikey):

    print("___________________ Body Text Check _________________\n")

    if "body" in email_to_analyse:
        for body in email_to_analyse["body"]:
            print("AI Body text output: ",AIAnalysis.ai_bodytext_analysis(body["content"]))
            print("Content Type: ", body["content_type"])

    #Scan URLS
            print("URLS in Email: ", body["uri"])
            print("URL Scans: Not working yet" )
    #Scan Domains
            print("Domains Listed: ", body["domain"])
            print("Domain Virus Total Scans: Not working yet") #to DO

            print("\n")


################### Headers #######################











######################  MAIN  ######################
apikey = read_api_file("Creds\VirusTotalAPI.txt")
check_Attachments(email_to_analyse,apikey)
check_Body(email_to_analyse,apikey)
