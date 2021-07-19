import allure
import pytest

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


@allure.epic('Registration cases')
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

    @allure.description('This test try to create user')
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description('This test try to create user with existing email')
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description('This test try to create user with invalid email')
    def test_create_user_with_invalid_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    @allure.description('This test try to create user with one symbol name')
    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data()
        data['username'] = 'a'
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Unexpected response content {response.content}"

    @allure.description('This test try to create user with very long name')
    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data()
        data[
            'username'] = 'ThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongNameThisIsVeryFuckingLongName'
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"

    @allure.description('This test try to create user with one empty field')
    @pytest.mark.parametrize("data", data_with_one_empty_param)
    def test_create_user_with_empty_fields(self, data):
        data, empty_param = data
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {empty_param}", f"Unexpected response content {response.content}"
