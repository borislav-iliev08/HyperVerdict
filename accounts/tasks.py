
import logging

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from accounts.models import ProfileBaseUser

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def send_email_to_user(self, user_id):
    try:
        user = ProfileBaseUser.objects.get(pk=user_id)
    except ProfileBaseUser.DoesNotExist:
        logger.warning('User %s does not exist.', user_id)
        return {'status': 'missing', 'user_id': user_id}

    try:
        send_mail(
            subject="Welcome to HyperVerdict – Your account is ready!!!",
            message=(
                f"Hello, {user.first_name} {user.last_name}!\n\n"
                f"WELCOME TO HYPERVERDICT\n\n"
                f"Your account has been successfully created. "
                f"We're excited to have you as part of our community!\n\n"
                f"HyperVerdict brings clients and trusted legal and real estate "
                f"professionals together, making it easier to find expert assistance, "
                f"manage appointments, and stay connected throughout your consultations.\n\n"
                f"GETTING STARTED\n\n"
                f"Here are a few things you can do next:\n\n"
                f"1. Complete your profile to introduce yourself.\n"
                f"2. Explore our professional directory and find an expert who matches your needs.\n"
                f"3. Schedule your first appointment and take the next step.\n\n"
                f"Your journey starts here.\n\n"
                f"Thank you for choosing HyperVerdict. We're glad to have you with us.\n\n"
                f"Best regards,\n"
                f"The HyperVerdict Team"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        logger.info('Welcome email successfully sent to %s', user.email)
        return {'status': 'sent', 'user_id': user_id}

    except Exception as exc:
        logger.exception('Failed to send welcome email to %s', user.email)
        raise self.retry(exc=exc)
