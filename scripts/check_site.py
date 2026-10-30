from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
errors = []


def local_path(value: str, source: Path):
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or value.startswith("#"):
        return None
    return (source.parent / parsed.path).resolve()


class SiteParser(HTMLParser):
    def __init__(self, source: Path):
        super().__init__()
        self.source = source
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            value = attributes["id"]
            if value in self.ids:
                errors.append(f"{self.source}: trùng id '{value}'")
            self.ids.add(value)

        for name in ("src", "href", "action"):
            value = attributes.get(name)
            if not value:
                continue
            target = local_path(value, self.source)
            if target and not target.is_file():
                errors.append(f"{self.source}: {name} không tồn tại: {value}")


def check_html():
    for source in ROOT.rglob("*.html"):
        parser = SiteParser(source)
        try:
            parser.feed(source.read_text(encoding="utf-8"))
            parser.close()
        except UnicodeDecodeError as exc:
            errors.append(f"{source}: không đọc được UTF-8 ({exc})")


def check_css():
    for source in ROOT.rglob("*.css"):
        text = source.read_text(encoding="utf-8")
        if text.count("{") != text.count("}"):
            errors.append(f"{source}: ngoặc CSS không cân bằng")
        for url in re.findall(r"url\((?:['\"]?)([^)'\"]+)", text):
            target = local_path(url, source)
            if target and not target.is_file():
                errors.append(f"{source}: tài nguyên CSS không tồn tại: {url}")


check_html()
check_css()

if errors:
    print("\n".join(f"::error::{error}" for error in errors))
    sys.exit(1)

print("OK: HTML, CSS và tài nguyên cục bộ đều hợp lệ.")
