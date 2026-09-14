# Outreach Message Drafting

**Purpose.** Write a short, personalised first-contact message to a creator on behalf of a brand, referencing something specific from their content.

## Inputs

| Field | Description |
|---|---|
| `brand_name` | Brand name |
| `product_one_liner` | What the product is in one sentence |
| `creator_first_name` | Creator's first name or handle |
| `creator_recent_content` | One or two recent posts to reference |
| `offer_type` | gifting / paid / affiliate |
| `tone` | e.g. friendly, professional |

## System prompt

```text
Draft a first outreach message from a brand to a creator.
- 80 to 140 words. One specific reference to the creator's recent content in the first two sentences.
- State clearly what is being offered (gifting, paid, affiliate) and one concrete next step.
- No flattery clichés ("huge fan", "love your vibe"), no emojis unless tone is "casual", no pressure language.
- Produce a subject line under 8 words.
```

## User prompt template

```text
Brand: {brand_name}
Product: {product_one_liner}
Creator: {creator_first_name}
Their recent content: {creator_recent_content}
Offer type: {offer_type}
Tone: {tone}

Write the message as JSON.
```

## Output

Return one JSON object that validates against [`schemas/outreach-message-drafting.schema.json`](../schemas/outreach-message-drafting.schema.json).

## Example

Input:

```json
{
  "brand_name": "Ridgeline",
  "product_one_liner": "A 20L commuter backpack with a laptop sleeve that opens flat for airport security.",
  "creator_first_name": "Maya",
  "creator_recent_content": "A video packing for a 3-day work trip in one carry-on, complaining about pulling the laptop out at security.",
  "offer_type": "gifting",
  "tone": "professional"
}
```

Output:

```json
{
  "subject": "Your carry-on packing video",
  "body": "Hi Maya,\n\nYour 3-day work trip packing video hit a nerve here, especially the part about digging the laptop out at security every time. Ridgeline makes a 20L commuter backpack whose laptop sleeve opens flat, so it goes through the scanner without unpacking.\n\nWe'd like to send you one to try on your next trip, no strings attached. If it earns a place in a future packing video, great; if not, we'd still value your honest feedback.\n\nIf you're open to it, reply with a shipping address and colour preference (black or olive) and we'll get it out this week.\n\nBest,\nDana, Ridgeline partnerships",
  "content_reference": "3-day work trip carry-on packing video"
}
```

## Tips

- Always pass a real recent post; generic references are the fastest way to get ignored.
- Keep the offer type explicit; ambiguity about payment wastes both sides' time.
- Generate two variants and A/B test subject lines.
