from expects import expect, equal

######### "Production" code ##########################

def list_formatter(text):
    pass


#####################################################


CLEAN = None

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
    with context('it contains nothing because all is up to date'):
        with it('list formatter returns an empty list'):

            result = list_formatter(CLEAN)

            expected_result = []

            expect(result).to(equal(expected_result))
