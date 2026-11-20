"""Build the selected and detailed READMEs and the standalone catalog pages."""

import re
from pathlib import Path

TITLE = "Diffusion for Image-to-Image Translation"
BADGE = "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/wd1511/Awesome-Diffusion-for-Image-Translation)"
SELECTED = "README.md"
DETAILED = "README-detailed.md"


def read_sections(source):
    _, *parts = re.split(r"^## (.+)\n", source, flags=re.MULTILINE)
    sections = {}
    for heading, body in zip(parts[::2], parts[1::2]):
        body = body.strip()
        if heading == "2021 and earlier":
            slug = "before-2021"
        elif heading.isdecimal() and int(heading) <= 2021:
            slug = "before-2021"
            body = f"### {heading}\n\n{body}"
        else:
            slug = heading.lower()
        sections[slug] = "\n\n".join(filter(None, [sections.get(slug), body]))
    return sections


def label(slug):
    return {"datasets": "Datasets", "before-2021": "2021 and earlier"}.get(slug, slug)


def heading_link(slug):
    return "#" + label(slug).lower().replace(" ", "-")


def render_readme(sections, updated, detailed):
    if detailed:
        versions = f"[Selected papers]({SELECTED}) | **Full bibliography**"
        intro = "The complete bibliography of diffusion and flow models for image translation, editing, and style transfer."
    else:
        versions = f"**Selected papers** | [Full bibliography]({DETAILED})"
        intro = "Selected papers on diffusion and flow models for image translation, editing, and style transfer."
    navigation = " | ".join(f"[{label(slug)}]({heading_link(slug)})" for slug in sections)
    parts = [versions, f"# {TITLE} {BADGE}", f"{intro} {updated}", navigation]
    for slug, body in sections.items():
        resource = "datasets" if slug == "datasets" else "papers"
        parts.extend([f"## {label(slug)}", body, f"[Browse all {resource} →](papers/{slug}.md)"])
    parts.append(
        "<details>\n<summary>Downloads and catalog maintenance</summary>\n\n"
        "Run `python download.py` to download paper PDFs. To update the list, edit "
        "[the selection](catalog/selected.md) or [the full catalog](catalog/full.md), "
        "then run `python3 scripts/build_pages.py`.\n\n</details>"
    )
    return "\n\n".join(parts) + "\n"


def render_section(slug, sections, updated):
    section = heading_link(slug)
    short = f"../{SELECTED}{section}"
    full = f"../{DETAILED}{section}"
    title = "Datasets and benchmarks" if slug == "datasets" else f"Papers from {label(slug)}"
    navigation = " | ".join(f"[{label(key)}]({key}.md)" for key in sections)
    parts = [
        f"[Selected papers]({short}) | [Full bibliography]({full})",
        f"# {title}",
        updated,
        navigation,
        sections[slug],
        f"[Back to selected papers]({short}) | [Back to full bibliography]({full})",
    ]
    return "\n\n".join(parts) + "\n"


def build_pages(root):
    catalog_dir = root / "catalog"
    full = (catalog_dir / "full.md").read_text(encoding="utf-8")
    selected = (catalog_dir / "selected.md").read_text(encoding="utf-8")
    full_sections = read_sections(full)
    selected_sections = read_sections(selected)
    if full_sections.keys() != selected_sections.keys():
        raise ValueError("Each catalog section needs a corresponding selected section.")
    updated = re.search(r"\*\*Last updated: \d{4}-\d{2}-\d{2}\.\*\*", full).group()
    outputs = {
        root / SELECTED: render_readme(selected_sections, updated, detailed=False),
        root / DETAILED: render_readme(full_sections, updated, detailed=True),
    }
    papers = root / "papers"
    papers.mkdir(exist_ok=True)
    for slug in full_sections:
        outputs[papers / f"{slug}.md"] = render_section(slug, full_sections, updated)
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    build_pages(Path(__file__).resolve().parents[1])
