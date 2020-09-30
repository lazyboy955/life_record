from django.core.mail import send_mail
from django.conf import settings
from django.http.response import HttpResponse
import logging


def send_message(email_title, message, email_to_list, logger=logging.getLogger(__name__)):
    res = send_mail(email_title,
                    message,
                    settings.EMAIL_FROM,
                    email_to_list)
    logger.info(f'开始向{email_to_list}发送邮件！')
    logger.info(f'邮件内容:\n {email_title} \n {message}')
    if res == 1:
        logger.info('邮件发送成功')
    else:
        logger.warning('邮件发送失败')
