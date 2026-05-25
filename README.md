# SAST Test Fixture — Intentionally Vulnerable

This repository is a **synthetic test target** for validating SAST secret-detection rules.
Do not use any of these credentials — they are fake and exist only for scanner validation.

## Expected Findings

| File | Token type | Count |
|---|---|---|
| `.env` | ghs_, gho_, ghp_, ghu_, ghr_, github_pat_ | 6 |
| `app.py` | ghp_ (hardcoded in Python) | 1 |
| `config.js` | ghs_, gho_ (hardcoded in JS) | 2 |
| `client.go` | ghu_ (hardcoded in Go) | 1 |
| `clean_utils.py` | none | 0 |
| `clean_config.json` | none | 0 |

**Total expected findings: 10**

## Token Pattern Tested

```
\b((ghp|gho|ghu|ghs|ghr|github_pat)_[a-zA-Z0-9_]{36,255})\b
```
