from py.xml import html


def pytest_html_report_title(report):
    report.title = "Incorrect PHP Travels Login"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.h1("This test verifies the error message is displayed upon loggin in with incorrect credentials.")])
