import pytest

from textutils import count_words, is_palindrome, main, reverse_string


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "olleh"),
        ("Київ", "вїиК"),
        ("", ""),
        ("a b c", "c b a"),
    ],
    ids=["latin", "cyrillic", "empty", "spaces"],
)
def test_reverse_string(text, expected):
    assert reverse_string(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("level", True),
        ("A man, a plan, a canal: Panama", True),
        ("Нагорі роган", True),
        ("hello", False),
        ("", True),
    ],
    ids=["word", "phrase", "cyrillic-phrase", "not-palindrome", "empty"],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("one two three", 3),
        ("  кілька   пробілів  ", 2),
        ("", 0),
    ],
    ids=["three-words", "extra-spaces", "empty"],
)
def test_count_words(text, expected):
    assert count_words(text) == expected


def test_main_prints_result(capsys):
    assert main(["reverse", "abc"]) == 0
    assert capsys.readouterr().out.strip() == "cba"


def test_main_rejects_unknown_command():
    with pytest.raises(SystemExit):
        main(["unknown", "abc"])
