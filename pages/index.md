---
title: Dag 1
---

```sql cpi
select * from cpi
```

<LineChart
    data={cpi}
    title="Konsumprisindeksen"
    x=date
    y=twelve_month_change
    sort={false}
/>
