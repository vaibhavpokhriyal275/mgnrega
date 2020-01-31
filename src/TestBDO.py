import sqlite3

import mock
from BDO import BDO


class Test_BDO:

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.dashboard')
    @mock.patch('BDO.input')
    def test_login_success(self, inputs, dashboard, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        inputs.side_effect = ['test@test', 'test']
        db_mock.execute.return_value.fetchone.return_value = [1, 'test@test', 'test']
        dashboard.return_value = True
        assert BDO().login() is True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.input')
    def test_login_incorrect_credential(self, inputs, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        inputs.side_effect = ['test@test', 'test']
        db_mock.execute.return_value.fetchone.side_effect = None, 1
        assert BDO().login() is True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.dashboard')
    @mock.patch('BDO.input')
    def test_login_error(self, inputs, dashboard, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        inputs.side_effect = ['test@test', 'test']
        db_mock.execute.return_value.fetchone.side_effect = Exception
        assert BDO().login() is False

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.gpm_create')
    def test_dashboard_choice_1(self, create, inputs, login):
        inputs.return_value = '1'
        create.return_value = True
        assert BDO().dashboard('test') is 1

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.gpm_update')
    def test_dashboard_choice_2(self, update, inputs, login):
        inputs.return_value = '2'
        update.return_value = True
        assert BDO().dashboard('test') is 2

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.gpm_delete')
    def test_dashboard_choice_3(self, delete, inputs, login):
        inputs.return_value = '3'
        delete.return_value = True
        assert BDO().dashboard('test') is 3

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.project_create')
    def test_dashboard_choice_4(self, project, inputs, login):
        inputs.return_value = '4'
        project.return_value = True
        assert BDO().dashboard('test') is 4

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.project_update')
    def test_dashboard_choice_5(self, project, inputs, login):
        inputs.return_value = '5'
        project.return_value = True
        assert BDO().dashboard('test') is 5

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.project_delete')
    def test_dashboard_choice_6(self, project, inputs, login):
        inputs.return_value = '6'
        project.return_value = True
        assert BDO().dashboard('test') is 6

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.member_approve')
    def test_dashboard_choice_7(self, member, inputs, login):
        inputs.return_value = '7'
        member.return_value = True
        assert BDO().dashboard('test') is 7

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_dashboard_choice_else(self, inputs, login):
        inputs.return_value = '8'
        assert BDO().dashboard('test') is False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_gpm_create_success(self, inputs, login, db):
        inputs.side_effect = ['Vaibhav', 'Pokhriyal', 'Karnataka', '7th Cross Road', 560034, 'v@gmail.com', 'v']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().gpm_create() is True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_gpm_create_failure(self, inputs, login, db):
        inputs.side_effect = ['Vaibhav', 'Pokhriyal', 'Karnataka', '7th Cross Road', 560034, 'v@gmail.com', 'v']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert BDO().gpm_create() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.BDO.gpm_view')
    @mock.patch('BDO.input')
    def test_gpm_update_success(self, inputs, gpm_view, login, db):
        gpm_view.return_value = [1, 2, 'test', 'test', 'test', 'test', 2, 'test', 'test']
        inputs.side_effect = ['test', 'test', 'test', 'test', 'test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().gpm_update() == True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.BDO.gpm_view')
    @mock.patch('BDO.input')
    def test_gpm_update_failure(self, inputs, gpm_view, login, db):
        gpm_view.return_value = [1, 2, 'test', 'test', 'test', 'test', 2, 'test', 'test']
        inputs.side_effect = ['test', 'test', 'test', 'test', 'test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = Exception
        assert BDO().gpm_update() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.BDO.gpm_view')
    @mock.patch('BDO.input')
    def test_gpm_delete_yes(self, inputs, gpm_view, login, db):
        gpm_view.return_value = [1, 2, 'test', 'test', 'test', 'test', 2, 'test', 'test']
        inputs.return_value = 'Y'
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().gpm_delete() == True

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.BDO.gpm_view')
    @mock.patch('BDO.input')
    def test_gpm_delete_no(self, inputs, gpm_view, login):
        gpm_view.return_value = [1, 2, 'test', 'test', 'test', 'test', 2, 'test', 'test']
        inputs.return_value = ''
        assert BDO().gpm_delete() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_project_create_success(self, inputs, login, db):
        inputs.side_effect = ['Test', 1, 'Test', 'Test', 'Test', 'Test', 'Test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().project_create() == True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_project_create_error(self, inputs, login, db):
        inputs.side_effect = ['Test', 1, 'Test', 'Test', 'Test', 'Test', 'Test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert BDO().project_create() == False

    @mock.patch('BDO.BDO.login', return_value=True)
    @mock.patch('BDO.input')
    def test_project_create_wrong_choice(self, inputs, login):
        inputs.side_effect = ['Test', 4, 'Test', 'Test', 'Test', 'Test', 'Test']
        assert BDO().project_create() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.projects_view')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_project_update_success(self, login, inputs, projects_view, db):
        projects_view.return_value = None
        inputs.side_effect = [1, 'test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().project_update() == True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.projects_view')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_project_update_failure(self, login, inputs, projects_view, db):
        projects_view.return_value = None
        inputs.side_effect = [1, 'test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = Exception
        assert BDO().project_update() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.projects_view')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_project_delete_success(self, login, inputs, projects_view, db):
        projects_view.return_value = None
        inputs.return_value = 1
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().project_delete() == True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.projects_view')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_project_delete_failure(self, login, inputs, projects_view, db):
        projects_view.return_value = None
        inputs.return_value = 1
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = Exception
        assert BDO().project_delete() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.member_view_unapproved')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_member_approve_success(self, login, inputs, member_view_unapproved, db):
        member_view_unapproved.return_value = [1, 'Test']
        inputs.return_value = 1
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert BDO().member_approve() is True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.member_view_unapproved')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_member_approve_failure(self, login, inputs, member_view_unapproved, db):
        member_view_unapproved.return_value = True
        inputs.return_value = 1
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = Exception
        assert BDO().member_approve() is False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_gpm_view_success(self, login, inputs, db):
        inputs.return_value = 'test@test'
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchone.return_value = [1, 'test', 'test']
        assert BDO().gpm_view() == [1, 'test', 'test']

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.input')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_gpm_view_failure(self, login, inputs, db):
        inputs.return_value = 'test@test'
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = Exception
        assert BDO().gpm_view() == False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_projects_view_success(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchall.return_value = True
        assert BDO().projects_view() is True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_projects_view_failure(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchall.side_effect = Exception
        assert BDO().projects_view() is False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_member_view_unapproved_success(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchall.return_value = True
        assert BDO().member_view_unapproved() is True

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_member_view_unapproved_failure(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchall.side_effect = Exception
        assert BDO().member_view_unapproved() is False

    @mock.patch('BDO.db.sql_connection')
    @mock.patch('BDO.BDO.login', return_value=True)
    def test_member_view_unapproved_no_members(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchall.return_value = None
        assert BDO().member_view_unapproved() is False
