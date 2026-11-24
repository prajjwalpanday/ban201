# Week 4: Presenting Findings

**Week of Tuesday, September 15.** Two class meetings: Tuesday, September 15 and Friday, September 18.

The syllabus uses this week for the rest of the descriptive-analytics presentations. One course outcome is the point of the assignment: summarize your findings for a **non-technical audience**. The listener is a manager, a client, or a teammate who did not build the spreadsheet. They need the question, the result, and the limit. They do not need every formula.

Tuesday is a rehearsal with a tight outline. Friday is the second round of briefings.

---

## Class 1 — Brief a person who will decide

### Who is in the room

Picture the Bison Beans manager at the start of a Tuesday shift. She has about three minutes. She can read a chart if the title tells her the point. She will ask “so what?” if the chart does not.

She is a smart audience. “Non-technical” means she should not have to know what `STDEV.S` does in order to use your result. It does not mean she needs a vague story.

### An outline that fits on one card

| Beat | Time | What you say |
| --- | --- | --- |
| 1. Question | 20 seconds | “I looked at what happened on 20 summer weekdays in July.” |
| 2. Data, in one breath | 20 seconds | “Twenty days of register totals, plus a sample of 50 drink orders. I kept every day in the file, including one unusual wait.” |
| 3. Findings | 90 seconds | Two or three sentences. Each one has a number and a comparison. Show one visual. |
| 4. What you would not conclude | 20 seconds | “Promo days were higher, and they were also nicer weather. I am not calling that a promo effect.” |
| 5. What you recommend looking at next | 30 seconds | A next step, labeled as a next step. “Next I would want a month where promos were planned on rainy days too.” |

Stay inside descriptive analytics unless you label the hop. “I would staff an extra person on sunny promo days” is a prescriptive idea. Say it as a hypothesis to test, or leave it in the “next” beat. The briefing’s job this month is the description.

### One visual

Bring one chart or one table, not a tour of the workbook.

A bar chart is a good default for categories: average sales for promo and non-promo, or drink counts for the five drinks. A column chart of the frequency bins works for a quantitative variable. A line across the 20 dates works for the time series, if the point you want to make is about a particular day.

Make the chart easy to defend:

- The title is the finding, not the column name. “Promo days averaged about \$1,116; other days averaged about \$806.”
- Both axes are labeled, with units.
- The source line is small and specific: “Bison Beans, 20 weekdays, July 6–31, 2026.”
- Gridlines are light. The ink goes to the bars and the labels.
- Categories with no natural order are sorted by the size of the bar. Dates stay in date order.
- You can state the group sizes. Six promo days and fourteen other days belong in the title or the speaker’s sentence.

If you show the July 31 wait, mark it. An outlier that appears with no comment looks like a chart error. An outlier that you name looks like you checked the file.

### Words that keep you accurate

| Say this | When |
| --- | --- |
| “In this file…” | You are about to give a number. |
| "About..." | The mean is rounded. \$898.86 can be "about \$899." |
| “averaged higher” | You compared two group means. |
| “The mode was latte, 16 of 50 orders.” | You are talking about the order sample, which is not the same as the 20-day file. |
| “I would want a file that…” | You are about to ask for evidence you do not have yet. |

Practice the three findings out loud and time them. If you run past three minutes, cut a finding. Do not talk faster.

:::{tip} In class
Pair up. One person gives the five-beat briefing with no slides, only the card. The listener may not look at the speaker’s workbook. Afterward the listener repeats the two findings in their own words. If the listener cannot repeat them, the findings are not ready. Switch roles.
:::

### A slide, if you use one

One slide is enough.

- Top: the question.
- Middle: the chart.
- Bottom: two findings and one limit, in short lines.

A paragraph on the slide competes with your voice. The slide holds the picture and the numbers. You hold the sentences.

---

## Class 2 — Second round of briefings

Friday continues the presentations. Use the same five beats. If you presented on September 11, use the feedback you received and change one thing: a clearer title, a causal word removed, or the outlier explained.

### Peer notes

For each speaker, write three lines:

1. **I heard this finding:** copy the number and the comparison as you heard them.
2. **A manager would still ask:** one question.
3. **One change that would help the next listener:** a title, a missing unit, a group size, or a word that overreached.

Keep the note about the briefing. “Speak louder” is fair if you could not hear the number. Comments about the person are out of place in this class.

### What “done” looks like for Weeks 1–4

You can move on to the visualization weeks when you can do all of the following without the notes in front of you:

- Name the four analytics questions from Week 1, and say which one a given sentence is asking.
- Point at a column and say whether it is quantitative or categorical, and whether the file is a time series or a cross-section.
- Produce a frequency table whose counts add up, plus a mean and a median.
- Flag an outlier with a z-score and say what you still need to find out.
- Brief a manager in three minutes, with one chart and one stated limit.

The next block of the course, starting the week of September 22, is data visualization in Excel. The charts you defended this week are the standard: a title that states the finding, labeled axes, and a picture that matches the question.

### Check

1. Who is the audience for the Friday briefing, and what do they need from you?
2. Where in the five beats does a recommendation belong?
3. Write a chart title for the rainy-day drink comparison that a manager can use without opening the workbook.
