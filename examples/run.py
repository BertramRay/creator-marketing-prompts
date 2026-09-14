"""Minimal runner: python examples/run.py <prompt-slug> <input.json> [--model MODEL]

Reads prompts/<slug>.md, fills the user template with the input JSON, requests a JSON
object from any OpenAI-compatible chat endpoint, and validates it against schemas/<slug>.schema.json.
"""
import argparse, json, re, sys
from pathlib import Path

from jsonschema import validate
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent


def load_prompt(slug: str) -> tuple[str, str]:
    text = (ROOT / "prompts" / f"{slug}.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```text\n(.*?)```", text, flags=re.S)
    if len(blocks) < 2:
        sys.exit(f"prompt file for {slug} must contain a system and a user block")
    return blocks[0].strip(), blocks[1].strip()


def fill(template: str, values: dict) -> str:
    def repl(match):
        key = match.group(1)
        value = values.get(key, "")
        return json.dumps(value, ensure_ascii=False, indent=2) if isinstance(value, (list, dict)) else str(value)
    return re.sub(r"\{(\w+)\}", repl, template)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("input_json")
    parser.add_argument("--model", default="gpt-4o-mini")
    args = parser.parse_args()

    system, user_template = load_prompt(args.slug)
    values = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schemas" / f"{args.slug}.schema.json").read_text(encoding="utf-8"))

    client = OpenAI()
    response = client.chat.completions.create(
        model=args.model,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": system}, {"role": "user", "content": fill(user_template, values)}],
    )
    result = json.loads(response.choices[0].message.content)
    validate(result, schema)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
