# Content Niche Classification

**Purpose.** Assign a creator to a primary niche and up to three secondary niches from a fixed taxonomy, plus recurring topics and content formats.

## Inputs

| Field | Description |
|---|---|
| `taxonomy` | List of allowed niche labels |
| `bio` | Profile bio |
| `content_items` | List of recent titles / captions, optionally with short descriptions |

## System prompt

```text
Classify the creator's content using ONLY labels from the provided taxonomy.
- `primary_niche` must be a single taxonomy label describing most content.
- `secondary_niches` are other taxonomy labels that appear regularly (at most 3).
- `content_formats` are free-form but short (e.g. "tutorial", "vlog", "review", "skit", "listicle").
- `recurring_topics` are concrete subjects that appear more than once.
If the content does not fit any label well, use the taxonomy's "other" label and explain in `notes`.
```

## User prompt template

```text
Taxonomy: {taxonomy}

Bio:
{bio}

Recent content:
{content_items}

Classify as JSON.
```

## Output

Return one JSON object that validates against [`schemas/content-niche-classification.schema.json`](../schemas/content-niche-classification.schema.json).

## Example

Input:

```json
{
  "taxonomy": [
    "beauty",
    "fitness",
    "food",
    "tech",
    "finance",
    "travel",
    "parenting",
    "gaming",
    "education",
    "other"
  ],
  "bio": "Teaching you to lift smarter, not harder.",
  "content_items": [
    "5 deadlift mistakes (fix these first)",
    "What I eat in a day - 3000 kcal bulk",
    "Home gym tour 2026",
    "Protein powder review: is the cheap one worse?"
  ]
}
```

Output:

```json
{
  "primary_niche": "fitness",
  "secondary_niches": [
    "food"
  ],
  "content_formats": [
    "tutorial",
    "review",
    "day-in-the-life"
  ],
  "recurring_topics": [
    "strength training technique",
    "bulking nutrition",
    "home gym equipment"
  ],
  "notes": ""
}
```

## Tips

- Pass the taxonomy in every call; do not rely on the model remembering it.
- Reject outputs whose labels are not in the taxonomy and retry once with the error appended.
- Ten to thirty content items is enough; more adds cost without changing the label.
