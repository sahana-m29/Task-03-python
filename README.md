# Task-03-python
# News Headlines Web Scraper

This project is a simple Python web scraper that fetches the latest news
headlines from a public news website (BBC News by default) and saves
them into a `.txt` file.

------------------------------------------------------------------------

## 🚀 Features

-   Scrapes news headlines automatically
-   Uses **requests** to fetch webpage content
-   Uses **BeautifulSoup** to parse HTML
-   Saves extracted headlines into `headlines.txt`
-   Easy to run in Visual Studio Code or any Python environment

------------------------------------------------------------------------

## 📁 Files

-   `web_scraper.py` → Main Python script\
-   `headlines.txt` → Output file containing extracted headlines

------------------------------------------------------------------------

## 🛠 Requirements

Install dependencies using:

``` bash
pip install requests beautifulsoup4
```

------------------------------------------------------------------------

## ▶️ How to Run

1.  Save the Python script as `web_scraper.py`
2.  Open a terminal in the same folder
3.  Run the script:

``` bash
python web_scraper.py
```

4.  After running, check `headlines.txt` for the output.

------------------------------------------------------------------------

## 📝 Script Used

``` python
import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    URL = "https://www.bbc.com/news"

    try:
        print("Fetching news headlines...")

        response = requests.get(URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h2")

        extracted = [
            h.get_text(strip=True)
            for h in headlines
            if h.get_text(strip=True)
        ]

        with open("headlines.txt", "w", encoding="utf-8") as file:
            for line in extracted:
                file.write(line + "\n")

        print("✔ Headlines scraped and saved to headlines.txt")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    scrape_headlines()
```

------------------------------------------------------------------------

## ✔ Outcome

You will automatically collect top news data from a public website and
store it in a text file --- a great introductory task for web scraping!
