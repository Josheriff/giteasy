from expects import expect, equal

SPANISH_STATUS_TEXT = """
M  easygit.py
 M spec.py
MM spec.py
?? lololo.py
"""



ENGLISH_STATUS_TEXT = """
A  easygit.py
 M spec.py
?? lololo.py
"""

with describe('Given a git status --short text'):
    with context('it contains all files commited'):
        with it('returns an empty list'):


