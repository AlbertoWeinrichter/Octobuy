import logging

from source.bot_scripts.SNKRS import SNKRSBot
from source.conf.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def snkrs(product_id):
    bot = SNKRSBot(product_id)
    bot.run()
