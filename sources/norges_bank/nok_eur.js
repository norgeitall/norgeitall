import dayjs from "dayjs";

const url =
  "https://data.norges-bank.no/api/data/EXR/A.EUR.NOK.SP?format=sdmx-json&lastNObservations=30&locale=en";

const response = await fetch(url, {
  method: "GET",
});

if (!response.ok) {
  throw new Error(response.content);
}

const json = await response.json();
const labels = json.data.structure.dimensions.observation[0].values;
const values = json.data.dataSets[0].series["0:0:0:0"].observations;
const data = [];

for (const [index, label] of labels.entries()) {
  const value = values[index][0];
  const date = dayjs(label.end);
  data.push({
    date: date.format("YYYY-MM-DD"),
    value: parseFloat(value),
  });
}

export { data };
