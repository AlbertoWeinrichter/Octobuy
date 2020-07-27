import logging


from source.bot_scripts.SNKRS import SNKRSBot
from source.conf.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def snkrs(product_id):
    print("HELLO, NURSE!")
    print("HELLO, NURSE!")
    print("HELLO, NURSE!")

    # w = SNKRSBot(product_id)
    # w.set_up_mobile()
    # w.register()
