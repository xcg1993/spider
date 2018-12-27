from unittest import TestCase
from dao.dao.db import DB

class DBTestCase(TestCase):
    def test_conn(self):
        db=DB(db='dytt')
        with db:
            self.assertIsNotNone(db.conn,'数据库连接失败')