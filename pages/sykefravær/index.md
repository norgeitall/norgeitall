---
title: Sykefravær
---

```sql absence_illness
select
    *
from absence_illness
order by date desc
limit 20
```

<LineChart
    data={absence_illness}
    x=date
    y=value
    series=country
    subtitle="Kilde: OECD"
    title="Sykefraværsdager per innbygger i året"
/>
