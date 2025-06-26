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

# You can add other functions or classes that might be expected by deal_form_view.py
# For example, if it expects an EmailService class:
# class EmailService:
#     def __init__(self, config=None):
#         self.config = config
#         logger.info("Dummy EmailService initialized.")

#     def send_deal_email_via_sharepoint(self, *args, **kwargs):
#         logger.info("Attempted to send deal email via SharePoint service (dummy EmailService class).")
#         pass

#     # Add any other methods that deal_form_view.py might try to call
#     def some_other_email_function(self, *args, **kwargs):
#         logger.info("Called some_other_email_function (dummy).")
#         pass

logger.info("Dummy email_service.py loaded.")
