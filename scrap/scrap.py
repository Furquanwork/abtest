import requests
from bs4 import BeautifulSoup
import difflib

def fetch_html(url):
    response = requests.get(url)
    return response.text

def save_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def compare_and_save_diff(file1, file2, diff_file):
    with open(file1, 'r', encoding='utf-8') as file:
        html1 = file.readlines()
    with open(file2, 'r', encoding='utf-8') as file:
        html2 = file.readlines()

    differ = difflib.HtmlDiff()
    diff_content = differ.make_file(html1, html2)

    with open(diff_file, 'w', encoding='utf-8') as file:
        file.write(diff_content)

if __name__ == "__main__":
    # URLs of the websites you want to scrape
    url1 = "https://causalfunnel.wixsite.com/causalfunnel?siteRevision=26"
    url2 = "https://causalfunnel.wixsite.com/causalfunnel"

    html1 = fetch_html(url1)
    html2 = fetch_html(url2)

    save_html(html1, "website1.html")
    save_html(html2, "website2.html")

    compare_and_save_diff("website1.html", "website2.html", "difference.html")
