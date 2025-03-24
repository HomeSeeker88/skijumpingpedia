import requests
from bs4 import BeautifulSoup, ResultSet


def read_homologations() -> ResultSet:
    r = requests.get("https://www.fis-ski.com/DB/ski-jumping/homologations.html")
    soup = BeautifulSoup(r.content, "html.parser")
    soup.prettify()
    s = soup.find_all('div', class_ = "table-row pointer reset-padding")
    return s


if __name__ =="__main__":
    content = read_homologations()
    print(content)