# BAN 201 lecture notes

Student-facing lecture notes for **BAN 201 Introduction to Business Analytics**, Nichols College, Fall 2026 (section 04). Weeks 1–4 are written so they can be published as a website in the same format as the [BDI 475 textbook](https://bdi475.github.io/textbook/): a Jupyter Book with a left-hand table of contents, one page per lecture, and assignments in their own section.

The notes follow the Fall 2026 syllabus (`BAN 201-04 PRICE FA26.pdf`) and the course slide decks `DS_201 Intro to BAn.pptx` and `DS 201 Descriptive Statistics.pptx`. Examples in the notes are original, so the pages can be posted for students. The HBS Online article used in Week 1 is cited on that page.

## Preview the site on your computer

From this folder:

```bash
pip install jupyter-book
jupyter book start
```

Jupyter Book opens a local site. The table of contents is `myst.yml`. Each lecture is a Markdown file in `content/`.

`instructor/` is the answer key for the in-class lab. It is **not** in the table of contents. Leave that folder out of any public GitHub Pages site.

MyST treats `$...$` as math. Write money amounts as `\$899` so they stay dollar signs.

## What is included

| Week of | Page | Syllabus topic |
| --- | --- | --- |
| Aug 25 | Week 1 | Introduction to business analytics |
| Sep 1 | Week 2, plus the in-class lab | Descriptive analytics |
| Sep 8 | Week 3 | Descriptive analytics wrap-up and first presentations |
| Sep 15 | Week 4 | More presentations |

There is no separate descriptive-analytics assignment file in the BAN 201 course folder. The syllabus names **AirBnB Prelim** and **Mini Project 2** for the week of September 1; those live on Canvas. The in-class lab is a 75-minute Excel activity students can finish during the Week 2 Friday class.
