# Week 3: From Numbers to a Finding

**Week of Tuesday, September 8.** Two class meetings: Tuesday, September 8 and Friday, September 11.

The syllabus calls this week a wrap-up: finish the descriptive work in class, and start the presentations. Read this page after the [Week 2 lab](assignments/in-class-descriptive-analytics.md). The numbers below are the Bison Beans file, so they will match the workbook you built if the formulas are right.

Tuesday is about the sentence you can stand behind. Friday is the first round of short briefings.

---

## Class 1 — A finding is a sentence with a job

A spreadsheet is not yet a result. A **finding** is one sentence that answers “what happened?” for a person who will make a decision. It has three parts:

1. **The number**, with the units and the time window.
2. **The comparison** that makes the number mean something.
3. **The business reading**, still inside what the table can support.

Weak: “Sales were good.”

Stronger: “Over the 20 summer weekdays in this file, Bison Beans averaged about \$899 a day, and the six promo days averaged about \$1,116 while the other 14 days averaged about \$806.”

The second sentence can be checked. The first cannot.

### The story in this file

Use your own workbook first. Then compare it with this summary of `bison-beans-daily.csv` and `bison-beans-orders.csv`.

**What the 20 days add up to.** Total sales were \$17,977.25. The mean daily sales were about \$899, and the median was about \$907, so the center of the file is near \$900 a day. The lowest day was Tuesday, July 28, at \$553. The highest was Wednesday, July 29, at \$1,228.50. The range is \$675.50. The sample standard deviation of daily sales is about \$187, so a day that lands \$200 away from the mean is a real swing for this shop, not a rounding error.

**Drinks.** The shop sold about 156 drinks on a typical day (mean about 155.9, median 156.5).

**The order sample.** Of 50 orders, 16 were lattes (32 percent), 12 were iced coffee (24 percent), 9 were cold brew (18 percent), 8 were tea (16 percent), and 5 were hot chocolate (10 percent). The mode is Latte. The top three drinks are 74 percent of this sample.

**Two comparisons.** Promo days (6 of them) averaged about \$1,116 in sales. Days without a promo averaged about \$806. Sunny days averaged about 172 drinks. Rainy days averaged about 112 drinks. There were 10 sunny days, 6 cloudy days, and 4 rainy days.

**One outlier.** Average wait on Friday, July 31 was 14.5 minutes. The mean wait in the file is about 5.6 minutes, and the sample standard deviation is about 2.6 minutes. The z-score for 14.5 is about 3.5, past the usual +3 cutoff. That row stays in the file until someone checks it. A 14-minute average wait is either a bad afternoon the manager should remember, or a number that was entered wrong. Both possibilities matter, and they are different decisions.

### A comparison is still a description

The promo gap is large. It is also tangled with the weather. Of the six promo days, four were sunny and two were cloudy. None of the four rainy days was a promo day. A manager who says “the promo caused an extra \$300” is answering a *why* question with a file that mixed two things together.

That sentence belongs to diagnostic analytics, and this file is not an experiment. Nobody assigned the promo at random, and rain did not fall at random across promo and non-promo days. The honest descriptive sentences are:

- Promo days in this file had higher average sales than other days.
- Rainy days in this file had fewer drinks than sunny days.
- Promo and sunshine showed up together, so the two gaps are not separate pieces of evidence.

Week 1’s warning about bias sits in the same place. The file records the days the shop chose to run a promo. If those days were chosen because a game, a tour, or good weather was already on the calendar, the column `Promo` contains that choice. A later model that treats promo as a simple cause will inherit the choice.

:::{tip} In class
Write three findings from your workbook. Each one is a single sentence. At least one finding must be a comparison of groups. At least one sentence, separate from the findings, must say what you are not claiming yet.

Then trade with a partner. Underline the number, the comparison, and any word that sneaks in a cause (“because,” “drove,” “the effect of”). Rewrite the causal word into a descriptive one if the study did not assign the condition.
:::

### A checklist before you present

Go through this list on Tuesday and fix the workbook before Friday’s briefing.

- The question is written at the top: “What happened at Bison Beans on these 20 summer weekdays?”
- Every column you use is labeled quantitative or categorical.
- Filters are off, or you have stated which rows the filter keeps. A hidden row is easy to forget, and an average of the visible rows is a different average.
- Counts of a category add up to the number of observations. Relative frequencies add to 1.
- Mean and median are both reported for sales and for wait time.
- The outlier is named, its z-score is shown, and you say whether you kept it.
- Group averages say how many days are in the group. An average of 4 rainy days is a thinner fact than an average of 10 sunny days.
- Charts have a title that states the pattern, axis titles, and units. A chart of weather with three bars is enough. Sort bars from largest to smallest when the axis is a category with no natural order. Keep calendar order when the axis is time.
- The last paragraph separates “what we see” from “what we would need in order to say why.”

### Common ways a good file becomes a weak briefing

- The mean is reported with no window of time and no comparison.
- Percent frequency and frequency get swapped. “32 lattes” and “32 percent lattes” are different facts. This sample has 16 lattes, which is 32 percent.
- One chart tries to show sales, drinks, wait, and weather at once. Split them.
- The title of the chart is the name of the column (“Sales_Dollars”) instead of the pattern (“Promo days averaged higher sales in this July file”).
- The speaker drops the outlier because it “messed up the average,” and does not say so.

:::{note} Mini Project 2 and the AirBnB work
The syllabus puts **AirBnB Prelim** and **Mini Project 2** on the week of September 1, and it puts wrap-up and presentations on this week and next. Use the same checklist on the Canvas data set. If your Mini Project file is ready, brief that file on Friday. If it is still in progress, brief Bison Beans. Either way, the sentence structure is the same.
:::

### Check

1. Rewrite “Rain hurt sales” as a descriptive finding that uses the drink counts.
2. Why is the July 31 wait a row to investigate rather than a row to delete on sight?
3. Why does “four of six promo days were sunny” change how you talk about the promo gap?

---

## Class 2 — First briefings

Friday is a working presentation day. The full speaking structure is on the [Week 4 page](week-04-presenting-findings.md). For this first round, use a shorter version.

### Three minutes, four beats

1. **Question.** What happened, and in what window of time?
2. **Data.** How many observations, and which variables you actually used.
3. **Two findings.** Each one has a number and a comparison. Point at one chart or one table while you say it.
4. **Limit.** One sentence on what this file cannot yet answer.

Practice once out loud before you come up. Three minutes is short. The findings have to be chosen, not listed.

### While you listen

For each speaker, write:

- The clearest number you heard.
- One question a manager would still ask.
- One word that claimed a cause, if you heard one.

You will hand that slip to the speaker. The slip is feedback on the briefing, not a grade of the person. Week 4 uses a slightly longer form of the same habit.
