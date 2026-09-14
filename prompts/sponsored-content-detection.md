# Sponsored Content Detection

**Purpose.** Identify which of a creator's recent posts are likely paid partnerships, which brands are involved, and whether disclosure looks compliant.

## Inputs

| Field | Description |
|---|---|
| `content_items` | List of {id, caption, hashtags, description} for recent posts |

## System prompt

```text
For each post decide whether it is likely sponsored. Signals include disclosure tags (#ad, #sponsored, "paid partnership"), discount codes, affiliate links, brand handles in the caption, and product-centric phrasing.
- `collab_type` is "paid_likely" (clear commercial signals), "mention_only" (brand named without commercial signals) or "none".
- Only name a brand that appears in the post text. Do not guess brands from context.
- `disclosure` is "clear", "weak" (e.g. #sp buried among 30 hashtags) or "missing" for paid_likely posts; "n/a" otherwise.
Return one entry per input post, keeping the input `id`.
```

## User prompt template

```text
Posts:
{content_items}

Classify each post as JSON.
```

## Output

Return one JSON object that validates against [`schemas/sponsored-content-detection.schema.json`](../schemas/sponsored-content-detection.schema.json).

## Example

Input:

```json
{
  "content_items": [
    {
      "id": "p1",
      "caption": "My skin has never been happier. Use code SUN15 for 15% off @glowlab #ad",
      "hashtags": [
        "ad",
        "skincare"
      ],
      "description": ""
    },
    {
      "id": "p2",
      "caption": "Morning walk with the dog",
      "hashtags": [
        "sunday"
      ],
      "description": ""
    }
  ]
}
```

Output:

```json
{
  "posts": [
    {
      "id": "p1",
      "collab_type": "paid_likely",
      "brands": [
        "glowlab"
      ],
      "disclosure": "clear",
      "evidence": "#ad tag, discount code SUN15, brand handle"
    },
    {
      "id": "p2",
      "collab_type": "none",
      "brands": [],
      "disclosure": "n/a",
      "evidence": ""
    }
  ],
  "brands_summary": [
    {
      "brand": "glowlab",
      "post_ids": [
        "p1"
      ]
    }
  ]
}
```

## Tips

- Always echo the input `id`; matching by caption text is fragile.
- Disclosure rules differ by country; treat `weak` as 'needs a human look'.
- Aggregate `brands_summary` over months to build a creator's sponsorship history.
