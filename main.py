#!/usr/bin/env python
from csv import DictWriter
from datetime import date

from httpx import post


def main():
    response = post(
        "https://data.ssb.no/api/v0/no/table/10725/",
        json={
            "query": [
                {"code": "Formaal", "selection": {"filter": "item", "values": ["COF0"]}}
            ],
            "response": {"format": "json-stat2"},
        },
    )
    response.raise_for_status()
    data = response.json()
    years = data["dimension"]["Tid"]["category"]["index"]
    values = data["value"]
    observations = []
    for year, index in years.items():
        observations.append({"year": date(int(year), 12, 31), "value": values[index]})
    csv_file = "sources/ssb/government_expenses.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = DictWriter(file, fieldnames=observations[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(observations)

    print(f"CSV file '{csv_file}' created successfully!")
    pass


if __name__ == "__main__":
    main()
