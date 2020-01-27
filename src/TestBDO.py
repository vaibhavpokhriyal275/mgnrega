import sqlite3

import mock
from BDO import BDO


class Test_BDO:

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_gpm_create_success(self, inputs, login, db):
        inputs.side_effect = ['Vaibhav', 'Pokhriyal', 'Karnataka', '7th Cross Road', 560034, 'v@gmail.com', 'v']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().gpm_create() == True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_gpm_create_failure(self, inputs, login, db):
        inputs.side_effect = ['Vaibhav', 'Pokhriyal', 'Karnataka', '7th Cross Road', 560034, 'v@gmail.com', 'v']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert BDO().gpm_create() == False

