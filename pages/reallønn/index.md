---
title: Reallønn
---

Reallønnsveksten avtok rundt 2013, og i 2016 hadde gjennomsnittsnordmannen for første gang siden 1989 dårligere råd enn året før:

```sql real_wages
select
    cast(date as date) as dato,
    value as lønn
from real_wages
```

<LineChart
    data={real_wages}
    subtitle="Kilde: SSBs tabell 09786"
    title="Reallønn i 2010-kroner"
    x=dato
    y=lønn
/>

<Alert status="warning">
    SSB sluttet å oppdatere reallønn i tabell 09786. De siste tallene er fra 2024. Jeg spurte dem om dette i april 2026, og fikk til svar at de er i ferd med å utarbeide en ny tabell som vil dekke noe av det samme.
</Alert>

Reallønnen sank også i 2022 og 2023, før den i 2024 hentet seg opp til 2021-nivået.

```sql joined
select
    cast(real_wages.date as date) as real_wages_date,
    real_wages.value as lønn,
    fund_value.value as fondsverdi
from real_wages
full outer join fund_value on fund_value.date = real_wages.date
order by real_wages_date
```

Hvordan kan dette ha seg? Martin Bech Holte behandler dette spørsmålet i boken [_Landet som ble for rikt: Hvordan Norge endte i Oljefondets felle_](https://www.landetsombleforrikt.no/). Han argumenterer for at Oljefondet kombinert med manglende begrensninger i pengebruk har ført til dårligere reallønnsutvikling i Norge.

For å vurdere denne påstanden kan vi se reallønnsutviklingen i sammenheng med Oljefondets størrelse:

<LineChart
    data={joined}
    subtitle="Kilde: SSBs tabell 09786, NBIM"
    title="Reallønn i 2010-kroner sett i sammenheng med Oljefondets verdi i milliarder kroner"
    x=real_wages_date
    y=lønn
    y2=fondsverdi
/>
