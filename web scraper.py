import requests
from bs4 import BeautifulSoup

# URL of the news website
URL = "https://www.bbc.com/news"   # You can change to any public news website

def scrape_headlines():
    try:
        # Fetch the web page
        response = requests.get(URL)
        response.raise_for_status()  # Raise error for bad status codes

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines (h2 tags used by BBC)
        headlines = soup.find_all("h2")

        # Store text only
        extracted = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

        # Save to file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for line in extracted:
                file.write(line + "\n")

        print("✔ Headlines scraped and saved to headlines.txt")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    scrape_headlines()
