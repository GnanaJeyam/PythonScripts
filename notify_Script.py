import notify2
from bsfour import GetScore
ICON_PATH = "/home/gnanajeyam/Desktop/py_scripts/india-cricket-icon-vector-783535.jpg"
notify2.init("News Notifier")
# Getting score from GetScore class
appc = GetScore.score
n = notify2.Notification(appc, icon = ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10)
n.show()
