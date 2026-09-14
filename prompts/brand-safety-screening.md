# Brand Safety Screening

**Purpose.** Flag content themes that a mainstream advertiser would want to know about before sponsoring a creator, graded by severity and frequency.

## Inputs

| Field | Description |
|---|---|
| `content_items` | Recent titles / captions / transcript snippets |
| `comments` | Optional comment sample |
| `brand_sensitivities` | Categories this particular brand cares about (optional) |

## System prompt

```text
Screen a creator for brand-safety concerns. For each category report severity ("none", "low", "medium", "high") and a one-line justification:
profanity, adult_content, violence_or_gore, hate_or_harassment, drugs_or_alcohol, political_or_divisive, misinformation, dangerous_activities.
Severity is driven first by how serious the worst instance is, then by how often it appears. A single serious instance is at least "medium".
Do not penalise ordinary opinions, mild language, or topics merely being mentioned in a neutral way.
Set `overall` to the highest category severity and list the specific items behind any non-"none" rating in `flagged_items`.
```

## User prompt template

```text
Recent content:
{content_items}

Comment sample:
{comments}

Brand-specific sensitivities: {brand_sensitivities}

Screen as JSON.
```

## Output

Return one JSON object that validates against [`schemas/brand-safety-screening.schema.json`](../schemas/brand-safety-screening.schema.json).

## Example

Input:

```json
{
  "content_items": [
    "Trying the world's hottest chip challenge (I cried)",
    "Rating my viewers' setups",
    "Why I quit energy drinks after 5 years"
  ],
  "comments": [],
  "brand_sensitivities": [
    "alcohol"
  ]
}
```

Output:

```json
{
  "overall": "low",
  "categories": {
    "profanity": {
      "severity": "none",
      "note": ""
    },
    "adult_content": {
      "severity": "none",
      "note": ""
    },
    "violence_or_gore": {
      "severity": "none",
      "note": ""
    },
    "hate_or_harassment": {
      "severity": "none",
      "note": ""
    },
    "drugs_or_alcohol": {
      "severity": "none",
      "note": "Energy drink discussion is not alcohol"
    },
    "political_or_divisive": {
      "severity": "none",
      "note": ""
    },
    "misinformation": {
      "severity": "none",
      "note": ""
    },
    "dangerous_activities": {
      "severity": "low",
      "note": "Extreme spicy food challenge, common format, no injury"
    }
  },
  "flagged_items": [
    "Trying the world's hottest chip challenge (I cried)"
  ]
}
```

## Tips

- Keep the category list fixed so results are comparable across creators.
- Severity-first grading prevents 'it only happened once' from hiding serious issues.
- Log `flagged_items` for human review rather than auto-rejecting on `medium`.
