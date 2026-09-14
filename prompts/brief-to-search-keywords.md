# Campaign Brief to Search Keywords

**Purpose.** Turn a campaign brief into diverse search keywords and hashtags for discovering relevant creators on a given platform, grouped by intent.

## Inputs

| Field | Description |
|---|---|
| `brief` | Product, target customer, campaign goal |
| `platform` | Platform to search on |
| `language` | Language of the target market |
| `max_keywords` | Upper bound on keywords to return |

## System prompt

```text
Generate creator-discovery search terms from a campaign brief.
- Group terms into: `product_terms` (what the product is), `problem_terms` (what it solves), `adjacent_niches` (creators whose audience overlaps), `format_terms` (content formats that suit the product).
- Terms must be in the target language and phrased the way people actually search or tag on the platform (short, no punctuation, hashtags lowercase without spaces).
- Avoid brand names of competitors and avoid terms that are too broad to be useful (e.g. "video", "fun").
- Order each group from most to least specific.
```

## User prompt template

```text
Brief:
{brief}
Platform: {platform}
Language: {language}
Max keywords: {max_keywords}

Return keyword groups as JSON.
```

## Output

Return one JSON object that validates against [`schemas/brief-to-search-keywords.schema.json`](../schemas/brief-to-search-keywords.schema.json).

## Example

Input:

```json
{
  "brief": "Noise-cancelling earbuds for people who work in open offices or cafés. Target: remote workers and students. Goal: awareness.",
  "platform": "tiktok",
  "language": "en",
  "max_keywords": 20
}
```

Output:

```json
{
  "product_terms": [
    "noise cancelling earbuds",
    "anc earbuds review",
    "earbuds for focus"
  ],
  "problem_terms": [
    "cant focus in open office",
    "loud cafe study",
    "noisy roommate studying"
  ],
  "adjacent_niches": [
    "studytok",
    "deskssetup",
    "remote work day in my life",
    "productivity tips"
  ],
  "format_terms": [
    "earbuds unboxing",
    "sound test",
    "work from cafe vlog"
  ]
}
```

## Tips

- Run the output through a quick volume check on the platform; the model cannot know which terms are actually active.
- Regenerate per language; do not translate keywords literally.
- Keep `adjacent_niches`; that is where most of the interesting creators come from.
