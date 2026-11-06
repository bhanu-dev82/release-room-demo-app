# keepary-core

The receipt-parsing core of Keepary, an expense app. This repo is the demo target for [**Release Room**](https://github.com/bhanu-dev82/release-room), a Switch workflow where AI agents triage app reviews and fix the bugs behind them.

Pull requests titled `[Release Room] Fix: …` were opened by the Release Room fixer agent, after its reviewer agent approved the patch and a person allowed the push in chat.

## Run the tests

```bash
uv run --with pytest pytest -q
```

## The bugs (on purpose)

The `main` branch ships with three bugs. Each one matches a cluster of user reviews in Release Room's sample data:

| Users say | Where |
|---|---|
| "App crashes when I scan a receipt without a date" | `keepary_core/parse.py` |
| "Amounts show as 100,000 instead of 1,00,000" | `keepary_core/money.py` |
| "Hindi bills don't read the total" | `keepary_core/parse.py`, `keepary_core/digits.py` |

The tests on `main` cover only behaviour the bugs don't touch. The agents write the failing tests themselves, from the users' words.

## License

MIT. See `LICENSE`.
