"""Offline tests for ICTRSearcher."""
from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path

from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import ictr_adapter as adapter  # noqa: E402


class FakeHttp:
    def __init__(self, html):
        self.html = html
        self.evidence = []

    def soup(self, url, params=None, headers=None):
        return BeautifulSoup(self.html, "html.parser"), {
            "source_url": "https://unictr.irmct.org/search",
            "http_status": 200, "content_type": "text/html", "bytes": 100,
            "retrieved_at": "2026-11-09T00:00:00Z", "sha256": "0" * 64,
        }


def args(**kwargs):
    base = dict(limit=2, offset=0, cache=".cache", offline=False, cache_ttl=0, timeout=30)
    base.update(kwargs)
    return argparse.Namespace(**base)


class IctrTests(unittest.TestCase):
    def test_search_parses_news_and_case_links(self):
        html = """
        <html><head><title>Search results for "Akayesu"</title></head><body>
        <div class="search-results">
          <h3><a href="/en/news/akayesu">Historic judgement finds Akayesu guilty</a></h3>
          <h3><a href="/en/cases/akayesu">Akayesu case</a></h3>
        </div></body></html>
        """
        out = adapter.search("Akayesu", args(), FakeHttp(html))
        self.assertEqual(out["status"], "ok")
        self.assertEqual(out["results"][0]["section"], "news-or-press")
        self.assertEqual(out["results"][1]["section"], "case-page")


if __name__ == "__main__":
    unittest.main()
