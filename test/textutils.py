"""Прості функції для роботи з рядками."""

import argparse
import sys


def reverse_string(text: str) -> str:
    """Повертає рядок у зворотному порядку."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Перевіряє, чи є рядок паліндромом без урахування регістру,
    пробілів і розділових знаків."""
    cleaned = [char.lower() for char in text if char.isalnum()]
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """Повертає кількість слів у рядку."""
    return len(text.split()).


COMMANDS = {
    "reverse": reverse_string,
    "palindrome": is_palindrome,
    "words": count_words,
}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Утиліти для роботи з рядками")
    parser.add_argument("command", choices=COMMANDS.keys(), help="дія над рядком")
    parser.add_argument("text", help="вхідний рядок")
    args = parser.parse_args(argv)
    print(COMMANDS[args.command](args.text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
