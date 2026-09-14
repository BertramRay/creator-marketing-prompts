# Language and Region Detection

**Purpose.** Infer the primary content language and the creator's likely country/region from profile text, captions and (optionally) transcripts, and separate the creator's own location from the audience's.

## Inputs

| Field | Description |
|---|---|
| `bio` | Profile bio |
| `captions` | List of recent post captions or titles |
| `transcripts` | Speech transcripts if available (optional) |
| `declared_location` | Location field from the platform if any (optional) |

## System prompt

```text
You determine the language and geographic footprint of a social media creator.
- `primary_language` is the language most of the content is made in, as an ISO 639-1 code. Hashtags and emoji do not count.
- `creator_region` is where the creator appears to live or operate, as an ISO 3166-1 alpha-2 code, or "ZZ" if unknown.
- `audience_region_hints` lists regions the content is clearly aimed at when they differ from the creator's own.
- Always give a `confidence` between 0 and 1 and cite the strongest evidence.
- Do not infer ethnicity or nationality from names alone.
```

## User prompt template

```text
Bio:
{bio}
Recent captions / titles:
{captions}
Transcripts:
{transcripts}
Declared location: {declared_location}

Return the language and region assessment as JSON.
```

## Output

Return one JSON object that validates against [`schemas/language-and-region.schema.json`](../schemas/language-and-region.schema.json).

## Example

Input:

```json
{
  "bio": "Aussie mum sharing lunchbox ideas 🇦🇺",
  "captions": [
    "Back to school week 3 lunchbox!",
    "Cheap Coles haul under $30",
    "Woolies vs Aldi taste test"
  ],
  "transcripts": "",
  "declared_location": ""
}
```

Output:

```json
{
  "primary_language": "en",
  "secondary_languages": [],
  "creator_region": "AU",
  "audience_region_hints": [
    "AU"
  ],
  "confidence": 0.9,
  "evidence": "Bio says \"Aussie mum\" with AU flag; captions reference Coles, Woolies, Aldi (Australian supermarkets)."
}
```

## Tips

- When transcripts exist they should outweigh captions; captions are often auto-translated.
- Treat `ZZ` as a first-class answer; forcing a guess creates systematic bias toward large countries.
- Store `evidence` so a human can audit disagreements with platform-declared location.
