# Design — One Sentence for a Traveler from 1800

## The entry (132 chars, one sentence)

> It is one coffeehouse holding every newspaper and letter in the world,
> where you may ask anything and hear the world answer at once.

## Lane choice

Live field re-checked 24 Nov 13:07 WIB (552 subs): road 157 titles,
library 131, post office 99, letter 93, ink 41. The judge brief's own
examples (road / post office / library) are the most flooded lane on the
board — following them means fighting 150 near-identical entries in
pairwise games. Coffeehouse: 0 titles. Almanac: 0. Bell: 0.
A coffeehouse is genuinely 1800-known (London coffeehouses from the 1650s),
and it carries the two things the internet is — the world's writings at
hand, and anyone in the world answering back — in one room the traveler can
picture. The almanac lane was the runner-up; it explains knowledge well but
not conversation.

## 1800 word audit (every noun/verb in the entry)

coffeehouse (1650s), newspaper (1670s), letter, world, ask, hear, answer,
at once — all pre-1800. Avoided: wire, telegraph (1830s), lightning, glass
hall, village square, "before the ink dries", "before your tea cools" (all
flooded), "instant", any list of features. "Hear the world answer" is the memorable phrase;
"may ask anything" states a capability, not a guaranteed reply, so the
sentence stays literally true as a comparison.

## Tournament — 10 candidates, judge criteria in strict order

C1 Coffeehouse, answered cup: "Picture a coffeehouse where every newspaper
on earth arrives at once, and a letter you write there is answered before
you finish your cup." (138)
C2 Coffeehouse, open papers: "A coffeehouse where every newspaper in the
world lies open at once, and any letter you write may reach any door on
earth before your cup is empty." (146)
C3 Almanac: "Picture an almanac that rewrites itself each morning, holding
every book and letter in the world and answering any question you ask it."
(135)
C4 Coffeehouse, three verbs: "Imagine a coffeehouse where you may read
every newspaper on earth, speak with any soul alive, and have your letter
answered before your cup cools." (146)
C5 Bell: "Picture a church bell whose ring carries your letter to any door
on earth and brings the answer back before the sound fades." (124)
C6 Coffeehouse, ask/answer (WINNER): "It is one coffeehouse holding every
newspaper and letter in the world, where you may ask anything and hear the
world answer at once." (132)
C7 Almanac, breakfast: "An almanac that rewrites itself each morning, so
any question finds its answer and any letter reaches any door before
breakfast ends." (133)
C8 Coffeehouses squeezed: "Picture every coffeehouse on earth squeezed
into one room, its newspapers, letters, and voices all arriving at your
table at once." (130)
C9 Coffeehouse, warm cup: "Sit in one coffeehouse and ask it anything, for
every newspaper on earth lies open there and every letter you write is
answered while your cup is warm." (151)
C10 Almanac, news/books: "Picture an almanac that rewrites itself each
morning with the whole world's news, books, and letters, answering any
question you put to it." (139)

## Bracket and elimination reasons

- R1 C1 vs C2: C2 wins. Criterion 3 — C1 promises a reply ("is answered");
  C2 hedges to a true capability ("may reach").
- R1 C3 vs C10: C3 wins. Criterion 4 — C10 lists three items (news, books,
  letters); C3 says the same in two.
- R1 C4 vs C9: C4 wins. Criterion 1 — C4 covers reading, speaking, writing;
  C9 covers less, and its "is answered" overpromises.
- R1 C5 vs C8: C8 wins. Criterion 1 — C5 explains messaging only; C8 also
  covers newspapers and voices, the knowledge side.
- R1 C6 vs C7: C6 wins. Criterion 1 — "ask anything, hear the world
  answer" is the two-way internet; the almanac is one-way reference.
- R2 C2 vs C3: C2 wins. Criterion 3 — C3's "answering any question" implies
  every question gets an answer; C2 stays a hedged capability.
- R2 C4 vs C8: C8 wins. Criterion 4 — C4 is a three-verb list; C8 is one
  image, no list.
- R3 C2 vs C8: C2 wins. Criterion 1 — C2 has the traveler acting (write a
  letter, it reaches a door); C8 is passive arrival at a table.
- Final C2 vs C6: C6 wins. Criterion 1 — asking and being answered by the
  world is the internet's defining act; newspapers lying open plus letters
  is the older, static half of it. C6 is also 14 chars shorter (criterion 4)
  and its closing phrase is the more memorable one (criterion 5).

## Program

`main.py` holds the sentence as one constant, checks 1–200 chars and one
sentence, and writes `/output/entry.txt` with no trailing newline; no clock,
random, network or input, so two runs are byte-identical.
