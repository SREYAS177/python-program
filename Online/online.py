
import requests

def get_virustotal_report(file_hash, api_key):
    """
    Fetches the file analysis report from VirusTotal API v3.
    """

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            json_data = response.json()

            attributes = json_data.get("data", {}).get("attributes", {})
            analysis_stats = attributes.get("last_analysis_stats", {})

            malicious_count = analysis_stats.get("malicious", 0)
            harmless_count = analysis_stats.get("harmless", 0)
            suspicious_count = analysis_stats.get("suspicious", 0)
            undetected_count = analysis_stats.get("undetected", 0)

            print("\n[+] Analysis Results for Hash:", file_hash)
            print("--------------------------------------------------")
            print("Malicious Detections :", malicious_count)
            print("Harmless             :", harmless_count)
            print("Suspicious           :", suspicious_count)
            print("Undetected           :", undetected_count)

        elif response.status_code == 404:
            print("[-] File hash not found in VirusTotal database.")

        elif response.status_code == 401:
            print("[-] Unauthorized: Please check your API key.")

        elif response.status_code == 403:
            print("[-] Access denied. Check your API permissions or quota.")

        else:
            print("[-] Error: Received status code", response.status_code)

    except requests.exceptions.RequestException as e:
        print("[-] An error occurred:", e)


# Main Program
if __name__ == "__main__":

    API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"

    sample_hash = "6408b5177b4c8c1e1338a8e22393e4d319e17b8d4f40f090d8a5c3701dfc1363"

    if API_KEY == "YOUR_VIRUSTOTAL_API_KEY_HERE":
        print("Please add a valid VirusTotal API key to run the script.")
    else:
        get_virustotal_report(sample_hash, API_KEY)
