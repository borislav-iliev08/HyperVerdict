import logging
from accounts.tasks import send_email_to_user
logger = logging.getLogger(__name__)


def enqueue_welcome_email(user_id):
    try:
        return send_email_to_user.apply_async(args=[user_id],queue='welcome')
    except Exception:
        logger.exception('Unable to enqueue welcome email for user %s',user_id)

        return None
