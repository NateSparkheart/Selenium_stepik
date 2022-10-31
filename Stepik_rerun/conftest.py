import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print('\nЗапускаем хромированного для теста...')
    browser = webdriver.Chrome()
    yield browser
    print('\nЗакрываем браузер')
    browser.quit()


@pytest.fixture(autouse=True, scope='session')
def plus_moral():
    yield plus_moral
    print('\nFriendly reminder that ur a Legend!')