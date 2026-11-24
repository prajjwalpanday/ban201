# Week 2: Descriptive Analytics

**Week of Tuesday, September 1.** Two class meetings: Tuesday, September 1 and Friday, September 4.

Descriptive analytics answers **what happened**. This week you learn the words analysts use for a data set, and then you describe one in Excel.

Friday’s class is the [in-class lab](assignments/in-class-descriptive-analytics.md). Read Class 1 before Tuesday. Bring a laptop with Excel on Friday.

The running example is **Bison Beans**, a campus coffee shop. The lab file is 20 weekdays in July 2026. The small examples in the Tuesday lecture are separate, so Friday’s numbers are yours to calculate.

---

## Class 1 — Words for a data set

### Four words you will use all semester

| Word | Meaning | In the Bison Beans daily file |
| --- | --- | --- |
| **Data** | Facts and figures collected so they can be analyzed and presented. | The whole spreadsheet. |
| **Variable** | One characteristic that can take different values. | `Sales_Dollars`, `Weather`, `Promo`. Each column is a variable. |
| **Observation** | The values of the variables for one case. | One row: one date. |
| **Variation** | The way a variable differs from one observation to the next. | Sales are not the same every day. That difference is the reason to analyze the file. |

A **random variable** (also called an uncertain variable) is a quantity whose value is not known for certain before you observe it. Tomorrow’s sales are a random variable today. Once the day is over and the register closes, that day’s sales are data.

The point of collecting the past values is to learn how the business varies. A single “typical day” is a summary. The variation around it is often the more useful fact.

### Population and sample

The **population** is every case you actually care about. The **sample** is the subset you have in front of you.

If the manager wants to understand Bison Beans on ordinary summer weekdays, the population might be all summer weekdays. The file has 20 of them. Those 20 days are the sample. A **random sample** is drawn so that each member of the population has a chance to be included. A random sample is the kind that can stand in for the population.

The July file is a slice of consecutive weekdays, not a random draw from every day the shop has ever opened. You can describe these 20 days with confidence. Extending the description to “the shop always…” needs more caution, and you should say so.

### Numbers and categories

**Quantitative data** are values you can add, subtract, multiply, or divide in a way that still means something. Drinks sold, dollars, and wait time in minutes are quantitative.

**Categorical data** name groups. Arithmetic on the labels does not mean anything. `Weather` (Sunny, Cloudy, Rain) and `Promo` (Yes, No) are categorical. You can count how many days fall in each group. You cannot add “Sunny” to “Rain.”

`Weekday` is categorical even though the calendar is ordered. Monday is not “1 more than Sunday” in the file. You can still choose to list the days in calendar order when you make a table.

:::{tip} In class
Open `bison-beans-daily.csv`, or look at the header below. Label each column quantitative or categorical.

`Date`, `Weekday`, `Drinks_Sold`, `Food_Sold`, `Sales_Dollars`, `Avg_Wait_Minutes`, `Promo`, `Weather`
:::

### One moment, or many moments

**Cross-sectional data** are collected from several cases at the same time, or nearly the same time. A survey of 30 customers on one Friday afternoon is cross-sectional. Each customer is a case, and the clock time is about the same.

**Time series data** are collected over several time periods. The Bison Beans daily file is a time series: one shop, many dates. A graph of a time series is often the first descriptive picture, because it shows the path, the spikes, and the quiet stretches.

The orders file you will use on Friday (`bison-beans-orders.csv`) is a sample of 50 purchases. Each row is one order. That file is a cross-section of purchases, not a clock of the whole summer.

### Where data come from

In an **experiment**, the researcher picks the variable they care about, then controls or changes one or more other variables to see what happens. A café could randomly choose which weekdays get a poster at the library door, then compare sales. Because the researcher assigned the poster, a difference in sales is easier to read as an effect of the poster.

In an **observational study**, nobody assigns the conditions. The analyst records what occurred. A customer comment card is a common observational study: overall experience, greeting, wait, food, each rated Excellent, Good, Average, Fair, or Poor. Those ratings are categorical. They tell the manager where the morning went well. They do not, by themselves, prove which change would fix a low score.

Companies also already have data: receipts, schedules, inventory, card swipes. Much of business analytics starts with a file that exists because the business was running, not because someone designed an experiment.

The Bison Beans promo column is observational in this file. The shop ran promotions on some days. Those days also had their own weather. On Friday and again in Week 3, keep that in mind when you compare averages.

### Check

1. In the daily file, what is one observation?
2. Why is `Promo` categorical?
3. Why is the daily file a time series?
4. The shop did not flip a coin to decide promo days. What kind of study is that, and what should you be careful about when promo days have higher sales?

---

## Class 2 — Describe it in Excel

Friday is the lab. This section is the method. Work the tiny examples with the instructor, then switch to the [Bison Beans lab](assignments/in-class-descriptive-analytics.md) and do the calculations there.

Download both files before class, or open them from Canvas if your instructor posts them there:

- [bison-beans-daily.csv](data/bison-beans-daily.csv) — 20 weekdays
- [bison-beans-orders.csv](data/bison-beans-orders.csv) — 50 drink orders

In Excel, use **Data → From Text/CSV**, or double-click the file if it opens cleanly as a sheet. Save your work as an Excel workbook (`.xlsx`) so your formulas survive.

### Sort, filter, and conditional formatting

These three tools are how you look at a file before you summarize it.

**Sort** reorders rows by a column. To sort a sheet that has headers: select the whole table, including the header. **Data → Sort**. Check **My data has headers**. Choose the column and the order (largest to smallest, or A to Z). Excel moves the entire row, so the date stays with its sales.

**Filter** hides rows that do not match. Select the table, **Data → Filter**. Use the arrow in the header. Uncheck **(Select All)**, check the values you want, then OK. A filter is a data query. To see every row again, check **(Select All)** or turn Filter off.

**Conditional formatting** marks cells that meet a rule. Select the column. **Home → Conditional Formatting → Highlight Cells Rules**. “Less than 0” is the usual rule for a percent-change column when you want the declines. **Data bars**, under Conditional Formatting, draw a bar inside the cell. The bar’s length follows the value, which makes a large number and a small number visible before you build a chart.

A percent change from an old value to a new value is:

```text
= (New - Old) / Old
```

Format the cell as a percent. A result of −0.08 is an 8 percent decline.

### Frequency for categories

A **frequency distribution** counts how many observations fall in each **bin**. For categories, the bins are the category names.

Here is a sample of 10 snack-stand purchases, small enough to count by hand:

Chips, Cookie, Chips, Fruit, Chips, Cookie, Pretzel, Cookie, Chips, Fruit.

| Snack | Frequency | Relative frequency | Percent frequency |
| --- | ---: | ---: | ---: |
| Chips | 4 | 0.40 | 40% |
| Cookie | 3 | 0.30 | 30% |
| Fruit | 2 | 0.20 | 20% |
| Pretzel | 1 | 0.10 | 10% |
| **Total** | **10** | **1.00** | **100%** |

- **Frequency** is the count.
- **Relative frequency** is the count divided by the total number of observations. Chips are 4/10 = 0.40.
- **Percent frequency** is the relative frequency times 100.

The relative frequencies add to 1, and the percent frequencies add to 100. If they do not, a count is wrong.

In Excel, if the drink names are in `B2:B51`, the count of Lattes is:

```text
=COUNTIF(B2:B51, "Latte")
```

Relative frequency is that count divided by `=COUNTA(B2:B51)`.

The **mode** is the value that appears most often. In the snack stand, the mode is Chips. A quantitative column can have a mode too, but for categories the mode is usually the more interesting summary.

### Frequency for numbers

Quantitative data need bins you define. Three choices, made together:

1. **How many bins.** Somewhere between 5 and 20 is typical. A small file, like 20 days, can use about 5 bins. Too few bins hide the shape. Too many bins leave most bins almost empty.
2. **How wide each bin is.** Use the same width for every bin.

```text
Approximate bin width = (largest value − smallest value) / number of bins
```

Round the width to a number a person can read, often up to a nearby whole number.

3. **The bin limits.** Each value belongs to one bin. The lower limit is the smallest value that goes in the bin. The upper limit is the largest. If you decide a bin is “500 up to but not including 650,” write that down and use it the same way in every formula.

A tiny example, “minutes to make a drink,” with 10 observations:

2, 3, 3, 4, 4, 4, 5, 5, 7, 9.

Largest 9, smallest 2, four bins: approximate width (9 − 2) / 4 = 1.75, so use a width of 2.

| Minutes | Frequency |
| --- | ---: |
| 2–3 | 3 |
| 4–5 | 5 |
| 6–7 | 1 |
| 8–9 | 1 |
| **Total** | **10** |

Most drinks in this sample were made in 4 or 5 minutes. One took 9. That is a description of these 10 drinks.

A **histogram** is the chart for this table. The horizontal axis is the variable, marked with the bins. The vertical axis is the frequency, the relative frequency, or the percent frequency. Each bin is a rectangle whose height is that bin’s frequency. The rectangles touch, because the bins cover a continuous range.

In current Excel you can select the quantitative column and use **Insert → Histogram**. For a file this small, building the frequency table with `COUNTIFS` and then inserting a column chart teaches you more, because you can see the limits. The lab tells you which one to do.

Histograms show **shape**. **Skewness** means the distribution is not symmetric.

- A **right tail** (skewed right) stretches toward large values. A few very large numbers pull it. Prices and incomes often look like this.
- A **left tail** (skewed left) stretches toward small values. A set of exam scores piled up near the top, with a few low scores, often looks like this.
- A **symmetric** shape has tails that mirror each other. Heights of adults are a common example.

### Location and spread

These summaries answer “what is a typical value?” and “how spread out are the values?”

| Measure | What it says | Excel, if the values are in `E2:E21` |
| --- | --- | --- |
| **Mean** | The arithmetic average. Add the values and divide by how many there are. | `=AVERAGE(E2:E21)` |
| **Median** | The middle value once the column is sorted. Half the observations are at or below it, half at or above. | `=MEDIAN(E2:E21)` |
| **Mode** | The most common value. | `=MODE.SNGL(E2:E21)` |
| **Range** | Largest minus smallest. One pair of points controls it. | `=MAX(E2:E21)-MIN(E2:E21)` |
| **Standard deviation** | A typical distance from the mean. Larger means more spread. For a sample, Excel’s `STDEV.S` divides by *n − 1*. | `=STDEV.S(E2:E21)` |

The mean uses every value, so one extreme day moves it. The median stays with the middle of the list, so it is steadier when one day is unusual. Report both when they differ.

A **percentile** is a cutoff. The *p*th percentile is a value where about *p* percent of the observations fall below it, and the rest fall above it. **Quartiles** cut the data into four parts of about 25 percent each.

- Q1 is the 25th percentile.
- Q2 is the median, the 50th percentile.
- Q3 is the 75th percentile.

The **interquartile range (IQR)** is Q3 − Q1. It is the spread of the middle half of the data, so the most extreme points do not control it the way they control the range.

```text
=QUARTILE.INC(E2:E21, 1)
=QUARTILE.INC(E2:E21, 2)
=QUARTILE.INC(E2:E21, 3)
```

### A value’s place in the list: the z-score

A **z-score** says how many standard deviations a value sits from the mean.

```text
z = (value − mean) / standard deviation
```

A z-score of 0.25 means the value is one quarter of a standard deviation above the mean. A z-score of −0.25 means it is one quarter of a standard deviation below the mean. In Excel, `=STANDARDIZE(value, mean, stdev)` does the arithmetic.

A common rule of thumb: a value with a z-score below −3 or above +3 is an **outlier**, an extreme value. Then you investigate. Sometimes the number was typed wrong, and you correct it. Sometimes the row does not belong in this population, and you set it aside and say that you did. Sometimes the value is real and unusual, and it stays in the file because it is part of the story. The lab asks you to do this investigation in writing.

For data that really do form a symmetric bell shape, the **empirical rule** is a useful check. About 68 percent of the values fall within 1 standard deviation of the mean, about 95 percent within 2, and nearly all within 3. If your histogram is strongly skewed, do not force this rule onto it.

A **boxplot** is a picture built from the quartiles. The box runs from Q1 to Q3, a line marks the median, and whiskers extend to the smallest and largest values that are not flagged as extreme. Excel can draw one from a column (**Insert → Box and Whisker**). You will read one before you are asked to build many of them. The IQR is the height of the story: a tall box means the middle half of the days were far apart.

### Two variables at once

A **scatter chart** plots two quantitative variables, one on each axis. Each observation is a point. The chart is descriptive. It shows whether the points rise together, fall in opposite directions, or form no straight-line pattern.

The **correlation coefficient** *r* summarizes the straight-line part of that picture.

| Value of *r* | Straight-line pattern |
| --- | --- |
| Greater than 0 | Positive: the points tend to rise together. |
| Near 0 | No straight line. A curve can still be sitting in the picture. |
| Less than 0 | Negative: one variable tends to be high when the other is low. |

*r* is near +1 or −1 when the points hug a straight line. It only measures the line. A U-shape can have *r* near 0 and still be a strong pattern, which is why the chart and the number belong together.

Here is a six-day illustration, not the lab data. Iced drinks sold against the afternoon high temperature:

| High °F | Iced drinks |
| ---: | ---: |
| 70 | 40 |
| 75 | 55 |
| 80 | 70 |
| 85 | 90 |
| 90 | 110 |
| 95 | 130 |

The points rise together. That is a positive linear pattern. You would expect *r* > 0. You would not yet say “temperature causes iced-drink sales.” People also buy iced drinks because of habit, menu placement, and price. The chart describes the six days.

`Promo` is categorical, so it does not go on a scatter axis as a number you invented. For a category, compare the mean of the quantitative variable inside each group. That comparison is still descriptive. Friday’s lab asks for it.

### What to turn in

Finish the [in-class lab](assignments/in-class-descriptive-analytics.md) before you leave, or by the end of the day if your instructor extends it. The syllabus also lists **AirBnB Prelim** and **Mini Project 2** this week. Those instructions are on Canvas. The lab is the in-class practice that uses the same skills.

### Check

Answer from the snack-stand table and the drink-time table. Save the Bison Beans arithmetic for the lab.

1. What percent of snack purchases were cookies?
2. Which bin of drink-prep times has the highest frequency?
3. Why can one unusual day move the mean more than it moves the median?
4. A wait time has a z-score of 3.4. What do you do before you delete the row?
