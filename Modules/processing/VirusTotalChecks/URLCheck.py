import requests

# def read_api_key():

#     try:
#         with open("Creds/VirusTotalAPI.txt", 'r') as file:
#             api_key = file.read().strip()  # Strip any leading/trailing whitespace
#             return api_key
#     except FileNotFoundError:
#         print("Error: File 'Creds/VirusTotalAPI.txt' not found.")
#         return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

def scan_url(url_to_scan,api_key):

    url = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": url_to_scan }

    headers = {
        "accept": "application/json",
        "x-apikey": api_key,
        "content-type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def get_url_report(vt_url,api_key):
    
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
        }

    try:
        response = requests.get(vt_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Example usage:
# if __name__ == "__main__":
#     scan_result = scan_url("www.google.com")
#     if scan_result:
#         url_report = get_url_report(scan_result.get("data", {}).get("links", {}).get("self"))
#         if url_report:
#             print(url_report)
