# app/services/email_service.py
import logging

logger = logging.getLogger(__name__)

def send_deal_email_via_sharepoint_service(*args, **kwargs):
    """
    Dummy function for sending deal emails.
    In this distribution, full email functionality may be disabled.
    """
    logger.info("Attempted to send deal email via SharePoint service (dummy implementation).")
    # In a real scenario, you might raise an error or return a specific status
    # For now, just log and do nothing.
    pass

logger.info("Dummy email_service.py loaded.")
