from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.avito.ru/all/predlozheniya_uslug/obuchenie_kursy-ASgBAgICAUSYC7afAQ?cd=1&q=python&p={}"

def get_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def main():
    driver = get_driver()
    ad_counter = 0
    search_word = "добрый"

    with open(f"./result_{search_word}.txt", "w", encoding="utf-8") as f:
        for page in range(1, 1001):
            print(f"\n=== Страница {page} ===")
            url = BASE_URL.format(page)
            driver.get(url)

            try:
                WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-marker="item"]'))
                )
            except:
                print("Объявления не загрузились")
                continue

            ads = driver.find_elements(By.CSS_SELECTOR, 'div[data-marker="item"]')
            print(f"Нашёл {len(ads)} объявлений на странице")

            msg = ''
            for ad in ads:
                ad_counter += 1
                try:
                    title_el = ad.find_element(By.CSS_SELECTOR, 'a[data-marker="item-title"]')
                    link = title_el.get_attribute("href")

                    try:
                        desc_el = ad.find_element(By.CSS_SELECTOR, 'div.iva-item-bottomBlock-VewGa p')
                        desc = desc_el.text.lower()
                    except:
                        desc = ""

                    if search_word in desc:
                        msg = f'{ad_counter}) слово "{search_word}" найдено в {link} . А описание было: {desc}'
                        print(msg)
                    else:
                        print(f'{ad_counter}) слово "{search_word}" НЕ найдено. А описание было: {desc}')

                except Exception as e:
                    print(f'{ad_counter}) Не удалось получить информацию для объявления: {e}')
                
                f.write("\n" + msg + "\n")
                f.flush()

    driver.quit()
    print("\nПарсинг завершён. Результаты в result.txt")

if __name__ == "__main__":
    main()
