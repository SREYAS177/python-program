import requests

def get_virustotal_report(file_hash, api_key):
    """
    Fetches the analysis report for a file hash from VirusTotal API v3
    and displays the number of malicious detections.
    """
    # VirusTotal v3 API endpoint for files
    url = f"https://virustotal.com{file_hash}"
    
    # Authenticate via the custom header required by VirusTotal
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            json_data = response.json()
            
            # Navigate through the nested JSON structure to get analysis stats
            attributes = json_data.get("data", {}).get("attributes", {})
            analysis_stats = attributes.get("last_analysis_stats", {})
            
            # Extract specific detection counts
            malicious_count = analysis_stats.get("malicious", 0)
            harmless_count = analysis_stats.get("harmless", 0)
            suspicious_count = analysis_stats.get("suspicious", 0)
            undetected_count = analysis_stats.get("undetected", 0)
            
            print(f"\n[+] Analysis Results for Hash: {file_hash}")
            print(f"--------------------------------------------------")
            print(f"🔴 Malicious Detections : {malicious_count}")
            print(f"🟢 Harmless             : {harmless_count}")
            print(f"🟡 Suspicious           : {suspicious_count}")
            print(f"⚪ Undetected           : {undetected_count}")
            
        elif response.status_code == 404:
            print(f"[-] File hash {file_hash} not found in VirusTotal database.")
        elif response.status_code == 401:
            print("[-] Unauthorized: Please check if your API key is valid.")
        else:
            print(f"[-] Error: Received status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] An error occurred during the request: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Replace with your actual VirusTotal API key
    API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"
    
    # Example SHA-256 hash (e.g., a known clean or malicious file hash)
    sample_hash = "6408b5177b4c8c1e1338a8e22393e4d319e17b8d4f40f090d8a5c3701dfc1363"
    
    if API_KEY == "YOUR_VIRUSTOTAL_API_KEY_HERE":
        print("Please replace 'YOUR_VIRUSTOTAL_API_KEY_HERE' with a valid key to run the script.")
    else:
        get_virustotal_report(sample_hash, API_KEY)
