#!/usr/bin/env python3
"""Validate inline JavaScript in the static portfolio pages with Node.js."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile


class InlineScriptParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.scripts = []
        self._current = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "script" or self._current is not None:
            return
        attributes = dict(attrs)
        script_type = attributes.get("type", "").strip().lower()
        if "src" not in attributes and script_type not in {"application/ld+json", "application/json"}:
            self._current = []

    def handle_data(self, data):
        if self._current is not None:
            self._current.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "script" and self._current is not None:
            self.scripts.append("".join(self._current))
            self._current = None


def main():
    pages = [Path("index.html"), Path("privacy.html")]
    failed = False
    with tempfile.TemporaryDirectory(prefix="judo-js-check-") as temp_dir:
        temp_root = Path(temp_dir)
        for page in pages:
            if not page.is_file():
                print(f"FAIL: missing {page}", file=sys.stderr)
                failed = True
                continue
            parser = InlineScriptParser()
            parser.feed(page.read_text(encoding="utf-8"))
            if not parser.scripts:
                print(f"FAIL: no inline JavaScript found in {page}", file=sys.stderr)
                failed = True
                continue
            for index, source in enumerate(parser.scripts, start=1):
                script_path = temp_root / f"{page.stem}-{index}.js"
                script_path.write_text(source, encoding="utf-8")
                result = subprocess.run(
                    ["node", "--check", str(script_path)],
                    text=True,
                    capture_output=True,
                    check=False,
                )
                if result.returncode != 0:
                    print(f"FAIL: JavaScript syntax error in {page}, inline script {index}", file=sys.stderr)
                    print(result.stdout + result.stderr, file=sys.stderr)
                    failed = True
                else:
                    print(f"PASS: {page}, inline script {index}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
