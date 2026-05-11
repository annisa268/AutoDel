#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "35598012"))
API_HASH     = os.environ.get("API_HASH", "1f047852265a6f2b590fad84bc9ca347")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "8700666009:AAGtKvJb60-_tsBWdnLovhCJ5rtJjlQ_EKc")
SESSION      = os.environ.get("SESSION", "1BQANOTEuMTA4LjU2LjE0NgG7gsMhlKdRP0ycPrluxD0qAIsZhDOqeS4yztqPtoQ+fSp050pmXWyMoWx9L2tAHiQz26gYHsViATFx8JTI5BxqAExYOHNEGuYRt7cCR1k0FgTXFLCS8IeCFk3+dwvKEinQM2fk+nKoSHmlZUnUrEgsf82/zcbqs5iroUP7/3ANpoOEMoxBy49ABxq1VtHVW8vbdQOWMdqn9i49vC1ofhuLomH5q07MnNuKaZc3ANKYeir+L/gW4WAL3ciBDUIAmKjdIPZqPFE3T/bX9JFM2sg4ZRcrL1FJd5AGnfo16KJ+JMl4acrlPf9SdVw6xLAbrVPUR+seFzLo+N2jxl9zsCAEBg==")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb://admin:M4D%25ch7un7ogFBej@localhost:27017/amber_core_db?authSource=admin&retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
