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
  const absolute_value = value * 1000;
  let change = null;
  if (index > 0) {
    const previous_value = values[index - 1] * 1000;
    change =
      previous_value !== 0
        ? ((absolute_value - previous_value) / previous_value) * 100
        : null;
  }

  data.push({
    date: date.format("YYYY-MM-DD"),
    absolute_value: absolute_value,
    change: change, // Relative change as a decimal (e.g., 0.05 for 5%)
  });
}

export { data };
