import allure


@allure.title("Get user by ID")
@allure.description("Verify that user is returned successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user(user_service):
    user = user_service.get_user(2)

    assert user.get("data", {}).get("id") == 2


@allure.title("Create new user")
@allure.description("Verify that user is created successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user(user_service):
    user = user_service.create_user("morpheus", "leader")

    assert user.get("name") == "morpheus"
    assert user.get("job") == "leader"
