---
title: Dag 1
---

```sql cpi
select
    cast(date as date) as date,
    twelve_month_change
from cpi
```

<LineChart
    data={cpi}
    title="Konsumprisindeksen"
    x=date
    y=twelve_month_change
/>
