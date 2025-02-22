---
title: Dag 1
---

> Dag-1-samfunn kan skape økonomiske mirakler. Dag-2-samfunn vil ødelegge dem.
>
> …
>
> Terminologien er lånt av Jeff Bezos, grunnlegger av Amazon. Bezos er nærmest manisk opptatt av å sikre at Amazon for alltid vil være det han kaller et dag-1-selskap. Et dag-1-selskap er vitalt, i stadig vekst og utvikling og evner å raskt gripe nye muligheter. I [sitt brev til Amazons aksjonærer i 2016](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) beskriver han også dag 2: Dag 2 er stagnasjon. Etterfulgt av irrelevans. Etterfulgt av pinefullt forfall. Etterfulgt av død. Et slikt forfall vil typisk skje i ekstrem sakte film som gjerne kan ta tiår.
>
> —[_Landet som ble for rikt: Hvordan Norge endte i oljefondets felle_](https://www.landetsombleforrikt.no/), Martin Bech Holte, sidene 24 og 321.

```sql real_wages
select
    cast(date as date) as date,
    value
from real_wages
```

<LineChart
    data={real_wages}
    subtitle="Kilde: SSB tabell 09786"
    title="Reallønn i 2010-kroner"
    x=date
    y=value
    chartAreaHeight={500}
/>
