from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class instagram_bot:
    def __init__(self, user, password):
        # Abrir el driver y la pagina que quiero abrir con selenium
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("https://www.instagram.com/")
        self.user = user
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        sleep(2)
        # pongo lo que quiero que el bot haga click con el xpath (copy full xpath)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        # agregar nombre de usuario, password y hacer click en log in
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(5)

    def unfollow(self):

        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.user)).click()
        sleep(1)
        # obtengo la cantidad de following que tengo
        self.nfollowers = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
        self.nfollowing = int(self.driver.find_element_by_xpath("//li[3]/a/span").text)
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        sleep(3)
        following = self._get_names_following()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        sleep(2)
        followers = self._get_names_followers()
        sleep(2)
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names_following(self):
        sleep(2)
        scroll = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
        # scroll

        while self.nfollowing > 0:
            self.driver.execute_script('''
                        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                        fDialog.scrollTop = fDialog.scrollHeight
                    ''')

            sleep(2)

            self.driver.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollBot = fDialog.scrollHeight
                            ''')

            sleep(2)

            self.driver.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                            ''')

            self.nfollowing -= 12

        links = scroll.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg').click()
        return names
    
    def _get_names_followers(self):
        sleep(2)
        scroll = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
        # scroll

        while self.nfollowers > 0:
            self.driver.execute_script('''
                        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                        fDialog.scrollTop = fDialog.scrollHeight
                    ''')

            sleep(2)

            self.driver.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollBot = fDialog.scrollHeight
                            ''')

            sleep(2)

            self.driver.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                            ''')

            self.nfollowers -= 12

        links = scroll.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg').click()
        return names

# Necesito esta funcion para que abra el programa, sino no funciona.
bot = instagram_bot('ENTER YOUR USERNAME', 'ENTER YOUR PASSWORD')
bot.unfollow()