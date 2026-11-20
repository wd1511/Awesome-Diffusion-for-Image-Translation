"""Build both reading views and the standalone pages from the two catalog files."""

import re
from pathlib import Path

VIEWS = {"selected": "Selected papers", "full": "Full bibliography"}
TITLE = "Diffusion for Image-to-Image Translation"
BADGE = "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/wd1511/Awesome-Diffusion-for-Image-Translation)"


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


def fragment(target):
    # GitHub prefixes anchor names during sanitization. A literal fragment lets the
    # browser reveal the target inside a closed disclosure, including on direct links.
    return f"#user-content-{target}"


def anchor(target):
    # The ID also resolves the literal fragment in renderers that keep names as written.
    return f'<a name="{target}" id="user-content-{target}"></a>'


def navigation(slugs, view, standalone):
    links = []
    for slug in slugs:
        target = f"{slug}.md{fragment(view + '-view')}" if standalone else fragment(f"{view}-{slug}")
        links.append(f"[{label(slug)}]({target})")
    return " | ".join(links)


def section_text(slug, body, view, default, standalone):
    other = "full" if view == "selected" else "selected"
    destination = fragment(f"{other}-{'view' if standalone else slug}")
    switch = f"[{VIEWS[other]}]({destination})"
    parts = [anchor(f"{view}-{slug}")]
    if view == default and not standalone:
        if slug == "datasets":
            parts.append(anchor("dataset"))
        elif slug == "before-2021":
            parts.append(anchor("before-2021"))
            if view == "selected":
                parts.append(anchor("2021"))
    if not standalone:
        parts += [f"## {label(slug)}", switch]
    parts.append(body)
    if standalone:
        overview = "README.md" if view == "selected" else "PAPERS.md"
        target = fragment(f"{view}-{slug}")
        parts.append(f"{switch} | [Back to overview](../{overview}{target})")
    else:
        resource = "datasets" if slug == "datasets" else "papers"
        parts.append(f"{switch} | [Browse all {resource} →](papers/{slug}.md)")
    return "\n\n".join(parts)


def render_page(catalog, updated, default, slug=None):
    other = "full" if default == "selected" else "selected"
    slugs = list(catalog["full"])
    switches = " | ".join(f"[{name}]({fragment(view + '-view')})" for view, name in VIEWS.items())
    if slug:
        title = "Datasets and benchmarks" if slug == "datasets" else f"Papers from {label(slug)}"
        parts = [switches, f"# {title}", updated]
    else:
        intro = "Diffusion and flow models for image translation, editing, and style transfer."
        parts = [switches, f"# {TITLE} {BADGE}", f"{intro} {updated}"]
    for view in (default, other):
        opened = " open" if view == default else ""
        parts += [
            f'<details name="reading-view"{opened}>\n<summary><strong>{VIEWS[view]}</strong></summary>',
            anchor(f"{view}-view"),
            navigation(slugs, view, bool(slug)),
        ]
        for key in [slug] if slug else slugs:
            parts.append(section_text(key, catalog[view][key], view, default, bool(slug)))
        parts.append("</details>")
    if not slug:
        parts.append(
            "<details>\n<summary>Downloads and catalog maintenance</summary>\n\n"
            "Run `python download.py` to download paper PDFs. To update the list, edit "
            "[the selection](catalog/selected.md) or [the full catalog](catalog/full.md), "
            "then run `python3 scripts/build_pages.py`.\n\n</details>"
        )
    return "\n\n".join(parts) + "\n"


def build_pages(root):
    catalog_dir = root / "catalog"
    full = (catalog_dir / "full.md").read_text(encoding="utf-8")
    selected = (catalog_dir / "selected.md").read_text(encoding="utf-8")
    catalog = {"full": read_sections(full), "selected": read_sections(selected)}
    if catalog["full"].keys() != catalog["selected"].keys():
        raise ValueError("Each catalog section needs a corresponding selected section.")
    updated = re.search(r"\*\*Last updated: \d{4}-\d{2}-\d{2}\.\*\*", full).group()
    outputs = {
        root / "README.md": render_page(catalog, updated, "selected"),
        root / "PAPERS.md": render_page(catalog, updated, "full"),
    }
    papers = root / "papers"
    papers.mkdir(exist_ok=True)
    for slug in catalog["full"]:
        outputs[papers / f"{slug}.md"] = render_page(catalog, updated, "full", slug)
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    build_pages(Path(__file__).resolve().parents[1])
