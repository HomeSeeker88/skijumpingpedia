import requests
from bs4 import BeautifulSoup, ResultSet

from utils.consts import HOMOLOGATIONS


def read_homologations() -> tuple[ResultSet, ResultSet, ResultSet]:
    r = requests.get(HOMOLOGATIONS)
    soup = BeautifulSoup(r.content, "html.parser")
    cities = soup.find_all("div", class_ = "g-xs g-sm g-md g-lg justify-left bold")
    countries = soup.find_all("span", class_="country__name-short")
    rows = soup.find_all("div", class_="table-row pointer reset-padding")
    return cities,countries,rows


def prepare_data(cities: list[str], country: list[str], urls: list[str]) -> None:
    return None #TODO


if __name__ == "__main__":
    cities,countries, rows = read_homologations()
    for city, country, row in zip(cities, countries, rows):
        print(city.getText(),country.getText(), row["onclick"], type(row["onclick"]))


