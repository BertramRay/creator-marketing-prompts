# Engagement Authenticity Check

**Purpose.** Judge from aggregate metrics and a comment sample whether a creator's engagement looks organic, and list any suspicious patterns without making accusations.

## Inputs

| Field | Description |
|---|---|
| `metrics` | Follower count, average views, likes, comments per post, posting frequency |
| `comments` | Sample of recent comments (text only) |
| `history` | Optional: follower growth points over time |

## System prompt

```text
Assess engagement authenticity. You are looking for patterns, not proof.
Consider: like-to-view and comment-to-view ratios relative to typical ranges for the follower size, generic or repetitive comments, comment timing bursts if provided, and sudden follower jumps.
- `authenticity` is "likely_organic", "mixed" or "suspicious".
- `patterns` lists concrete observations; each must reference a number or a quoted example.
- Do not label the creator as fraudulent; describe patterns and let a human decide.
```

## User prompt template

```text
Metrics:
{metrics}

Comment sample:
{comments}

Growth history:
{history}

Assess as JSON.
```

## Output

Return one JSON object that validates against [`schemas/engagement-authenticity.schema.json`](../schemas/engagement-authenticity.schema.json).

## Example

Input:

```json
{
  "metrics": {
    "followers": 52000,
    "avg_views": 1800,
    "avg_likes": 1700,
    "avg_comments": 210,
    "posts_per_week": 3
  },
  "comments": [
    "Nice!",
    "Great post",
    "Nice!",
    "Amazing content keep it up",
    "Nice!",
    "Where did you get the jacket?"
  ],
  "history": ""
}
```

Output:

```json
{
  "authenticity": "suspicious",
  "patterns": [
    "Likes nearly equal views (1700 of 1800), far above typical ratios",
    "4 of 6 sampled comments are generic one-liners, 'Nice!' repeated three times",
    "Comment count (210) is high relative to 1800 views"
  ],
  "comment_quality": "low",
  "notes": "One substantive comment about the jacket suggests some real audience."
}
```

## Tips

- Provide typical ratio ranges for the platform in the system prompt if you have them; the model's priors are rough.
- This is a triage signal; combine with follower-growth data before acting.
- Sample at least 30 comments from several posts to avoid single-post bias.
