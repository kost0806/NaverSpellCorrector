from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SpellCorrector(object):
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=2&acq=%EB%A7%9E%EC%B6%A4%EB%B2%95%EA%B2%80%EC%82%AC&qdt=0&ie=utf8&query=%EB%A7%9E%EC%B6%A4%EB%B2%95%EA%B2%80%EC%82%AC%EA%B8%B0')

        self.text_elem = self.driver.find_element_by_css_selector('#grammar_checker > div > div.api_cs_wrap > div.check_box > div.text_box._original > div > div.text_area > textarea')

    def correct(self, s):
        self.text_elem.clear()
        self.text_elem.send_keys(s)
        self.driver.find_element_by_css_selector('#grammar_checker > div > div.api_cs_wrap > div.check_box > div.text_box._original > div > div.check_info > button').click()

        result_found = False
        while not result_found:
            try:
                result = self.driver.find_element_by_css_selector('#grammar_checker > div > div.api_cs_wrap > div.check_box > div.text_box.right._result.result > div > div.text_area > p')
                if result.text == '맞춤법 검사 중입니다. 잠시만 기다려주세요.':
                    continue
                result_found = True
            except Exception:
                result_found = False

        return result

    def __del__(self):
        self.driver.close()


if __name__ == '__main__':
    s = SpellCorrector()
    result = s.correct('본지침은 모든회사의 정보자산에 대하여 적용한다.')
    print(result)
