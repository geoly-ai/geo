"""
Multilingual Terminology Helper

This script is a reference implementation sketch for how an automated helper
could manage multilingual terminology maps for the `geo-multilingual-optimizer`
skill. It is not executed automatically by the skill, but illustrates the
data structures and transformations that could be reused by automation.

The core idea:
- Represent terminology as structured Python dictionaries.
- Support export to simple tabular formats (CSV/TSV/Markdown) that humans and
  other tools can consume.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class TermEntry:
    source_term: str
    description_en: str
    translations: Dict[str, str]
    keep_english_for: List[str]
    notes: str = ""


def build_example_terminology_map() -> Dict[str, TermEntry]:
    """
    Return an in-memory example terminology map that the skill can conceptually
    mirror in its markdown outputs.
    """
    return {
        "Zero-trust data governance": TermEntry(
            source_term="Zero-trust data governance",
            description_en="A security approach that assumes no implicit trust for data access.",
            translations={
                "es-ES": "Gobernanza de datos de confianza cero",
                "es-MX": "Gobernanza de datos de confianza cero",
                "de-DE": "Zero-Trust-Datengovernance",
                "pt-BR": "Governança de dados de confiança zero",
            },
            keep_english_for=["product-name-variants"],
            notes="Prefer capitalized form in titles; allow lowercase in body text.",
        ),
        "SaaS security platform": TermEntry(
            source_term="SaaS security platform",
            description_en="A cloud-based platform that secures software-as-a-service applications.",
            translations={
                "es-ES": "Plataforma de seguridad SaaS",
                "es-MX": "Plataforma de seguridad SaaS",
                "de-DE": "SaaS-Sicherheitsplattform",
                "pt-BR": "Plataforma de segurança SaaS",
            },
            keep_english_for=["SaaS"],
            notes="Keep the acronym 'SaaS' in all languages.",
        ),
    }


def to_markdown_table(terminology_map: Dict[str, TermEntry]) -> str:
    """
    Convert a terminology map into a markdown table string.
    This can be used as a conceptual template for what the skill
    should output in responses.
    """
    # Collect all language codes used across terms
    languages = set()
    for entry in terminology_map.values():
        languages.update(entry.translations.keys())
    language_cols = sorted(languages)

    headers = ["Source Term", "Description (EN)"] + language_cols + ["Keep English For", "Notes"]
    rows = ["|" + "|".join(headers) + "|", "|" + "|".join(["---"] * len(headers)) + "|"]

    for key, entry in terminology_map.items():
        row = [
            entry.source_term,
            entry.description_en,
        ]
        for lang in language_cols:
            row.append(entry.translations.get(lang, ""))
        row.append(", ".join(entry.keep_english_for))
        row.append(entry.notes)
        rows.append("|" + "|".join(row) + "|")

    return "\n".join(rows)


if __name__ == "__main__":
    # Demonstration: print an example markdown table
    terminology_map = build_example_terminology_map()
    print(to_markdown_table(terminology_map))

