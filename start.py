from scrapper.instagram import instagram
from utils.log import log

log.getInstance().printLog('Start the scrapper for instagram.')

instagram.getInstance().start()

log.getInstance().printLog('End the scrapper for instagram. See you later.')
