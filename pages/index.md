---
title: Dag 1
---

Velkommen til Dag 1. Målet med Dag 1 er å få i gang igjen veksten i norsk økonomi.

Men hva betyr _Dag 1_?

> Dag-1-samfunn kan skape økonomiske mirakler. Dag-2-samfunn vil ødelegge dem.
>
> …
>
> Terminologien er lånt av Jeff Bezos, grunnlegger av Amazon. Bezos er nærmest manisk opptatt av å sikre at Amazon for alltid vil være det han kaller et dag-1-selskap. Et dag-1-selskap er vitalt, i stadig vekst og utvikling og evner å raskt gripe nye muligheter. I [sitt brev til Amazons aksjonærer i 2016](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) beskriver han også dag 2: Dag 2 er stagnasjon. Etterfulgt av irrelevans. Etterfulgt av pinefullt forfall. Etterfulgt av død. Et slikt forfall vil typisk skje i ekstrem sakte film som gjerne kan ta tiår.
>
> — [_Landet som ble for rikt: Hvordan Norge endte i oljefondets felle_](https://www.landetsombleforrikt.no/), Martin Bech Holte, sidene 24 og 321.

## Stagnasjon

Norge har stagnert. Det er ingen krise ennå, men det er tydelig at noe har skjedd. La oss se på noen tall som viser dette.

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

```sql eur_ten_years
WITH historical AS (
    SELECT
        cast(date as date) as dato,
        value as pris
    FROM nok_eur
    WHERE date = (SELECT MAX(date) FROM nok_eur WHERE date <= CURRENT_DATE - INTERVAL '10 years')
),
current AS (
    SELECT
        cast(date as date) as dato,
        value as pris
    FROM nok_eur
    WHERE date = (SELECT MAX(date) FROM nok_eur WHERE date <= CURRENT_DATE)
)
SELECT
    c.dato AS dagens_dato,
    h.dato AS historisk_dato,
    c.pris AS dagens_pris,
    h.pris AS historisk_pris,
    ROUND(((c.pris - h.pris) / h.pris) * 100) AS prosent_endring
FROM current c
JOIN historical h ON 1=1;
```

Prisen vi må betale for utenlandsk valuta er en annen indikator på hvor bra det går med økonomien vår. Ved utgangen av 2024 betalte vi <Value data={eur_ten_years} column=prosent_endring />prosent mer for én Euro enn vi gjorde for ti år siden:

```sql nok_eur
select
    cast(date as date) as dato,
    value as pris
from nok_eur
```

<LineChart
    data={nok_eur}
    subtitle="Kilde: Norges Bank"
    title="Pris for én Euro"
    x=dato
    y=pris
    chartAreaHeight={500}
/>
