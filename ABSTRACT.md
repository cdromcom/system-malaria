---
page_type: executive brief
audience: decision-makers, no biomedical or statistical background assumed
created: 2026-11-14
updated: 2026-11-14
human_reviewed: no
---

# Are malaria parasites outrunning our drugs?

**An executive brief on what the published evidence shows, and how much of it there is.**

## The question

Malaria is caused by a parasite[^parasite] carried by mosquitoes. We treat it with drugs, and the
parasite evolves ways to survive those drugs. Certain changes in the parasite's genes[^marker]
act as warning signs that a drug is failing. We asked a single question: how far has that
resistance actually gone, according to everything researchers have published?

## What we did

We read an open database[^graph] holding roughly six million research findings and pulled out
every one concerning the seven parasite genes linked to drug resistance. That gave **222 findings
from 118 separate studies, published between 1987 and 2025**. We then checked each paper for signs
of unreliability, and whether its data could be obtained by anyone wanting to repeat the work.

## What we found

**Resistance genes do predict treatment failure.** Of 30 findings linking a resistance gene to
whether treatment worked, **28 pointed the same way (93%)**, meaning almost every study agreed
that patients carrying these genes were more likely to see treatment fail. Agreement this strong across four
genes studied independently is the most dependable result here. Individual effects
were large: one study found patients with a particular mutation had **24.7 times the odds**[^or]
of treatment failure, with a range of 8.2 to 74.2[^ci] (so the true figure is uncertain, but
clearly far above "no effect").

**Resistance rises and falls with drug use.** Of 110 findings on how common these genes are,
**82 reported them becoming more common and 26 less common (76% agreement)**. Both directions are
expected. Resistance spreads while a drug is in heavy use and recedes after health programmes
switch to a different drug. A falling figure therefore signals a policy change, and should not be read as a
retreating parasite.

**No clear link to severe illness.** Of 11 findings on whether these genes make patients sicker,
**6 pointed one way and 5 the other (55%, close to a coin flip)**. The evidence does not support
claims in either direction.

**The most urgent gene is the least studied.** One gene, Pfkelch13, governs resistance to
artemisinin[^art], the drug family underpinning every current frontline treatment, and resistance
has recently appeared in East Africa. It has just **18 findings**, against 89 and 77 for two
older, less threatening genes. Evidence is thinnest exactly where the risk is newest.

## How far to trust this

Encouraging: **none of the 118 papers has been retracted**[^retract] or formally questioned.

Concerning: the database's own documentation states that roughly **one finding in five is
misread** by its automated extraction. Only **30 of our 222 findings (14%)** appear in the
publisher's quality-checked release. And only **6 of 118 papers shared their underlying data,
with 3 sharing their analysis code**, so almost nothing here can be independently re-checked.

## What this means

Treat the treatment-failure signal as solid enough to act on. Treat severity claims as unproven.
Fund surveillance and data sharing on Pfkelch13 as a priority, because the gene that matters most
is the one we currently know least about.

---

[^parasite]: *Plasmodium falciparum*, a single-celled organism. It is neither a bacterium nor
a virus, which is why ordinary antibiotics have no effect on it.

[^marker]: Called a "resistance marker". Genes are instructions written in a chemical code; a
small change in that code can alter a protein just enough that a drug no longer binds to it.
Markers are written like `K76T`, meaning the building block at position 76 changed from K to T.

[^graph]: The System Public Graph, an open database that automatically extracts statistical
results from published research papers.

[^or]: An "odds ratio" compares how often two things occur together. A value of 1 means no
relationship at all. Values above 1 mean the two occur together more often than chance would
predict, and the further above 1, the stronger the link.

[^ci]: A "confidence interval" is the range the true value plausibly sits in, given that the study
only measured a sample of patients rather than everyone. A wide range means the study was small or
the outcome was rare. When the range stays entirely above 1, the finding is considered
statistically reliable.

[^art]: Artemisinin is a fast-acting malaria drug, always given alongside a slower partner drug.
Losing it would leave no equally effective replacement in current use.

[^retract]: "Retracted" means a journal formally withdrew a paper, usually for error or
misconduct. Four of our papers carry a correction notice, which is a smaller fix to a specific
mistake rather than a withdrawal of the whole paper.
