import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"  # Replace with the URL of the website you want to scrape
response = requests.get("https://hospitality.usc.edu/residential-dining-menus/?menu_venue=venue-27229&menu_date=03/22/2023")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    #links = soup.find_all("li") 
    li_elements = soup.find_all("li")
    for li in li_elements:
        print(li.get_text())
    
else:
    print("Failed to fetch the web page.")
    exit()
