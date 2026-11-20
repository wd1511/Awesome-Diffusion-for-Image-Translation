"""Generate the standalone reading pages from the full bibliography."""

import re
from pathlib import Path


def build_pages(root):
    source = (root / "PAPERS.md").read_text(encoding="utf-8")
    sections = re.split(r"^## (Datasets?|\d{4})\n", source, flags=re.MULTILINE)
    updated = re.search(r"\*\*Last updated: \d{4}-\d{2}-\d{2}\.\*\*", sections[0]).group()
    nav = next(line for line in sections[0].splitlines() if line.startswith("[Datasets](papers/"))
    papers = root / "papers"
    papers.mkdir(exist_ok=True)

    pages = {}
    for heading, body in zip(sections[1::2], sections[2::2]):
        if heading in {"Dataset", "Datasets"}:
            pages["datasets"] = ["Datasets and benchmarks", heading.lower(), body.strip()]
        elif int(heading) <= 2021:
            early = pages.setdefault("before-2021", ["Papers from 2021 and earlier", "2021"])
            early.append(f"## {heading}\n\n{body.strip()}")
        else:
            pages[heading] = [f"{heading} papers", heading, body.strip()]

    for slug, (title, anchor, *content) in pages.items():
        brief = f"../README.md#{slug}"
        full = f"../PAPERS.md#{anchor}"
        parts = [
            f"[简要版]({brief})｜[完整版]({full})",
            f"# {title}",
            updated,
            nav.replace("](papers/", "]("),
            *content,
            f"[← Back to selected papers]({brief}) · [Full bibliography]({full})",
        ]
        (papers / f"{slug}.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_pages(Path(__file__).resolve().parents[1])
