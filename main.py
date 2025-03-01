#!/usr/bin/env python
from csv import DictWriter
from datetime import date
from pathlib import Path

from httpx import get, post, Response


def main() -> None:
    get_government_expenses_from_ssb()
    get_petroleum_fund_data()


def get_petroleum_fund_data() -> None:
    url = "https://www.nbim.no/en/investments/the-funds-value/"
    response = get(url)
    text = response.text
    observations = parse_petroleum_fund_data(text)
    delete_and_write_csv(observations, Path("sources/nbim/fund_value.csv"))


def get_government_expenses_from_ssb() -> None:
    response = _post(
        "https://data.ssb.no/api/v0/no/table/10725/",
        {"code": "Formaal", "selection": {"filter": "item", "values": ["COF0"]}},
    )
    observations = simplify_jsonstat2(response)
    delete_and_write_csv(observations, Path("sources/ssb/government_expenses.csv"))


def parse_petroleum_fund_data(text: str) -> list[dict]:
    line: str | None = None
    for _line in text.splitlines():
        if _line.startswith("data: [[Date.UTC(1998,11, 31),172]"):
            line = _line
            break
    assert isinstance(line, str)
    line = line[8:]
    line = line[:-2]
    rows = line.split("],[")
    observations: list[dict] = []
    for row in rows:
        cells = row.split("),")
        year = cells[0][9:13]
        year = int(year)
        value = int(cells[1])
        observations.append({"date": date(year, 12, 31), "value": value})
    return observations


def _get(url: str) -> Response:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = get(url, headers=headers)
    response.raise_for_status()
    return response


def _post(url: str, query: dict) -> Response:
    response = post(
        url,
        json={
            "query": [
                query,
            ],
            "response": {"format": "json-stat2"},
        },
    )
    response.raise_for_status()
    return response


def simplify_jsonstat2(response: Response) -> list[dict]:
    json = response.json()
    years = json["dimension"]["Tid"]["category"]["index"]
    values = json["value"]
    observations: list[dict] = []
    for year, index in years.items():
        observations.append({"date": date(int(year), 12, 31), "value": values[index]})
    return observations


def delete_and_write_csv(observations: list[dict], path: Path) -> None:
    delete_file_if_exists(path)
    with path.open(mode="w", newline="", encoding="utf-8") as file:
        writer = DictWriter(
            file,  # type: ignore
            fieldnames=observations[0].keys(),
            delimiter=";",
        )
        writer.writeheader()
        writer.writerows(observations)


def delete_file_if_exists(path) -> None:
    path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
