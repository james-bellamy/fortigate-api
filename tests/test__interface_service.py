"""unittest internet_service.py"""

import unittest

from fortigate_api.internet_service import InternetService
from tests.helper__tst import NAME1, NAME2, NAME3, MockFortigate


# noinspection DuplicatedCode
class Test(MockFortigate):
    """InternetService"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = InternetService(rest=self.rest)

    def test_valid__create(self):
        """InternetService.create()"""
        for name, req in [
            (NAME1, 200),  # present in the Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name}).status_code
            self.assertEqual(result, req, msg=f"{name=}")

    def test_valid__delete(self):
        """InternetService.delete()"""
        for kwargs, req in [
            (dict(uid=NAME1), 200),
            (dict(uid=NAME2), 500),
            (dict(filter=f"name=={NAME1}"), 200),
            (dict(filter=f"name=={NAME2}"), 200),
        ]:
            result = self.obj.delete(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__get(self):
        """InternetService.get()"""
        for kwargs, req in [
            (dict(uid=NAME1), [NAME1]),
            (dict(uid="NAME9"), []),
        ]:
            result_ = self.obj.get(**kwargs)
            result = [d["name"] for d in result_]
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__update(self):
        """InternetService.update()"""
        for kwargs, req in [
            (dict(uid=NAME1, data=dict(name=NAME1)), 200),
            (dict(uid="NAME9", data=dict(name="NAME9")), 500),
            (dict(data=dict(name=NAME1)), 200),
            (dict(data=dict(name="NAME9")), 500),
        ]:
            result = self.obj.update(**kwargs).status_code
            self.assertEqual(result, req, msg=f"{kwargs=}")

    def test_valid__is_exist(self):
        """Address.is_exist()"""
        for uid, req in [
            (NAME1, True),
            ("NAME9", False),
        ]:
            result = self.obj.is_exist(uid=uid)
            self.assertEqual(result, req, msg=f"{uid=}")


if __name__ == "__main__":
    unittest.main()
