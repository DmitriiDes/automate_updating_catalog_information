#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(generated_report_path, report_name, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(generated_report_path + report_name)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])
