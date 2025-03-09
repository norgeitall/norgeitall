

#Nominal wages come as 1000 of NOK per year. We want to show the real values in the graph

#Set value as lønn * 1000 if lønn isnt missing

```sql nominal_wages
select
    cast(date as date) as dato,
    case
        when value is null then null
        else value * 1000
    end as lønn
from nominal_wages
```

#Now to add a sql for nok_usd


```sql nok_usd
select
    cast(date as date) as dato,
    value as kurs
from nok_usd
```

#Line Chart for Nominal Wages

<LineChart
    data={nominal_wages}
    subtitle="Kilde: SSBs tabell 09786"
    title="Nominell lønn"
    x=dato
    y=lønn
    chartAreaHeight={500}
/>

#Line Chart for NOK per USD

<LineChart
    data={nok_usd}
    subtitle="Kilde: SSBs tabell 07917"
    title="NOK per USD"
    x=dato
    y=kurs
    chartAreaHeight={500}
/>

#Now lets make a chart for nominal wages in USD by converting the nominal wages to USD using the exchange rate

```sql nominal_wages_usd
select
    cast(nominal_wages.date as date) as dato,
    (nominal_wages.value / nok_usd.value) * 1000 as lønn_usd
from nominal_wages
join nok_usd
on cast(nominal_wages.date as date) = cast(nok_usd.date as date)
```

#Line Chart for Nominal Wages in USD

<LineChart
    data={nominal_wages_usd}
    subtitle="Kilde: SSBs tabell 09786 og 07917"
    title="Nominell lønn i USD"
    x=dato
    y=lønn_usd
    chartAreaHeight={500}
/>
