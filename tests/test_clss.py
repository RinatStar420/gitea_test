import time
import requests
import random
import string
from selenium import webdriver



def randomStringDigits(stringLength=6):
    symbols = string.ascii_letters + string.digits
    while True:
        random_string = ''.join(random.choice(symbols) for i in range(stringLength))
        if (any(c.islower() for c in random_string)
                and any(c.isupper() for c in random_string)
                and sum(c.isdigit() for c in random_string) >= 3):
            break
    return random_string


chrome_driver = './chromedriver'  # TODO ссылка на драйвер
register_url = "http://localhost:3000/user/sign_up"
login_url = "http://localhost:3000/user/login?redirect_to=%2f"
test_user_name = randomStringDigits(8)
test_email = randomStringDigits(8) + '@mail.ru'
test_password = randomStringDigits(8)
repository = 'my_repository'


class ClassTest:

    def request_200(cls):
        cls.r = requests.get('http://localhost:3000')
        return cls.r.status_code

    def test_request(self):
        assert self.request_200() == 200

    def test_register(self):



        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.get(register_url)

        if "Регистрация" in self.driver.title:
            assert True
            user_name = self.driver.find_element_by_xpath('//*[@id="user_name"]')
            user_name.send_keys(test_user_name)

            email = self.driver.find_element_by_xpath('//*[@id="email"]')
            email.send_keys(test_email)

            password = self.driver.find_element_by_xpath('//*[@id="password"]')
            password.send_keys(test_password)

            repeat_password = self.driver.find_element_by_xpath('//*[@id="retype"]')
            repeat_password.send_keys(test_password)

            button = self.driver.find_element_by_xpath("//button [@class='ui green button']")
            time.sleep(2)
            button.click()

        else:
            print(f'для регистрации нового пользователя перейдите на страницу {register_url}')
            assert False

        time.sleep(2)

    def login_gitea(self):

        self.driver.get(login_url)
        if "Gitea: Git with a cup of tea" in self.driver.title:
            assert True
            user_name = self.driver.find_element_by_xpath('//*[@id="user_name"]')
            user_name.send_keys(test_user_name)

            password = self.driver.find_element_by_xpath('//*[@id="password"]')
            password.send_keys(test_password)

            button = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/form/div[4]/button')
            button.click()
        else:
            print(f'для входа нового пользователя перейдите на страницу {login_url}')
            assert False

        time.sleep(2)

    def create_repo(self):

        go_to_create_repo = self.driver.find_element_by_xpath('//*[@id="dashboard-repo-list"]/div/div[2]/h4/a')
        go_to_create_repo.click()

        name_repo = self.driver.find_element_by_xpath('//*[@id="repo_name"]')
        name_repo.send_keys(repository)

        description = self.driver.find_element_by_xpath('//*[@id="description"]')
        description.send_keys('Тут должно быть описание репозитория')

        auto_drop = self.driver.find_element(by='id', value='auto-init')
        auto_drop.click()

        button = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div/div[8]/button')
        time.sleep(2)
        button.click()



    def add_new_file(self):

        add_new_file = self.driver.find_element_by_xpath('//*[@id="file-buttons"]/div/a[1]')
        add_new_file.click()

        file_name = 'new_file'
        name_new_file = self.driver.find_element_by_xpath('//*[@id="file-name"]')
        name_new_file.send_keys(file_name)

        text_for_new_file = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/form/div[2]/div[2]/div/div/div[1]/textarea')
        text_for_new_file.send_keys('Это именно мой коммит')

        button_for_create_new_file = self.driver.find_element_by_xpath('//*[@id="commit-button"]')
        time.sleep(2)
        button_for_create_new_file.click()



    def chek_commit(self):
        check_commit = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[4]/div/div/div[1]/a')
        time.sleep(2)
        check_commit.click()

        open_commit = self.driver.find_element_by_xpath('//*[@id="commits-table"]/tbody/tr[1]/td[2]/a')
        open_commit.click()

        time.sleep(3)
        self.driver.close()


test = ClassTest()

test.test_request()
test.test_register()
# test.login_gitea()
test.create_repo()
test.add_new_file()
test.chek_commit()
