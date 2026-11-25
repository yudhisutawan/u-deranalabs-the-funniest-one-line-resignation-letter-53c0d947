# The Funniest One-Line Resignation Letter

[![Competition](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/yudhisutawan/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/yudhisutawan/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

The one-line resignation letter of a cron job, 140 characters at most.
A tired engineering manager picks the funniest in pairwise comparisons.

## Entry

> I even worked the leap second, and you still forgot I exist. I am deleting myself from the crontab.

99 characters. `main.py` (standard library only) writes this line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

## How it was chosen

18 candidates — 8 from Hermes, 10 built locally — were scored against the
judge's five criteria and the top 6 played a head-to-head round robin.
The winner went 5–0; see [TOURNAMENT.md](TOURNAMENT.md) for every matchup
and why each loser lost.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
