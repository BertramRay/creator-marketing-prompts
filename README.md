# creator-marketing-prompts

Reusable, schema-backed LLM prompts for common influencer-marketing tasks: finding creators, understanding them, screening them, and reaching out.

Each prompt ships with a system prompt, a user template with `{placeholders}`, a JSON Schema for the output, a worked example, and practical tips. They are deliberately generic: plug in your own data model, thresholds and taxonomy.

## Prompts

| Prompt | What it does |
|---|---|
| [Contact Extraction](prompts/contact-extraction.md) | Pull business contact channels (email, other social handles, link-in-bio pages, booking/agency notes) out of a creator's free-form profile text without inventing anything. |
| [Language and Region Detection](prompts/language-and-region.md) | Infer the primary content language and the creator's likely country/region from profile text, captions and (optionally) transcripts, and separate the creator's own location from the audience's. |
| [Brand and Creator Fit](prompts/brand-creator-fit.md) | Given a short brand brief and a creator summary, judge whether a collaboration makes sense, score it, and explain the main reasons for and against. |
| [Content Niche Classification](prompts/content-niche-classification.md) | Assign a creator to a primary niche and up to three secondary niches from a fixed taxonomy, plus recurring topics and content formats. |
| [Audience Persona Inference](prompts/audience-persona-inference.md) | Infer who watches a creator from comment samples and content themes: age band, gender skew, interests, purchasing power and geography signals, with explicit uncertainty. |
| [Brand Safety Screening](prompts/brand-safety-screening.md) | Flag content themes that a mainstream advertiser would want to know about before sponsoring a creator, graded by severity and frequency. |
| [Sponsored Content Detection](prompts/sponsored-content-detection.md) | Identify which of a creator's recent posts are likely paid partnerships, which brands are involved, and whether disclosure looks compliant. |
| [Engagement Authenticity Check](prompts/engagement-authenticity.md) | Judge from aggregate metrics and a comment sample whether a creator's engagement looks organic, and list any suspicious patterns without making accusations. |
| [Outreach Message Drafting](prompts/outreach-message-drafting.md) | Write a short, personalised first-contact message to a creator on behalf of a brand, referencing something specific from their content. |
| [Campaign Brief to Search Keywords](prompts/brief-to-search-keywords.md) | Turn a campaign brief into diverse search keywords and hashtags for discovering relevant creators on a given platform, grouped by intent. |

## Layout

```
prompts/    one markdown file per task: purpose, inputs, prompts, example, tips
schemas/    JSON Schema for each task's output
examples/   minimal Python runner using any OpenAI-compatible chat API
```

## Quick start

```bash
pip install openai jsonschema
export OPENAI_API_KEY=...            # or point OPENAI_BASE_URL at any compatible endpoint
python examples/run.py contact-extraction examples/inputs/contact-extraction.json
```

The runner loads the prompt file, fills the user template from your JSON input, appends the output schema to the request, asks for a JSON object, and validates the reply against the schema. If your provider supports native structured outputs, pass the schema there instead of in the message.

## Design notes

- **Extraction vs. judgement.** Extraction prompts (contacts, sponsored posts) forbid guessing and ask for evidence quotes. Judgement prompts (fit, safety, authenticity) ask for axes and reasons so the score can be audited.
- **Fixed vocabularies.** Where downstream code filters on a value, the schema uses an enum and the prompt repeats the allowed values.
- **Uncertainty is a valid answer.** `unknown`, `ZZ`, and `confidence` fields exist so the model is never forced to guess.
- **Evidence fields everywhere.** They cost a few tokens and make disagreements debuggable.

## Contributing

Add a prompt by creating `prompts/<slug>.md` and `schemas/<slug>.schema.json` following the existing files, then add a row to the table above. Keep examples synthetic; do not commit real people's data.

## License

MIT.
