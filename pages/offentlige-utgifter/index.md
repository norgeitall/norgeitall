---
title: Offentlige utgifter
---

```sql government_expenses
select date as dato, value as offentlige_utgifter from government_expenses
```

<LineChart
    data={government_expenses}
    title="Offentlige utgifter i nominelle kroner"
    subtitle="Kilde: SSBs tabell 10725"
    x=dato
    y=offentlige_utgifter
    chartAreaHeight={500}
/>
