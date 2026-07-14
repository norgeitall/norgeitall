---
title: Konsumpriser
---

Statistisk sentralbyrå beregner endringen i prisene for forbruksgoder:

```sql cpi
select
    cast(date as date) as date,
    value as 'tolvmånedersendring'
from cpi
order by date desc
```

<BigValue
  data={cpi}
  value=tolvmånedersendring
  title="Siste tolvmånedersendring i prosent"
/>

<LineChart
    data={cpi}
    title="Konsumprisindeksen, 12-månedersendring"
    subtitle="Kilde: SSBs tabeller 03013 (til og med 2025) og 14700 (fra og med 2026)"
    x=date
    y=tolvmånedersendring
/>
