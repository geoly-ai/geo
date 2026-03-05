# Multilingual GEO Guidelines (Reference)

This reference file supports the `geo-multilingual-optimizer` skill. It provides additional
background and best practices for multilingual GEO and AI citation alignment.

The skill should selectively draw on these guidelines when helpful, but **not** copy them
verbatim into every answer. Summarize and adapt them to the user’s specific context.

---

## 1. Multilingual GEO Principles

1. **Canonical source of truth**  
   - Always identify which language and page is the canonical starting point.  
   - If the canonical asset is low quality, fix it **before** scaling to more languages.  

2. **Adaptation over literal translation**  
   - Literal translations often fail GEO and AI needs.  
   - Preserve **meaning, entities, and claims**, while adapting examples, tone, and idioms.  

3. **Stable entities across languages**  
   - Brand and product names should stay consistent or follow a well-defined transliteration.  
   - Key entities (features, frameworks, protocols) should be mapped 1:1 where possible.  

4. **Local expectations and regulations**  
   - Some markets require extra disclosures, disclaimers, or proof.  
   - GEO content should respect these differences while keeping core definitions aligned.  

5. **AI is multilingual, but training data is uneven**  
   - In many categories, English data is richer, so English answers can be stronger.  
   - The job of multilingual GEO is to **raise the floor** for other languages by serving high-quality,
     clearly structured, localized content that is easy for models to ingest and trust.

---

## 2. Language and Locale Design

When designing for multiple markets:

- Start from a **clear market priority** list (e.g., US → EU → LATAM → APAC).  
- Decide whether each locale gets:
  - A **fully localized experience** (own subdirectory, localized UX, separate PDPs).  
  - A **light-localization layer** (shared templates, limited copy changes).  
- Aim for **consistent URL patterns**, avoiding unnecessary fragmentation (e.g., avoid mixing
  `/es`, `/es-es`, `/es_ES` without a clear strategy).

Useful conventions:

- Use **language + region** where it matters: `en-us`, `en-gb`, `es-es`, `es-mx`, `pt-br`.  
- Group content per language in sitemaps or logical sections.  
- Ensure that each localized page has:
  - A clear `lang` attribute.  
  - Correct `hreflang` annotations.  
  - A stable canonical URL (no random query parameters or tracking IDs in the canonical).

---

## 3. Terminology and Style Guides

For strong multilingual GEO performance:

- Maintain a **central terminology map** that includes:
  - Source term (often English).  
  - Approved translations per target language.  
  - Notes about when to **keep the English term** (e.g., product names, brand taglines).  

- Define **style constraints** per language:
  - Formal vs. informal tone.  
  - B2B vs. B2C voice.  
  - Local legal sensitivities.  

- Address:
  - How to write numbers, units, dates, currencies.  
  - Whether to localize screenshots, pricing examples, or case study names.  

The skill should encourage the user to **reuse these guides** in content, schemas, and llms.txt.

---

## 4. Multilingual Structured Data

Key practices:

- Use Schema.org types (`WebPage`, `Article`, `FAQPage`, `Product`, etc.) per language.  
- Set the `inLanguage` property correctly (e.g., `en-US`, `es-ES`, `de-DE`).  
- Localize:
  - `headline`  
  - `description`  
  - `name` (when appropriate)  
  - `about` and `keywords`, if used.  

- Hreflang / alternates:
  - Reflect language/locale relationships both in HTML and in sitemaps where possible.  
  - Ensure that AI-visible canonical pages appear in the same **hreflang cluster** as their
    localized variants.

The goal is for AI crawlers and models to see a **clean, coherent graph** of localized entities
rather than a messy mix of duplicate or conflicting pages.

---

## 5. llms.txt and AI Hubs

When using `llms.txt` and AI-facing index pages:

- Group entries by **language and topic**.  
- Highlight:
  - Canonical pages per language.  
  - Key “overview” or “definition” pages that are safe to cite.  
  - Deep-dive guides and implementation docs.  

- Provide simple, explicit descriptions for each link, such as:
  - “Official Spanish guide to [Topic] from [Brand].”  
  - “German product documentation for [Product].”  

This helps AI systems understand **which page to treat as the primary reference** in each language.

---

## 6. Evaluating Multilingual AI Behavior

To measure success:

- Periodically test AI answers in multiple languages on:
  - ChatGPT  
  - Perplexity  
  - Gemini  
  - Other relevant platforms  

- Check:
  - Whether the correct **brand and products** are mentioned.  
  - Whether the **right localized URLs** are suggested or implied.  
  - Whether explanations stay **factually consistent** across languages.  

- Use these observations to refine:
  - Terminology maps.  
  - Structured data.  
  - Internal and external linking strategies.  
  - llms.txt and AI hub pages.

The skill should encourage **iterative improvement**, not a one-time localization project.

