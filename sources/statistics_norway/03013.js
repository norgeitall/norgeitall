let url = "https://data.ssb.no/api/v0/no/table/03013/";

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
  throw new Error(`HTTP error! Status: ${response.status}`);
}

const json = await response.json();
const data = transformData(json);

console.log("Hello")

function transformData(jsonStatData) {
  if (!jsonStatData || !jsonStatData.value) return [];

  const dimension = jsonStatData.dimension.Tid;
  const labels = dimension[Object.keys(dimension)[0]].category.index;
  const values = jsonStatData.value;

  let data = Object.keys(labels).map((key, index) => ({
    category: labels[key],
    value: values[index]
  }));

  return data;
}
export { data };
