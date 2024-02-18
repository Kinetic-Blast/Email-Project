import requests
from urllib.parse import urlencode

def api_request(url, method='GET', params=None, data=None, files=None, headers=None):
    try:
        response = requests.request(method, url, params=params, data=data, files=files, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def scan_url(url_to_scan, api_key):
    url = "https://www.virustotal.com/api/v3/urls"
    payload = urlencode({"url": url_to_scan})
    headers = {
        "accept": "application/json",
        "x-apikey": api_key,
        "content-type": "application/x-www-form-urlencoded"}

    return api_request(url, method='POST', data=payload, headers=headers)

def get_url_report(vt_url, api_key):
    headers = {
        "accept": "application/json",
        "x-apikey": api_key}

    return api_request(vt_url, headers=headers)

def get_ip_report(ip, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key}

    return api_request(url, headers=headers)

def get_domain_report(domain, api_key):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key}

    return api_request(url, headers=headers)

def upload_file_for_scanning(file_dict, api_key):
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key}

    return api_request(url, method='POST', files=file_dict, headers=headers)

def get_file_hash_report(file_hash, api_key):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "Accept": "application/json",
        "x-apikey": api_key}
        
    return api_request(url, headers=headers)


