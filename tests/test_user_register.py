import pytest

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    data_with_one_empty_param = [
        ({'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
         'password'),
        ({'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
         'username'),
        ({'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'},
         'firstName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'vinkotov@example.com'},
         'lastName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}, 'email')
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data()
        data['username'] = 'l'
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Unexpected response content {response.content}"

    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data()
        data[
            'username'] = 'ThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongName'
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize("data", data_with_one_empty_param)
    def test_create_user_with_empty_fields(self, data):
        data, empty_param = data
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {empty_param}", f"Unexpected response content {response.content}"
