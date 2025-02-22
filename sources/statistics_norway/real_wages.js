import dayjs from "dayjs";

const url = "https://data.ssb.no/api/v0/no/table/09786/";

const query = {
  query: [
    {
      code: "ContentsCode",
      selection: {
        filter: "item",
        values: ["RealArslonn"],
      },
    },
  ],
  response: {
    format: "json-stat2",
  },
};

const response = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(query),
});

if (!response.ok) {
  throw new Error(response.content);
}

const json = await response.json();
const values = json.value;
const labels = Object.values(json.dimension.Tid.category.label);
const data = [];

for (const [index, value] of values.entries()) {
  const label = labels[index];
  const date = dayjs(label).endOf("year");
  data.push({
    date: date.format("YYYY-MM-DD"),
    value: value * 1000,
  });
}

export { data };
