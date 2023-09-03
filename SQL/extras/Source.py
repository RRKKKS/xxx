import re
import time
from datetime import datetime
from IqArab import StartTime, iqthon
from IqArab.Config import Config
from IqArab.plugins import mention
help1 = ("**🝳 ⦙ كيفيه التنصيب :**")
help2 = ("**🝳 ⦙ قـائمـه الاوامـر :**\n**🝳 ⦙ قنـاه السـورس :** @SOURCE_NEON\n**🝳 ⦙ شـرح اوامـر السـورس : @VD_D_DD**\n**🝳 ⦙ شـرح فـارات السـورس : @VD_D_DD** \n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎⿻┊My  {mention} ٫ **\n‌‎**⿻┊BoT  {TG_BOT} ٫**\n**‌‎⿻┊TimE  {TM} ٫**\n**‌‎⿻┊‌‎VeRsIoN v1 ,** \n**⿻┊‌‎neon ** @SOURCE_NEON"
