import requests

def read_ApiKey():
    try:
        with open("Creds/VirusTotalAPI.txt", 'r') as file:
            apikey = file.read()
            return apikey.strip()  # strip any leading/trailing whitespace

    except FileNotFoundError:
        print(f"Error: File 'Creds/VirusTotalAPI.txt' not found.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

badurl = ""

url = f"https://www.virustotal.com/api/v3/urls/{badurl}"

headers = {
    "accept": "application/json",
    "x-apikey": read_ApiKey()
}

response = requests.get(url, headers=headers)

print(response.text)

