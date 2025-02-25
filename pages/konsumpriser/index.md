---
title: Konsumpriser
---

Statistisk sentralbyrå beregner endringen i prisene for forbruksgoder:

```sql cpi
select
    cast(date as date) as date,
    twelve_month_change
from cpi
```

<LineChart
    data={cpi}
    title="Konsumprisindeksen, 12-månedersendring"
    subtitle="Kilde: SSBs tabell 03013"
    x=date
    y=twelve_month_change
    chartAreaHeight={500}
/>
