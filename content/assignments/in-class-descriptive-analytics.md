# In-class lab: Describe Bison Beans

**When:** Friday, September 4, the second meeting of Week 2. One class period.

**Tools:** Microsoft Excel on your laptop. The lecture page for the methods is [Week 2](../week-02-descriptive-analytics.md).

**Files:**

- [bison-beans-daily.csv](../data/bison-beans-daily.csv) — 20 summer weekdays at Bison Beans, July 6–31, 2026
- [bison-beans-orders.csv](../data/bison-beans-orders.csv) — a sample of 50 drink orders

**Turn in:** one Excel workbook and the five sentences in Part D. Your instructor will say whether that is Canvas, email, or a check before you leave.

This lab is the in-class descriptive-analytics assignment. The syllabus also lists **AirBnB Prelim** and **Mini Project 2** for this week. Do those from the Canvas instructions. This lab is the guided practice for the same skills.

## The business question

The manager asks: **What happened on these 20 summer weekdays, and which patterns are strong enough to mention in a staff meeting?**

You are doing descriptive analytics. Write what the file shows. Save “why” and “what we should do” for the last sentence, and label them as questions rather than as facts.

## Setup

1. Open both CSV files in Excel. Save the workbook as `BisonBeans_YourName.xlsx` with two sheets, named `Daily` and `Orders`.
2. On `Daily`, confirm you have 20 data rows and these headers: `Date`, `Weekday`, `Drinks_Sold`, `Food_Sold`, `Sales_Dollars`, `Avg_Wait_Minutes`, `Promo`, `Weather`.
3. On `Orders`, confirm you have 50 data rows and the headers `Order` and `Drink`.
4. Above the table on `Daily`, type the business question in a cell, so the sheet states what you are trying to describe.

`Sales_Dollars` was computed as `4.25 × drinks + 3.50 × food`. You do not need to rebuild that formula unless a row looks inconsistent. If you check one row by hand, say which date you checked.

## Part A — Look before you summarize

Do this on `Daily`.

1. Sort by `Sales_Dollars` from largest to smallest. Write down the date and the sales of the highest day and the lowest day. Then sort by `Date` from oldest to newest so the sheet is back in calendar order. (Data → Sort, with **My data has headers** checked. Sort the whole table.)
2. Filter to `Promo` = Yes. Record how many rows remain. Clear the filter.
3. Filter to `Weather` = Rain. Record how many rows remain, and whether any of those rows have `Promo` = Yes. Clear the filter.
4. Add a column `Sales_per_Drink` with the formula `=E2/C2` in the first data row, filled down. Format it as currency or as a number with two decimals. This is dollars of total sales for each drink sold. It mixes food into the same ratio, so the label matters: it is not the drink price.
5. Turn on data bars for `Sales_Dollars` (Home → Conditional Formatting → Data Bars). Leave them on for the checkup.

## Part B — Summaries

Build a small summary block to the right of the daily table, or on a new sheet named `Summary`. Use formulas, not typed numbers, so a change in the data would update the block.

From `Daily`:

- Count of days, mean, median, minimum, maximum, and sample standard deviation of `Sales_Dollars`.
- Mean and median of `Drinks_Sold`.
- Mean, median, and sample standard deviation of `Avg_Wait_Minutes`.
- Mean of `Sales_Dollars` for promo days, and the count of those days.
- Mean of `Sales_Dollars` for non-promo days, and the count of those days.
- Mean of `Drinks_Sold` for sunny days, and for rainy days, with both counts.

`AVERAGEIF` and `COUNTIF` are enough. For sunny days, if drinks are in `C2:C21` and weather is in `H2:H21`:

```text
=AVERAGEIF(H2:H21, "Sunny", C2:C21)
=COUNTIF(H2:H21, "Sunny")
```

From `Orders`, build the frequency table:

| Drink | Frequency | Relative frequency | Percent frequency |
| --- | --- | --- | --- |
| Latte |  |  |  |
| Iced Coffee |  |  |  |
| Cold Brew |  |  |  |
| Tea |  |  |  |
| Hot Chocolate |  |  |  |
| Total |  |  |  |

Use `COUNTIF`. Relative frequency is the count divided by the total. Percent frequency is relative frequency formatted as a percent. The frequencies must add to 50, and the relative frequencies must add to 1.

Name the mode in a cell next to the table.

## Part C — One extreme wait

1. Compute the z-score of each day’s `Avg_Wait_Minutes`.

```text
z = (wait − mean wait) / standard deviation of wait
```

Use the mean and the sample standard deviation from Part B. `STANDARDIZE` is allowed.

2. Flag any day with a z-score greater than 3 or less than −3. Conditional formatting on the z-score column is a clean way to show it.
3. In a nearby cell, write two possibilities: the wait really was that long, or the value was recorded wrong. Say which day it is. Do not delete the row.

## Part D — Five sentences

Type these in the workbook, on the `Summary` sheet, in your own words. You may use AI to check grammar. You may not use AI to produce the numbers or the comparisons. If you use an AI tool for wording, cite it in a sixth line and keep the prompt, as the syllabus requires. You need to be able to explain every figure from your own formulas.

1. One sentence on the center of daily sales: mean, median, and the dates of the high and low days.
2. One sentence comparing promo days with other days, including both averages and both counts.
3. One sentence comparing drinks sold on sunny days and rainy days, including both counts.
4. One sentence on the drink sample: the mode, its percent frequency, and the fact that this is 50 orders rather than 20 days.
5. One sentence that a manager still cannot answer from this file. Use what you saw when you filtered rain and promo together.

## Before you leave

- Filters are cleared, or the summary sheet does not depend on a hidden row.
- Every summary number is a formula.
- The five sentences use the words “in this file” or “these 20 days” at least once.
- You can point to the cell that produced each number in sentences 1–4.

## If you finish early

Add quartiles of `Sales_Dollars` with `QUARTILE.INC`, compute the interquartile range, and write one sentence that says what the middle half of the days covered. That sentence can replace nothing in Part D. It is extra practice for Week 3.
