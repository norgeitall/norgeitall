---
title: Lønn
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
    subtitle="Kilde: SSB-tabell 09786"
    title="Reallønn i 2010-kroner"
    x=dato
    y=lønn
    chartAreaHeight={500}
/>
