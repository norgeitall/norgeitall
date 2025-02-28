---
title: Offentlige utgifter
---

```sql government_expenses
select date as dato, value as offentlige_utgifter from government_expenses
```

> Hold øye med én ting og bare én ting: hvor mye penger myndighetene bruker, for det er den egentlige skatten.
>
> —Milton Friedman

<LineChart
    data={government_expenses}
    title="Offentlige utgifter i nominelle kroner"
    subtitle="Kilde: SSBs tabell 10725"
    x=dato
    y=offentlige_utgifter
    chartAreaHeight={500}
/>
