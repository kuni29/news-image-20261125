# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/kuni29/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/kuni29/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world news of Wednesday 25 November 2026, drawn as a newspaper front page in a graphic-recording style. The hero is a three-panel triptych joined by a single "world line" arrow: mines hit three tankers in the Strait of Hormuz (and Houthis strike Riyadh's tallest tower again, 11 hurt), Russian strikes knock out power in five Ukrainian regions while two Rosneft refineries burn in Samara, and Shenzhou-24 docks at Tiangong with Pakistan's first astronaut — the first foreign astronaut aboard China's station. A "how today connects" arrow flow links the Hormuz blasts to Brent at $91.40 and the Nvidia slide to Asia's sell-off. Two more hero stories (the AI rally stalling as the Dow tops 50,000; Gaza's strike and the storm threatening 1.76 million people in tents), three mid stories (Real Madrid's 5-1 Champions League comeback, the Australia–Solomon Islands security treaty, Huawei's US conviction), a labelled atlas strip marking eight places where the day happened, and 24 one-line briefs from every region — 32 stories in all, each colour-coded by category with a legend. Every story was first reported on 25 November 2026; stories first reported on 24 November or earlier (the COP31 collapse, the Abu Dhabi talks, Putin's "inevitable" retaliation remark itself) were left out of the headlines or tagged with their day, and the page carries a DATE-CHECKED stamp. The picture is designed in `design.html` with hand-drawn inline SVG illustrations and rendered to `entry.png` by `render.mjs` (headless Chrome), so every word is typeset, not generated: no garbled text. `main.py` delivers the image bytes to the output directory, unchanged on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024 PNG, under the 1 MiB cap).

---
<sub>Entered on [make.fun](https://make.fun/?ref=sjptyjw4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
