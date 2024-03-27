import coverage
import pytest

cov = coverage.Coverage()
cov.start()

pytest.main(['summ.py'])

cov.stop()
cov.save()

cov.xml_report(outfile='coverage.xml')
cov.html_report(directory='htmlcov')
