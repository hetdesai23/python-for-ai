"""Reusable helper functions, separated from the main script."""


def clean_text(text: str) -> str:
    """Lowercase and strip whitespace from text."""
    return text.strip().lower()


def word_count(text: str) -> int:
    """Count words in a piece of text."""
    return len(text.split())


def summarize(texts: list[str]) -> dict:
    """Return simple stats about a list of texts."""
    return {
        "count": len(texts),
        "total_words": sum(word_count(t) for t in texts),
    }
