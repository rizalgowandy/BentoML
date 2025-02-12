from __future__ import annotations

import typing as t

class Pattern:
    __slots__: tuple[str, ...] = ...

    def __init__(self, include: bool | None) -> None: ...
    def match(self, files: t.Iterable[t.Text]) -> t.Iterator[t.Text]: ...

class RegexPattern(Pattern):
    def __init__(
        self, pattern: t.AnyStr | t.Pattern[t.Any], include: bool | None = ...
    ) -> None: ...
    def __eq__(self, other: RegexPattern) -> bool: ...
    @classmethod
    def pattern_to_regex(cls, pattern: t.Text) -> tuple[t.Text, bool]: ...
