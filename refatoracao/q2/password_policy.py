from __future__ import annotations


class PasswordPolicy:

    def is_valid(self, password: str | None) -> bool:
        return (
            password is not None
            and len(password) >= 10
            and self._has_upper(password)
            and self._has_digit(password)
            and " " not in password
        )

    def _has_upper(self, p: str) -> bool:
        return any(c.isupper() for c in p)

    def _has_digit(self, p: str) -> bool:
        return any(c.isdigit() for c in p)

