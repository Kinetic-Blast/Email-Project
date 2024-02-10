import requests

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
