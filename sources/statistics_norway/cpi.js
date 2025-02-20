import dayjs from 'dayjs';

const url = "https://data.ssb.no/api/v0/no/table/03013/";

const query = {
  query: [
    {
      code: "Konsumgrp",
      selection: {
        filter: "vs:CoiCop2016niva1",
        values: ["TOTAL"]
      }
    },
    {
      code: "ContentsCode",
      selection: {
        filter: "item",
        values: ["Tolvmanedersendring"]
      }
    }
  ],
  response: {
    format: "json-stat2"
  }
};

const response = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(query)
});

if (!response.ok) {
  throw new Error(response.content);
}

const json = await response.json();
const values = json.value;
const labels = Object.values(json.dimension.Tid.category.label);
const data = []

for (const [index, value] of values.entries()) {
  const label = labels[index];
  const month = label.replace("M", "-")
  const date = dayjs(month).endOf('month')
  data.push({
    date: date.format('YYYY-MM-DD'),
    twelve_month_change: value,
  })
}

export { data };
