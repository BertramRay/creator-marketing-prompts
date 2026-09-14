# Brand and Creator Fit

**Purpose.** Given a short brand brief and a creator summary, judge whether a collaboration makes sense, score it, and explain the main reasons for and against.

## Inputs

| Field | Description |
|---|---|
| `brand_brief` | Product, target customer, campaign goal, must-have and must-avoid constraints |
| `creator_summary` | Niche, typical content, audience description, past sponsorships, tone |
| `deliverable` | Requested content format (e.g. short video review) |

## System prompt

```text
You are an experienced influencer marketing strategist. Assess creator fit for a specific brand brief.
Judge on four axes, each 0-10:
1. audience_match: does the creator's audience look like the brand's target customer?
2. content_match: does the requested deliverable fit the creator's usual format and tone?
3. credibility: would the creator's endorsement be believable for this product category?
4. risk: brand-safety or reputational concerns (10 = no concerns).
`fit_score` is 0-100 and should not be a plain average; weight audience_match and credibility highest.
`verdict` is "strong_fit", "possible_fit" or "poor_fit". Be specific in `reasons`; avoid generic praise.
```

## User prompt template

```text
Brand brief:
{brand_brief}

Creator summary:
{creator_summary}

Requested deliverable: {deliverable}

Evaluate the fit as JSON.
```

## Output

Return one JSON object that validates against [`schemas/brand-creator-fit.schema.json`](../schemas/brand-creator-fit.schema.json).

## Example

Input:

```json
{
  "brand_brief": "Budget meal-prep containers. Target: students and young professionals in the UK. Goal: drive online sales. Avoid: creators who mostly post restaurant content.",
  "creator_summary": "UK-based creator posting weekly 60-second 'cook once, eat all week' videos; audience mostly 18-30, comments ask about prices and storage; two prior kitchenware sponsorships, casual tone.",
  "deliverable": "One 45-60s short video demonstrating the product in a weekly meal prep"
}
```

Output:

```json
{
  "fit_score": 84,
  "verdict": "strong_fit",
  "axes": {
    "audience_match": 9,
    "content_match": 9,
    "credibility": 8,
    "risk": 9
  },
  "reasons_for": [
    "Audience already asks about storage and prices, matching the product's value proposition",
    "Deliverable is the creator's native format",
    "Prior kitchenware sponsorships show the audience accepts product content"
  ],
  "reasons_against": [
    "Two recent kitchenware deals may dilute perceived authenticity if spaced too closely"
  ],
  "suggested_angle": "Show a full week of meals fitting in the containers with a total cost overlay."
}
```

## Tips

- Feed the model a compact creator summary rather than raw data; summarising first cuts tokens and improves consistency.
- Calibrate `fit_score` on a labelled set of past deals before using thresholds.
- Ask for `reasons_against` explicitly; without it models rarely volunteer negatives.
