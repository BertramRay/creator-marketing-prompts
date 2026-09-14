# Audience Persona Inference

**Purpose.** Infer who watches a creator from comment samples and content themes: age band, gender skew, interests, purchasing power and geography signals, with explicit uncertainty.

## Inputs

| Field | Description |
|---|---|
| `content_summary` | One-paragraph description of what the creator posts |
| `comments` | Sample of recent comments (text only, no personal data) |
| `declared_audience_stats` | Platform-provided audience stats if any (optional) |

## System prompt

```text
Infer an audience persona from indirect signals. You are estimating, so:
- Use ranges and skews, not point values ("18-24", "mostly female").
- Ground every claim in the comments or content themes; put the supporting pattern in `signals`.
- When platform-declared stats are provided they override your inference; note any conflict.
- Never identify individual commenters.
```

## User prompt template

```text
Content summary:
{content_summary}

Comment sample:
{comments}

Declared audience stats: {declared_audience_stats}

Describe the audience as JSON.
```

## Output

Return one JSON object that validates against [`schemas/audience-persona-inference.schema.json`](../schemas/audience-persona-inference.schema.json).

## Example

Input:

```json
{
  "content_summary": "Short apartment-organising videos with product links.",
  "comments": [
    "where is the shelf from?? need for my dorm",
    "my roommate would kill for this",
    "link for the bins pls",
    "ok but rent in this city..."
  ],
  "declared_audience_stats": ""
}
```

Output:

```json
{
  "age_band": "18-24",
  "gender_skew": "unknown",
  "interests": [
    "home organisation",
    "budget furniture",
    "student living"
  ],
  "purchasing_power": "low",
  "geography_signals": [
    "urban renters"
  ],
  "signals": [
    "dorm and roommate references",
    "repeated requests for product links",
    "rent complaint"
  ],
  "confidence": 0.6
}
```

## Tips

- Strip usernames and avatars before sending comments; text alone is enough.
- Sample comments across several posts, not one viral post.
- Treat `confidence` below 0.5 as 'unknown' downstream.
