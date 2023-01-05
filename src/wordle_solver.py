#!/usr/bin/env python3

from re import compile
from re import Pattern

import requests


class WordleSolver:
    WORD_REFERENCE_URL: str = "https://meaningpedia.com/5-letter-words?show=all"
    WORD_REFERENCE_HTML_IDENTIFIER_REGEX: str = r'<span itemprop="name">(\w+)</span>'
    WORD_REFERENCE_HTML_IDENTIFIER_REGEX_PATTERN: Pattern = compile(pattern=WORD_REFERENCE_HTML_IDENTIFIER_REGEX)

    def __init__(self):
        word_list_raw_html = requests.get(
            url=self.WORD_REFERENCE_URL
        )

        self.remaining_words = self.WORD_REFERENCE_HTML_IDENTIFIER_REGEX_PATTERN.findall(
            string=word_list_raw_html.text
        )


if __name__ == "__main__":
    wordle_solver = WordleSolver()
    print(wordle_solver.remaining_words)
