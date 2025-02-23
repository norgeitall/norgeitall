const queryString = new URLSearchParams({
  licenceTypes: ["BANK"],
  page: 24,
}).toString();
const url = `https://api.finanstilsynet.no/registry/v1/legal-entities/filter?${queryString}`;

const response = await fetch(url);

if (!response.ok) {
  throw new Error(response.content);
}

const json = await response.json();

console.debug(json);

const bankLicences = [];

for (const legalEntity of json.legalEntities) {
  for (const licence of legalEntity.licences) {
    if (licence.licenceType.code !== "BANK") {
      continue;
    }
    bankLicences.push(licence);
  }
}

const bankNames = new Set();

for (const bankLicence of bankLicences) {
  bankNames.add(bankLicence.licensedEntity.legalEntityName);
}

console.debug(bankLicences);
