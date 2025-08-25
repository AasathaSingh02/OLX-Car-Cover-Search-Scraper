import requests
from bs4 import BeautifulSoup
import pandas as pd
def scrape_olx_car_cover():
url = "https://www.olx.in/items/q-car-cover"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers)
if response.status_code != 200:
print("Failed to fetch OLX page. Status code:", response.status_code)
return
soup = BeautifulSoup(response.text, "html.parser")
results = []
ads = soup.find_all("li", {"data-aut-id": "itemBox"})
for ad in ads:
title = ad.find("span", {"data-aut-id": "itemTitle"})
price = ad.find("span", {"data-aut-id": "itemPrice"})
location = ad.find("span", {"data-aut-id": "itemLocation"})
link_tag = ad.find("a", href=True)
results.append({
"Title": title.text.strip() if title else "N/A",
"Price": price.text.strip() if price else "N/A",
"Location": location.text.strip() if location else "N/A",
"Link": "https://www.olx.in" + link_tag["href"] if link_tag else "N/A"
})
# Save to CSV
df = pd.DataFrame(results)
df.to_csv("olx_car_cover_results.csv", index=False, encoding="utf-8")
print("■ Scraping completed. Results saved to olx_car_cover_results.csv")
if __name__ == "__main__":
scrape_olx_car_cover()
