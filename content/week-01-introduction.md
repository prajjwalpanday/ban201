# Week 1: Introduction to Business Analytics

**Week of Tuesday, August 25.** Two class meetings: Tuesday, August 25 and Friday, August 28.

This week answers three questions. What is business analytics? Why are companies investing in it? And what kinds of questions can data actually answer?

The four kinds of questions below are the map for the whole course. Weeks 2–4 stay on the first kind: describing what has already happened.

---

## Class 1 — Why this field grew, and what a decision is

### Three changes that made analytics ordinary

A generation ago, a careful manager could still run a business mostly on experience. Three changes arrived together, and together they made “look at the data” a normal part of the job.

1. **There is more data.** Scanners, online orders, social networks, and phones record what people do. A store can see which size sold, at what hour, after which ad.
2. **The methods got better.** Researchers built faster ways to search large files, to try many options, and to draw a picture of the data that a person can actually read.
3. **The computers caught up.** Storage is cheap, machines are fast, and **cloud computing** means a company can rent computing power over the internet instead of buying a room of servers.

Companies use that combination to run operations more efficiently, understand customers, set prices, and compete. The tool is only useful if someone asks a clear question and is honest about what the data can and cannot say. That is the skill this course is for.

### Decisions come in three sizes

A manager’s job is to decide. The decisions are not all the same size.

| Kind | What it settles | A campus example |
| --- | --- | --- |
| **Strategic** | The direction of the organization | The college store decides to open a second location by the athletic center. |
| **Tactical** | How to carry out that direction | Managers choose how many new staff to hire this semester, which products to stock there, and where the extra inventory will sit. |
| **Operational** | The day-to-day work | A shift lead decides how many hoodies to reorder on Friday and who works the Saturday game. |

:::{tip} In class
Pick a business you already know: a team, a campus job, a family store, a club. Name one strategic decision, one tactical decision, and one operational decision that business has made or might make. One sentence each.
:::

### A decision is a process

“Going with your gut” skips steps. A usable decision process has five:

1. Name the problem in a sentence other people can agree with.
2. List the criteria you will use to judge the options. Cost, time, risk, and fairness are common criteria.
3. List the real options. Include “do nothing” when that is a genuine choice.
4. Compare the options against the criteria.
5. Choose, and be able to say why.

Business analytics lives mostly in step 4. It turns data into evidence you can put next to the criteria. It does not replace the choice. A person still chooses.

### What “business analytics” means

**Business analytics** is the scientific process of turning data into insight for making better decisions. People also call this **data-driven** or **fact-based** decision making. The aim is a decision that other people can inspect: here is the question, here is the data, here is what we did with it, here is what we recommend.

Harvard Business School Professor Jan Hammond describes the skill underneath that process as data literacy: the ability to analyze, interpret, and question data. Catherine Cote’s article for HBS Online, linked below, is the reading for this week. It is written for business professionals, and it is the right level for this course.

:::{seealso} Read before Friday
Cote, Catherine. “4 Types of Data Analytics to Improve Decision-Making.” *Harvard Business School Online*, 19 Oct. 2021, updated 17 Nov. 2026, [https://online.hbs.edu/blog/post/types-of-data-analysis](https://online.hbs.edu/blog/post/types-of-data-analysis).

As you read, mark one example of each of the four types. Bring the examples to class.
:::

---

## The four analytics questions

Cote organizes business analytics into four types. Each type answers a different question. You can use one of them, or you can walk through them in order. Cote (2021) is the source for the four questions and for the console example in the next section. The short definitions here are the ones we will use all semester.

::::{grid} 1 1 2 2

:::{card}
:header: **1. Descriptive analytics**
:footer: *What happened?*
Uses current and historical data to summarize what already occurred. Reports, averages, counts, and charts live here. This is the work of Weeks 2–4.
:::

:::{card}
:header: **2. Diagnostic analytics**
:footer: *Why did it happen?*
Looks for the reasons behind a pattern. Comparisons, breakdowns, and careful tests live here. A descriptive result often raises the “why” question. It does not answer it by itself.
:::

:::{card}
:header: **3. Predictive analytics**
:footer: *What is likely to happen?*
Uses historical patterns to forecast. A forecast can be about later today or about next year. Regression, which this course reaches in late October, is one predictive tool.
:::

:::{card}
:header: **4. Prescriptive analytics**
:footer: *What should we do?*
Recommends an action. A forecast becomes prescriptive when you add a rule, such as “if the forecast says we will stock out, place the order.”
:::

::::

### One story, four questions

Cote uses a video game console to show how the four questions stack. Descriptive analytics notices that sales rise every October, November, and early December. Diagnostic analytics asks why, and finds that the buyers are mostly ages 35 to 55 while the players are mostly ages 8 to 18, which points to holiday gifts. Predictive analytics asks whether next year’s holiday will look similar, given a decade of the same spike. Prescriptive analytics asks what to do about it: for example, test two ads in September, one aimed at parents and one aimed at players, or start the holiday message earlier (Cote, 2021).

We will use a smaller story of our own. **Bison Beans** is the coffee shop in this set of notes. In Week 2 you will describe 20 summer weekdays of its sales. The descriptive question is “what happened in July?” The diagnostic question, which we will be careful with, is “why were some days higher?” The predictive question is “what might August have looked like?” The prescriptive question is “what should the manager do on the next rainy morning?”

| Question a manager asks | Type | Bison Beans, in one line |
| --- | --- | --- |
| How did July go? | Descriptive | Average daily sales, busiest drinks, slow days. |
| Why were Thursdays stronger? | Diagnostic | Break the days apart: promo days, rainy days, long waits. |
| What will the first week of classes look like? | Predictive | A forecast from the July pattern, said with uncertainty. |
| Should we staff an extra person on promo days? | Prescriptive | A rule tied to the forecast and to the cost of that person. |

:::{note} Where this course sits
Weeks 1–4 are descriptive on purpose. A clean description is what makes the later “why,” “what next,” and “what should we do” questions worth asking. Cote makes the same point: descriptive analytics is where you see the pattern; the other three types build on it (Cote, 2021).
:::

### Check

Write the type next to each question. Use descriptive, diagnostic, predictive, or prescriptive.

1. The bookstore sold 40 percent more sweatshirts in October than in September.
2. October was parents’ weekend, and the sweatshirt display moved to the front door. Both may have mattered.
3. Based on the last three Octobers, sweatshirt sales will probably rise again next October.
4. Order 200 more sweatshirts in the last week of September.

---

## Class 2 — What analysts actually produce

Friday is a tour of the products you will see in this course, plus the responsibilities that come with other people’s data.

### The descriptive toolkit

Descriptive analytics shows up in ordinary business objects. You will build several of these yourself.

| Product | What it is | You will see it when |
| --- | --- | --- |
| **Data query** | A request for rows that meet a condition, such as “all promo days” or “all rainy days.” | Week 2, with Excel’s filter. |
| **Report** | A table of counts, totals, or averages, updated on a schedule. | Weeks 2–4. |
| **Descriptive statistics** | A few numbers that stand in for a whole column: mean, median, a spread. | Week 2. |
| **Chart** | A picture of a pattern. A chart is still descriptive when it shows what already happened. | Week 3, and again in the visualization weeks. |
| **Dashboard** | A screen of tables, charts, and summary numbers that updates as new data arrives. A regional manager might watch sales and inventory. A shift lead might watch staffing and the next few hours of demand. | The Power BI weeks in October. |
| **What-if model** | A spreadsheet that shows how a result changes if one input changes. “What if the drink price goes up by 25 cents?” | Later Excel work. |

**Data mining** is the search for patterns in a large file. Two examples you will hear about again: **cluster analysis**, which groups similar customers or products, and **sentiment analysis**, which reads text such as reviews and scores the tone. Data mining can feed a description (“these are the groups we have”) or a prediction (“this group is likely to respond to a coupon”).

### A first look at prediction and prescription

Predictive work builds a model from past data to say what is likely, or to measure how one quantity moves with another. Names to recognize, without the math yet:

- **Linear regression** relates an outcome to one or more inputs. This course returns to it in late October.
- **Time series** methods follow a measurement across time, such as monthly sales.
- **Simulation** uses probability to study a decision when important inputs are uncertain. A bank might simulate loan defaults. The point is to see the range of outcomes, not a single lucky number.

A prediction is not yet a decision. Prescriptive analytics adds a rule or an objective. “Choose the mix of investments with the highest expected return while holding risk under a limit” is a **portfolio model**. “Place the warehouses so total cost is as low as possible and customers still get deliveries on time” is a **supply-network model**. “Mark down the unsold jackets on the date and by the amount that brings in the most revenue” is a **price-markdown model**. Models that search for the best choice under limits are **optimization models**.

When the future is uncertain, **simulation optimization** combines the two ideas: simulate the uncertainty, and search for a decision that works well across those simulated futures. **Decision analysis** is the version of this problem a person can do with a few clear options and a few possible futures, including how the decision maker feels about risk.

People sometimes call the predictive and prescriptive work **advanced analytics**. The name is a label for where you are in the stack. It is not a reason to skip the description.

### Big data, in four words

IBM’s picture of **big data** uses four V words. Big data means a collection that is too large or too messy for ordinary desktop tools.

| V | In plain language | A business example |
| --- | --- | --- |
| **Volume** | There is a lot of it. | A retailer recording every item on every receipt. |
| **Velocity** | It arrives quickly and keeps arriving. | A website logging clicks all day. |
| **Variety** | It comes in different shapes. | Spreadsheets, plus photos, plus comment text, plus sensor readings. |
| **Veracity** | Some of it is wrong, missing, or inconsistent, and you have to deal with that. | A customer typed a birth year of 2099. |

Two related ideas belong next to the four Vs.

**Data security** is the protection of stored data from loss and from people who should not have it. More data makes this a larger job.

The **Internet of Things (IoT)** is the set of sensors in machines, buildings, and vehicles that send measurements to a place where they can be stored and studied. A cooler that reports its own temperature is an IoT device.

Companies that live in this environment hire **data scientists**, people who can process and analyze very large collections. This course will not make you a data scientist in one semester. It will make you someone who can ask a data scientist a precise question and can read the answer.

### Where analytics shows up at work

Cote’s article lists the same idea from the employee’s side: marketers, product managers, finance staff, human resources, sales, operations, and supply-chain teams all use data, and so do people outside traditional business roles (Cote, 2021). The course slides group the business settings this way:

| Setting | A question analytics is asked to help with |
| --- | --- |
| **Financial analytics** | What return and what risk should we expect from this set of investments? |
| **Human resource analytics** | Are we hiring and keeping the skills the organization needs, including its diversity goals? |
| **Marketing analytics** | Which message, price, and product mix fit what customers actually do? Scanner data and social-media data made this one of the fastest-growing areas. |
| **Health care** | Which patients need attention sooner, and which treatments fit which patients? |
| **Supply chain** | Where should the product be, and when? |
| **Government and nonprofits** | Where should a limited budget go? |
| **Sports** | Which lineup, training load, or ticket price fits the evidence? |
| **Web analytics** | What do people do on the site, and which change is worth keeping? |

The marketing list is worth remembering, because it is concrete: better use of an advertising budget, pricing that fits demand, a forecast of that demand, a product line that matches what sells, and customers who stay.

:::{tip} In class
From the HBS article, pick the job closest to the work you want. Write the sentence from the article that describes how that job uses data, in your own words. Then write one decision in that job that is still a person’s decision after the analysis is done.
:::

### Using data is a responsibility

Customers and employees hand over data because they get something in return: a faster checkout, a saved order, a paycheck, a grade. The company has an obligation to protect that data and to avoid misusing it. The person has a reason to understand the tradeoff. The usual form of the agreement is a privacy notice or a consent form that both sides can actually read.

One of the strictest privacy laws is the **General Data Protection Regulation (GDPR)**, in effect in the European Union since May 2018. Four of its requirements are easy to remember, and they are good practice even when the law does not apply:

- The request for consent is written so a person can understand it.
- The organization says what it will use the data for.
- Withdrawing consent is easy.
- A person can ask for a copy of their data, and can ask that it be erased.

Analysts have matching duties. Protect the file. Be open about what was collected and what the file does not contain. Be open about the method and about the assumptions the method needs. Deliver a conclusion the client can understand, and a recommendation the client can act on or can question.

One course outcome sits inside this duty. Data can carry human bias into a predictive model. If a hiring file reflects an old pattern of who got interviews, a model trained on that file will learn the old pattern. Descriptive work is where you notice the pattern. You will return to this in the predictive weeks. For now, the habit is: ask who is in the data, who is missing, and who decided what to record.

### What is on Canvas this week

The syllabus lists two items for the week of August 25:

- **First Day Assignment**
- **Mini Project 1**

Both are posted on Canvas. These lecture notes do not replace those instructions. Friday is a good time to start Mini Project 1 if the Canvas page is open, using the five-step decision process from Class 1 as the outline.

### Check

1. Name the four Vs and give a one-line example of veracity from a job or a class you know.
2. A dashboard of today’s sales is which type of analytics?
3. A model that recommends the markdown percent for unsold jackets is which type?
4. Why does a descriptive summary belong before a predictive model?

---

## References

Cote, Catherine. “4 Types of Data Analytics to Improve Decision-Making.” *Harvard Business School Online*, Harvard Business School, 19 Oct. 2021, updated 17 Nov. 2026, [https://online.hbs.edu/blog/post/types-of-data-analysis](https://online.hbs.edu/blog/post/types-of-data-analysis). Hammond is quoted in that article; the quotation in Class 1 follows her wording there.
