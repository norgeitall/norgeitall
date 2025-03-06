#!/usr/bin/env python
from calendar import monthrange
from csv import DictWriter
from datetime import date
from pathlib import Path

from httpx import get, post, Response
from polars import read_csv


def main() -> None:
    get_absence_from_work_due_to_illness()
    get_nok_eur()
    get_cpi()
    get_real_wages()
    get_government_expenses_from_ssb()
    get_petroleum_fund_data()


def get_absence_from_work_due_to_illness() -> None:
    csv_url = "https://sdmx.oecd.org/public/rest/data/OECD.ELS.HD,DSD_HEALTH_STAT@DF_AWDI,1.0/DNK+SWE+NOR.A.CAWI..........?startPeriod=2007&format=csvfile"
    response = get(csv_url)
    dataframe = read_csv(response.content).sort(
        ["TIME_PERIOD", "REF_AREA"], descending=[True, False]
    )
    observations = []
    for row in dataframe.to_dicts():
        year = row["TIME_PERIOD"]
        _date = date(year, 12, 31)
        value = row["OBS_VALUE"]
        country = row["REF_AREA"]
        if country == "NOR":
            country = "Norge"
        elif country == "SWE":
            country = "Sverige"
        elif country == "DNK":
            country = "Danmark"
        observations.append(
            {
                "date": _date,
                "value": value,
                "country": country,
            }
        )
    delete_and_write_csv(observations, Path("sources/oecd/absence_illness.csv"))


def get_nok_eur() -> None:
    response = get(
        "https://data.norges-bank.no/api/data/EXR/A.EUR.NOK.SP?format=sdmx-json&lastNObservations=30&locale=en"
    )
    json = response.json()
    labels = json["data"]["structure"]["dimensions"]["observation"][0]["values"]
    values = json["data"]["dataSets"][0]["series"]["0:0:0:0"]["observations"]
    observations = []
    for index, label in enumerate(labels):
        value = values[str(index)][0]  # Get value or None if missing
        _date = label["end"].split("T")[0]
        observations.append(
            {
                "date": _date,
                "value": float(value),
            }
        )
    delete_and_write_csv(observations, Path("sources/norges_bank/nok_eur.csv"))


def get_cpi() -> None:
    response = _post(
        "https://data.ssb.no/api/v0/no/table/03013/",
        [
            {
                "code": "Konsumgrp",
                "selection": {
                    "filter": "vs:CoiCop2016niva1",
                    "values": ["TOTAL"],
                },
            },
            {
                "code": "ContentsCode",
                "selection": {
                    "filter": "item",
                    "values": ["Tolvmanedersendring"],
                },
            },
        ],
    )
    observations = simplify_jsonstat2(response)
    delete_and_write_csv(observations, Path("sources/ssb/cpi.csv"))


def get_real_wages() -> None:
    response = _post(
        "https://data.ssb.no/api/v0/no/table/09786/",
        [
            {
                "code": "ContentsCode",
                "selection": {
                    "filter": "item",
                    "values": ["RealArslonn"],
                },
            }
        ],
    )
    observations = simplify_jsonstat2(response)
    for observation in observations:
        observation["value"] *= 1_000
    delete_and_write_csv(observations, Path("sources/ssb/real_wages.csv"))


def get_petroleum_fund_data() -> None:
    url = "https://www.nbim.no/en/investments/the-funds-value/"
    response = get(url)
    text = response.text
    observations = parse_petroleum_fund_data(text)
    delete_and_write_csv(observations, Path("sources/nbim/fund_value.csv"))


def get_government_expenses_from_ssb() -> None:
    response = _post(
        "https://data.ssb.no/api/v0/no/table/10725/",
        [{"code": "Formaal", "selection": {"filter": "item", "values": ["COF0"]}}],
    )
    observations = simplify_jsonstat2(response)
    for observation in observations:
        observation["value"] = observation["value"] / 1000
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


def _post(url: str, query: list[dict]) -> Response:
    response = post(
        url,
        json={
            "query": query,
            "response": {"format": "json-stat2"},
        },
    )
    response.raise_for_status()
    return response


def simplify_jsonstat2(response: Response) -> list[dict]:
    json = response.json()
    time_periods = json["dimension"]["Tid"]["category"]["index"]
    values = json["value"]
    observations: list[dict] = []
    for time_period, index in time_periods.items():
        observation = {}
        try:
            observation["date"] = date(int(time_period), 12, 31)
        except ValueError:
            year, month = time_period.split("M")
            year = int(year)
            month = int(month)
            last_day = monthrange(year, month)[1]
            observation["date"] = date(year, month, last_day)
        observation["value"] = values[index]
        observations.append(observation)
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
