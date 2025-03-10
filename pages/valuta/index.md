---
title: Valuta
---

```sql eur_ten_years
WITH historical AS (
    SELECT
        cast(date as date) as dato,
        value as pris
    FROM nok_eur
    WHERE date = (SELECT MAX(date) FROM nok_eur WHERE date <= CURRENT_DATE - INTERVAL '10 years')
),
current AS (
    SELECT
        cast(date as date) as dato,
        value as pris
    FROM nok_eur
    WHERE date = (SELECT MAX(date) FROM nok_eur WHERE date <= CURRENT_DATE)
)
SELECT
    c.dato AS dagens_dato,
    h.dato AS historisk_dato,
    c.pris AS dagens_pris,
    h.pris AS historisk_pris,
    ROUND(((c.pris - h.pris) / h.pris) * 100) AS prosent_endring
FROM current c
JOIN historical h ON 1=1;
```

Prisen vi må betale for utenlandsk valuta er en indikator på hvor bra det går med økonomien vår. Ved utgangen av fjoråret betalte vi <Value data={eur_ten_years} column=prosent_endring />prosent mer for en Euro enn vi gjorde ti år tidligere:

```sql nok_eur
select
    cast(date as date) as dato,
    value as pris
from nok_eur
```

<LineChart
    data={nok_eur}
    subtitle="Kilde: Norges Bank"
    title="Pris for én Euro"
    x=dato
    y=pris
/>
