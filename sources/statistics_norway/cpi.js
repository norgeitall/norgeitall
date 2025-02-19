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
  throw new Error(response.content);
}

const json = await response.json();
const values = json.value;
const labels = Object.values(json.dimension.Tid.category.label);

let data = []

for (const [index, value] of values.entries()) {
  const label = labels[index];
  const month = label.replace("M", "-")
  data.push({
    month: month,
    twelve_month_change: value,
  })
}
// const labels = json.

console.log(data);


// const data = transformData(json);

console.log("Hello")
//
// function transformData(jsonStatData) {
//   if (!jsonStatData || !jsonStatData.value) return [];
//
//   const dimension = jsonStatData.dimension.Tid;
//   const labels = dimension[Object.keys(dimension)[0]].category.index;
//   const values = jsonStatData.value;
//
//   let data = Object.keys(labels).map((key, index) => ({
//     category: labels[key],
//     value: values[index]
//   }));
//
//   return data;
// }
export { data };
