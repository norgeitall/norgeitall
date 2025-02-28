---
title: Offentlige utgifter
---

```sql government_expenses
select year as 'år', value as 'offentlige utgifter' from government_expenses
```

<LineChart
    data={government_expenses}
    x=år
    y='offentlige utgifter'
    chartAreaHeight={500}
/>
