# Contact Extraction

**Purpose.** Pull business contact channels (email, other social handles, link-in-bio pages, booking/agency notes) out of a creator's free-form profile text without inventing anything.

## Inputs

| Field | Description |
|---|---|
| `platform` | Source platform name |
| `username` | Creator handle |
| `bio` | Profile bio / about text |
| `links` | List of URLs found on the profile (optional) |
| `pinned_text` | Text of pinned post or highlights (optional) |

## System prompt

```text
You extract business contact information from social media creator profiles.
Rules:
- Only return values that literally appear in the input. Never guess or complete a partial email.
- Normalise obfuscated emails ("name [at] domain dot com" -> "name@domain.com") and say so in `evidence`.
- Distinguish the creator's own contact from an agency / manager contact when the text makes it clear.
- If nothing is found, return empty fields rather than a refusal.
```

## User prompt template

```text
Platform: {platform}
Username: @{username}
Bio:
{bio}
Links:
{links}
Pinned / highlight text:
{pinned_text}

Extract contact information as JSON.
```

## Output

Return one JSON object that validates against [`schemas/contact-extraction.schema.json`](../schemas/contact-extraction.schema.json).

## Example

Input:

```json
{
  "platform": "instagram",
  "username": "sunny.bakes",
  "bio": "Home baker in Lisbon 🍞 | recipes weekly\nBusiness: sunny.bakes [at] gmail dot com\nManaged by @northstar.talent",
  "links": [
    "https://linktr.ee/sunnybakes"
  ],
  "pinned_text": ""
}
```

Output:

```json
{
  "emails": [
    "sunny.bakes@gmail.com"
  ],
  "handles": [
    {
      "platform": "instagram",
      "handle": "northstar.talent"
    }
  ],
  "contact_page_urls": [
    "https://linktr.ee/sunnybakes"
  ],
  "contact_type": "mixed",
  "evidence": "\"Business: sunny.bakes [at] gmail dot com\" (de-obfuscated); \"Managed by @northstar.talent\""
}
```

## Tips

- Keep temperature at 0; this is extraction, not generation.
- Run a regex email check on the output before trusting it.
- Bios are short: batch 20 to 50 profiles per call to save on prompt overhead.
