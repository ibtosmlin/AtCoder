from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Any, Dict, List, Optional

from jinja2 import Environment, FileSystemLoader

from ..config.config_loader import ENCODING, PATHS

# =========================
# Tag
# =========================

LIB_FILE_PATTERN = "Lib_*.py"
MEMO_FILE_PATTERN = "Memo_*.md"
LINKS_FILE = "Links.json"


@dataclass(frozen=True)
class HtmlTagInfo:
    key: str
    marker: str


class HtmlTag(Enum):
    TITLE = HtmlTagInfo("title", "######title######")
    SUBTITLE = HtmlTagInfo("subtitle", "######subtitle######")
    NAME = HtmlTagInfo("name", "##############name##############")

    @property
    def key(self) -> str:
        return self.value.key

    @property
    def marker(self) -> str:
        return self.value.marker

    @classmethod
    def from_marker(cls, line: str) -> Optional[HtmlTag]:
        for tag in cls:
            if tag.marker == line:
                return tag
        return None


# =========================
# Segment（自動 order）
# =========================


@dataclass(frozen=True)
class SegmentInfo:
    code: str
    label: str


class Segment(Enum):
    # auto() を order として使う
    def _generate_next_value_(name, start, count, last_values):
        return count  # 0,1,2,... を返す

    A: tuple[SegmentInfo, auto] = (SegmentInfo("A", "一般アルゴリズム"), auto())
    D: tuple[SegmentInfo, auto] = (SegmentInfo("D", "データ構造"), auto())
    Q: tuple[SegmentInfo, auto] = (SegmentInfo("Q", "クエリ"), auto())
    G: tuple[SegmentInfo, auto] = (SegmentInfo("G", "グラフ"), auto())
    GB: tuple[SegmentInfo, auto] = (SegmentInfo("GB", "二部グラフ"), auto())
    GD: tuple[SegmentInfo, auto] = (SegmentInfo("GD", "有向グラフ"), auto())
    GT: tuple[SegmentInfo, auto] = (SegmentInfo("GT", "木"), auto())
    SP: tuple[SegmentInfo, auto] = (SegmentInfo("SP", "最短経路"), auto())
    N: tuple[SegmentInfo, auto] = (SegmentInfo("N", "整数"), auto())
    M: tuple[SegmentInfo, auto] = (SegmentInfo("M", "行列"), auto())
    STR: tuple[SegmentInfo, auto] = (SegmentInfo("Str", "文字列"), auto())
    AL: tuple[SegmentInfo, auto] = (SegmentInfo("AL", "幾何"), auto())
    O: tuple[SegmentInfo, auto] = (SegmentInfo("O", "その他"), auto())

    @property
    def info(self) -> SegmentInfo:
        return self.value[0]

    @property
    def order(self) -> int:
        return self.value[1]

    @property
    def code(self) -> str:
        return self.info.code

    @property
    def label(self) -> str:
        return self.info.label


# =========================
# モデル（型安全）
# =========================


@dataclass
class LibItem:
    fname: str
    title: str
    subtitle: List[str]


@dataclass
class LibCollection:
    items: Dict[str, List[LibItem]] = field(default_factory=dict)

    def add(self, key: str, item: LibItem):
        self.items.setdefault(key, []).append(item)

    def get(self, key: str) -> List[LibItem]:
        return self.items.get(key, [])


@dataclass
class MemoList:
    files: List[str]


@dataclass
class Links:
    data: Dict[str, Any]


@dataclass
class HtmlContext:
    segments: List[tuple]
    memos: MemoList
    links: Links

    @classmethod
    def build(cls, libs: LibCollection, memos: MemoList, links: Links):
        segments = [
            (seg.code, seg.label, libs.get(seg.code))
            for seg in sorted(Segment, key=lambda s: s.order)
        ]
        return cls(segments=segments, memos=memos, links=links)


# =========================
# パーサ
# =========================


def parse_lib_file(filepath: Path) -> Optional[LibItem]:
    with filepath.open("r", encoding=ENCODING) as f:
        lines = [line.strip() for line in f]

    title = None
    subtitle: List[str] = []
    current_tag: Optional[HtmlTag] = None

    for line in lines:
        tag = HtmlTag.from_marker(line)
        if tag:
            current_tag = tag
            continue

        if current_tag is HtmlTag.NAME:
            break

        if not line.startswith("# "):
            continue

        content = line[2:]
        if not content:
            continue

        if current_tag is HtmlTag.TITLE:
            title = content
        elif current_tag is HtmlTag.SUBTITLE:
            subtitle.append(content)

    if title:
        return LibItem(filepath.name, title, subtitle)

    return None


def collect_libs(lib_dir: Path) -> LibCollection:
    collection = LibCollection()

    for filepath in sorted(lib_dir.glob(LIB_FILE_PATTERN)):
        key = filepath.stem.split("_")[1]
        parsed = parse_lib_file(filepath)
        if parsed:
            collection.add(key, parsed)

    return collection


# =========================
# メモ・リンク読み込み
# =========================


def load_memos(lib_dir: Path) -> MemoList:
    files = [fp.name for fp in sorted(lib_dir.glob(MEMO_FILE_PATTERN))]
    return MemoList(files)


def load_links(links_path: Path) -> Links:
    with links_path.open(mode="r", encoding=ENCODING) as f:
        return Links(json.load(f))


# =========================
# HTML レンダリング
# =========================


def render_html(template_path: Path, output_path: Path, context: HtmlContext):
    env = Environment(loader=FileSystemLoader(template_path.parent, encoding=ENCODING))
    template = env.get_template(PATHS.HTML_TEMPLATE_FILE.name)

    html = template.render(
        segments=context.segments,
        memos=context.memos.files,
        links=context.links.data,
    )

    output_path.write_text(html, encoding=ENCODING)
    return f"✅ HTML generated: {output_path}"


# =========================
# メイン
# =========================


def main():
    libs = collect_libs(lib_dir=PATHS.LIBRARY)
    memos = load_memos(lib_dir=PATHS.LIBRARY)
    links = load_links(links_path=PATHS.LIBRARY / LINKS_FILE)

    context = HtmlContext.build(libs, memos, links)

    return render_html(
        template_path=PATHS.HTML_TEMPLATE_FILE,
        output_path=PATHS.HTML_OUTPUT_FILE,
        context=context,
    )


if __name__ == "__main__":
    print(main())
