import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(**kwargs):
    """
    :return:
    """
    from_addr = kwargs["mail_user"]
    password = kwargs["mail_pass"]
    smtp_server = kwargs["mail_host"]

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('来自<%s>接口测试' % from_addr)
    msg['To'] = _format_addr(' <%s>' % kwargs["to_addr"])
    msg['Subject'] = Header(kwargs["header_msg"], 'utf-8').encode()
    msg.attach(MIMEText(kwargs["attach"], 'plain', 'utf-8'))

    if kwargs.get("report", "0") != "0":
        part = MIMEApplication(open(kwargs["report"], 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', kwargs["report_name"]))
        msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, kwargs["port"])

    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, kwargs["to_addr"], msg.as_string())
    server.quit()


if __name__ == '__main__':
    to_addr = []
    mail_host = ""
    mail_user = ""
    mail_pass = ""
    port = ""
    header_msg = ""
    attach = ""

    report = PATH("../Log/report.xlsx")
    send_mail(
        to_addr=to_addr, mail_host=mail_host, mail_user=mail_user, port=port, mail_pass=mail_pass,
        header_msg=header_msg, report=report, attach=attach, report_name="接口测试报告"
    )
