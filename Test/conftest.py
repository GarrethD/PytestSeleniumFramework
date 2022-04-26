import os
from datetime import datetime

import pytest
from py.xml import html

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     if not os.path.exists('reports'):
#         os.makedirs('reports')
#     config.option.htmlpath = 'reports/Report - '+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
#
# def pytest_html_report_title(report):
#     report.title = "Incorrect PHP Travels Login"
#
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.h1("This test verifies the error message is displayed upon loggin in with incorrect credentials.")])


