import unittest
import os
import secrets
import sys
sys.path.append("..")
from wrapmail.smtp.email import SMTP_mail

class SMTP_mailTest(unittest.TestCase):

    def setUp(self):
        self.html_template = "test_html_temp.html"
        self.pdf_attachment = "test_pdf_attach.pdf"
        self.from_mail = os.environ.get("EMAIL")
        self.to_mail = os.environ.get("TARGET")
    
    def test_text_mail(self):
        mail = SMTP_mail(self.to_mail, "test_text_mail", "test")
        mail.send()
    
    def test_text_mail_with_attachment(self):
        mail = SMTP_mail(self.to_mail, "test_text_mail_with_attachment", "test")
        mail.add_attachment("documents/test_pdf_attach.pdf")
        mail.send()
    
    def test_text_mail_with_multiple_attachments(self):
        mail = SMTP_mail(self.to_mail, "test_text_mail_with_multiple_attachments", "test")
        mail.add_attachment("documents/test_pdf_attach.pdf")
        mail.add_attachment("documents/pdf-test.pdf")
        mail.send()
    
    def test_html_mail(self):
        mail = SMTP_mail(self.to_mail, "test_html_mail", "test", html="documents/test_html_temp.html")
        mail.send()
    
    def test_html_mail_with_attachment(self):
        mail = SMTP_mail(self.to_mail, "test_html_mail_with_attachment", "test", html="documents/test_html_temp.html")
        mail.add_attachment("documents/test_pdf_attach.pdf")
        mail.send()
    
    def test_html_mail_with_multiple_attachments(self):
        mail = SMTP_mail(self.to_mail, "test_html_mail_with_multiple_attachments", "test", html="documents/test_html_temp.html")
        mail.add_attachment("documents/test_pdf_attach.pdf")
        mail.add_attachment( "documents/pdf-test.pdf")
        mail.send()
    
    def test_jpg_attachment(self):
        mail = SMTP_mail(self.to_mail, "test_jpg_attachment", "test", html="documents/test_html_temp.html")
        mail.add_attachment("documents/harita.jpg")
        mail.send()
    
    def test_png_attachment(self):
        mail = SMTP_mail(self.to_mail, "test_png_attachment", "test", html="documents/test_html_temp.html")
        mail.add_attachment("documents/meme.png")
        mail.send()
    
    def test_pdf_and_jpg(self):
        mail = SMTP_mail(self.to_mail, "test_pdf_and_jpg", "test", html="documents/test_html_temp.html")
        mail.add_attachment("documents/harita.jpg")
        mail.add_attachment( "documents/pdf-test.pdf")
        mail.send()