import requests
import xml.etree.ElementTree as ET
import csv

# Fetch the sitemap
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get('https://fijiguide.com/post-sitemap.xml', headers=headers)
sitemap_content = response.text

# Print the beginning and end of the content for inspection
print("Beginning of the content:\n", sitemap_content[:500])  # first 500 characters
print("\nEnd of the content:\n", sitemap_content[-500:])  # last 500 characters

# Define the namespaces
namespaces = {
    'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9',
    'image': 'http://www.google.com/schemas/sitemap-image/1.1'
}

# Try to parse the sitemap content
try:
    root = ET.fromstring(sitemap_content)
    # Extract URLs
    urls = [elem.text for elem in root.findall(".//sitemap:loc", namespaces=namespaces)]
    
    # Generate search terms from the URLs
    terms = []
    for url in urls:
        # Extract the relevant part of the URL
        term = url.rstrip('/').split('/')[-1]
        # Replace '-' with spaces
        term = term.replace('-', ' ')
        terms.append((term, url))
    
    # Define the filename
    filename = "sitemaps-fiji-travel.csv"
    
    # Save the terms and URLs to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(["Term", "URL"])
        # Write the terms and URLs
        for term, url in terms:
            writer.writerow([term, url])
    
    print(f"\nData saved to {filename}")
    
except ET.ParseError as e:
    print("\nError parsing XML:", e)