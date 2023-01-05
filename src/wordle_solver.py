#!/usr/bin/env python3
from collections import Counter
from re import compile
from re import Pattern
from typing import List

import requests


class WordleSolver:
    WORD_REFERENCE_URL: str = "https://meaningpedia.com/5-letter-words?show=all"
    WORD_REFERENCE_HTML_IDENTIFIER_REGEX: str = r'<span itemprop="name">(\w+)</span>'
    WORD_REFERENCE_HTML_IDENTIFIER_REGEX_PATTERN: Pattern = compile(
        pattern=WORD_REFERENCE_HTML_IDENTIFIER_REGEX
    )

    def __init__(self):
        word_list_raw_html = requests.get(url=self.WORD_REFERENCE_URL)

        self.remaining_words = set(
            self.WORD_REFERENCE_HTML_IDENTIFIER_REGEX_PATTERN.findall(
                string=word_list_raw_html.text
            )
        )

        self.previous_estimate = None

    def _identify_most_common_letters(self) -> list[str]:
        """returns 5 most frequent letters in descending order"""

        remaining_character_count = [
            char for remaining_word in self.remaining_words for char in remaining_word
        ]

        most_frequent_char_cnts = Counter(remaining_character_count).most_common(5)

        most_frequent_chars = [char for char, _ in most_frequent_char_cnts]

        return most_frequent_chars

    # def _identify_most_common_letter_position(self) -> List[str]:
    #     """returns 5 most frequent letters in descending order"""
    #
    #     remaining_character_count = [
    #         (char, i) for remaining_word in self.remaining_words for i, char in enumerate(remaining_word)
    #     ]
    #
    #     most_frequent_char_cnts = Counter(remaining_character_count).most_common(5)
    #
    #     most_frequent_chars = [char for char, _ in most_frequent_char_cnts]
    #
    #     return most_frequent_chars

    def provide_best_estimate(self):
        pass


if __name__ == "__main__":
    wordle_solver = WordleSolver()
    print(wordle_solver.remaining_words)
    print(wordle_solver._identify_most_common_letters())
