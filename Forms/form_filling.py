import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class Form:

    def browser_opener(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.f = open("demo_file1.txt", "a")
        self.f.write("\n=====================================")
        self.f.write("\nOpening browser")
        url = "https://demo.anhtester.com/basic-first-form-demo.html"
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            self.driver.find_element(By.CLASS_NAME, "at-cm-no-button").click()
            print("Clicked on No")
            self.f.write("\nClicked on No")
        except:
            self.f.write("\nSkipping")
            print("Skipping...")

        self.driver.implicitly_wait(5)

    def browser_close(self):
        time.sleep(2)
        self.f.write("\n=====================================")
        self.f.write("\nClosing the browser")
        self.f.close()
        # self.f.write("Quiting the browser")
        self.driver.quit()

    def waiting(self, locator, element):
        self.f.write("\n=====================================")
        self.f.write("\nWaiting for element...")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((locator, element)))

    def input_form(self):
        self.driver.find_element(By.ID, "user-message").send_keys("Hello")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Show Message')]").click()
        msg = self.driver.find_element(By.ID, "display")
        print("Your Message: " + msg.text)
        self.f.write("\n=====================================")
        self.f.write("\nYour Message: " + msg.text)

        self.driver.find_element(By.ID, "sum1").send_keys("45")
        self.driver.find_element(By.ID, "sum2").send_keys("34")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Get Total')]").click()
        total = self.driver.find_element(By.ID, "displayvalue")
        print("Sum: " + str(total.text))
        self.f.write("\n=====================================")
        self.f.write("\nSum: " + str(total.text))

    def checkboxes(self):
        self.driver.find_element(By.LINK_TEXT, "Input Forms").click()
        self.driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()
        # self.check1 = self.driver.find_element(By.ID, "isAgeSelected")

        # Find all the checkboxes of a page & check it if not already checked
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        self.f.write("\n=====================================")
        self.f.write("\nChecking the checkboxes")
        for c in checkboxes:
            if c.is_selected() == False:
                c.click()
            else:
                continue

    def radio_buttons(self):
        self.driver.find_element(By.LINK_TEXT, "Input Forms").click()
        self.driver.find_element(By.LINK_TEXT, "Radio Buttons Demo").click()
        # Find all the radio buttons in the page
        all_radio_buttons = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
        # print(all_radio_buttons)
        self.f.write("\n=====================================")
        for btn in all_radio_buttons:
            print(btn.get_attribute("value"))  # Get the value of each buttons
            print("Before Selection: ")
            print(btn.is_selected())  # Check if radio button is selected or not
            btn.click()  # Select the radio button
            self.f.write("\nRadio selected: " + btn.get_attribute("value"))
            print("After Selection: ")
            print(btn.is_selected())

    def drop_down(self):
        self.driver.find_element(By.LINK_TEXT, "Input Forms").click()
        self.driver.find_element(By.LINK_TEXT, "Select Dropdown List").click()

        # Find all the dropdown of a specific section
        options = self.driver.find_elements(By.ID, "select-demo")
        # for option in options:
        #     print(option.text.strip())
        # time.sleep(2)
        # Select option
        self.f.write("\n=====================================")
        options = self.driver.find_element(By.ID, "select-demo")
        sel = Select(options)
        # sel.select_by_value("Sunday")
        # sel.select_by_index(2)
        sel.select_by_visible_text("Tuesday")
        self.f.write("\nDropdown Options: " + options.text)

    def multi_select(self):
        self.driver.find_element(By.LINK_TEXT, "Input Forms").click()
        self.driver.find_element(By.LINK_TEXT, "Select Dropdown List").click()

        # Find all the dropdown of a specific section
        options = self.driver.find_elements(By.ID, "multi-select")
        # for option in options:
        #     print(option.text)
        # Select an option
        options = self.driver.find_element(By.ID, "multi-select")
        time.sleep(2)
        sel = Select(options)
        # sel.select_by_visible_text("Ohio")
        # sel.select_by_value("Pennsylvania")
        self.f.write("\n=====================================")

        sel.select_by_index(1)
        self.driver.find_element(By.ID, "printMe").click()
        wait = WebDriverWait(self.driver, 10)
        elem = self.driver.find_element(By.CLASS_NAME, "getall-selected")
        EC.visibility_of(elem)
        print(elem.text)
        self.f.write("\nMultiselect: " + elem.text)

    def form_submit(self):
        self.f.write("\n=====================================")
        self.f.write("\nForm Submitting")
        self.driver.find_element(By.LINK_TEXT, "Input Forms").click()
        self.driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        self.driver.find_element(By.NAME, "first_name").send_keys("First")
        self.driver.find_element(By.NAME, "last_name").send_keys("Last")
        self.driver.find_element(By.NAME, "email").send_keys("fl@mail.com")
        self.driver.find_element(By.NAME, "phone").send_keys("(123)456-7890")
        self.driver.find_element(By.NAME, "address").send_keys("421 Bay Street")
        self.driver.find_element(By.NAME, "city").send_keys("Sault ")
        options = self.driver.find_element(By.NAME, "state")
        sel = Select(options)
        sel.select_by_index(5)
        self.driver.find_element(By.NAME, "zip").send_keys("12334-9827")
        self.driver.find_element(By.NAME, "website").send_keys("https://demo.anhtester.com/")
        self.driver.find_element(By.XPATH, '//input[@type="radio" and @value="no"]').click()
        self.driver.find_element(By.NAME, "comment").send_keys("Testing!!!")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()

    def loading_on_submission(self):
        self.f.write("\n=====================================")
        self.driver.find_element(By.LINK_TEXT, "Input Forms").click()
        self.driver.find_element(By.LINK_TEXT, "Ajax Form Submit").click()
        self.driver.find_element(By.ID, "title").send_keys("First Last")
        self.driver.find_element(By.ID, "description").send_keys("Description")
        self.driver.find_element(By.ID, "btn-submit").click()
        wait = WebDriverWait(self.driver, 10)
        load = self.driver.find_element(By.ID, "submit-control")
        EC.visibility_of(load)
        print(load.text)
        self.f.write("\nLoading Text: " + load.text)
        time.sleep(2)

    def date_picker(self):
        self.f.write("\n=====================================")
        self.driver.find_element(By.LINK_TEXT, "Date pickers").click()
        self.driver.find_element(By.LINK_TEXT, "Bootstrap Date Picker").click()
        date_pick = "04/05/2022"
        self.driver.find_element(By.XPATH, "//input[@placeholder='dd/mm/yyyy']").send_keys(date_pick)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Start date']").send_keys(date_pick)
        s = self.driver.find_element(By.XPATH, "//input[@placeholder='End date']").send_keys()
        self.f.write("\nDate: " + date_pick)

    def jquery_date_picker(self):
        self.f.write("\n=====================================")
        self.f.write("\nJquery Date Picker")
        self.driver.find_element(By.LINK_TEXT, "Date pickers").click()
        self.driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
        self.driver.find_element(By.ID, "from").send_keys("07/01/2022")
        self.driver.find_element(By.ID, "to").send_keys("07/05/2022")

    def pagination(self):
        self.f.write("\n=====================================")
        self.driver.find_element(By.LINK_TEXT, "Table").click()
        self.driver.find_element(By.LINK_TEXT, "Table Pagination").click()
        options = self.driver.find_elements(By.ID, "myPager")
        for option in options:
            option.click()
            print("Clicked on: " + option.text)
            self.f.write("\nClicked on: " + option.text)

    def table_data_search(self):
        self.f.write("\n=====================================")
        self.driver.find_element(By.LINK_TEXT, "Table").click()
        self.driver.find_element(By.LINK_TEXT, "Table Data Search").click()
        # search = self.driver.find_element(By.ID, "task-table-filter")
        # search.send_keys("Br")
        # res = self.driver.find_elements(By.XPATH, "//*[@id='task-table']/tbody")
        # for r in res:
        #     print(r.text)
        self.driver.find_element(By.CSS_SELECTOR, "span[class='glyphicon glyphicon-filter']").click()
        num = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='#']")
        username = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
        first_name = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
        last_name = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
        last_name.send_keys("k")
        elements = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/table/tbody")
        print("N Uname FName LName")
        for element in elements:
            print(element.text)
            self.f.write("\nRes: " + element.text)

    def table_filter(self):
        self.f.write("\n=====================================")
        self.f.write("\nTable Filter")
        wait = WebDriverWait(self.driver, 10)
        table = self.driver.find_element(By.LINK_TEXT, "Table")
        EC.visibility_of_element_located(table)
        table.click()
        table_filter = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Table Filter")
        EC.visibility_of_element_located(table_filter)
        table_filter.click()

    def table_sort_search(self):
        self.f.write("\n=====================================")
        self.driver.find_element(By.LINK_TEXT, "Table").click()
        self.driver.find_element(By.LINK_TEXT, "Table Sort & Search").click()
        self.driver.find_element(By.XPATH, "//th[contains(text(),'Position')]").click()
        headers = self.driver.find_elements(By.CSS_SELECTOR, "#example > thead > tr")
        page = self.driver.find_elements(By.XPATH, "//*[@id='example_paginate']/span/a")
        data = self.driver.find_elements(By.XPATH, "//*[@id='example']/tbody")
        nxt = self.driver.find_element(By.XPATH, "//*[@class='paginate_button next']")

        f = open("data.txt", "a")
        for header in headers:
            print(header.text)
            self.f.write("\n" + header.text)

        for i in range(1, 5):
            self.driver.find_element(By.XPATH, "//a[contains(text(),'{}')]".format(i)).click()
            for d in data:
                f.write(d.text)
                # print(d.text)
            f.write("\n--------------------------------------------------------------------")

        f.close()

    def jquery_download_progress(self):
        self.f.write("\n=====================================")
        self.driver.get("https://demo.anhtester.com/jquery-download-progress-bar-demo.html")
        self.driver.find_element(By.ID, "downloadButton").click()
        progress = self.driver.find_element(By.CSS_SELECTOR, ".progress-label")
        print(progress.text)
        self.f.write("\nProgress Text: " + progress.text)
        wait = WebDriverWait(self.driver, 10)
        t = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-label"), "Complete"))
        # assert progress.text == "Complete"
        print(progress.text)
        self.f.write("\nProgress Text: " + progress.text)

    def bootstrap_download_progress(self):
        self.f.write("\n=====================================")
        self.driver.get("https://demo.anhtester.com/bootstrap-download-progress-demo.html")
        self.driver.find_element(By.ID, "cricle-btn").click()
        progress = self.driver.find_element(By.CSS_SELECTOR, ".percenttext")
        print(progress.text)
        self.f.write("\nProgress Text: " + progress.text)
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".percenttext"), "100%"))
        print(progress.text)
        self.f.write("\nProgress Text: " + progress.text)

    def drag_and_drop_sliders(self):
        self.f.write("\n=====================================")
        self.driver.get("https://demo.anhtester.com/drag-drop-range-sliders-demo.html")
        slider1 = self.driver.find_element(By.XPATH, "//*[@id='slider1']/div/input")
        slider2 = self.driver.find_element(By.XPATH, "//*[@id='slider2']/div/input")
        slider3 = self.driver.find_element(By.XPATH, "//*[@id='slider3']/div/input")
        slider4 = self.driver.find_element(By.XPATH, "//*[@id='slider4']/div/input")
        slider5 = self.driver.find_element(By.XPATH, "//*[@id='slider5']/div/input")
        slider6 = self.driver.find_element(By.XPATH, "//*[@id='slider6']/div/input")
        slider_value1 = self.driver.find_element(By.ID, "range")
        slider_value2 = self.driver.find_element(By.ID, "rangePrimary")
        slider_value3 = self.driver.find_element(By.ID, "rangeSuccess")
        slider_value4 = self.driver.find_element(By.ID, "rangeInfo")
        slider_value5 = self.driver.find_element(By.ID, "rangeWarning")
        slider_value6 = self.driver.find_element(By.ID, "rangeDanger")

        print(slider1.get_attribute("value"))
        print(slider_value1.text)
        self.f.write("\nSlider1: " + slider1.get_attribute("value"))
        self.f.write("\nSlider1 Value: " + slider_value1.text)
        action = ActionChains(self.driver)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.text_to_be_present_in_element((By.ID, "range"), "50"))
        action.drag_and_drop_by_offset(slider1, 405.75, 25).perform()
        print(slider1.get_attribute("value"))
        print(slider_value1.text)
        self.f.write("\nSlider1: " + slider1.get_attribute("value"))
        self.f.write("\nSlider1 Value: " + slider_value1.text)

    def bootstrap_alert_autocloseable(self):
        self.f.write("\n=====================================")
        self.driver.get("https://demo.anhtester.com/bootstrap-alert-messages-demo.html")
        locator = By.XPATH
        self.driver.find_element(By.ID, "autoclosable-btn-success").click()
        elm = "/html/body/div[2]/div/div[2]/div/div[2]/div[1]"
        self.waiting(locator, elm)
        m = self.driver.find_element(locator, elm)
        print(m.text)
        self.f.write("\nMessage: " + m.text)

    def bootstrap_alert_normal(self):
        self.f.write("\n=====================================")
        self.driver.get("https://demo.anhtester.com/bootstrap-alert-messages-demo.html")
        self.driver.find_element(By.ID, "normal-btn-success").click()
        time.sleep(2)
        locator = By.XPATH
        element = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]"
        self.waiting(locator, element)
        msg = self.driver.find_element(locator, element)
        print(msg.text)
        self.f.write("\nMessage: " + msg.text)

    def bootstrap_warning_autocloseable(self):
        self.f.write("\n=====================================")
        self.driver.get("https://demo.anhtester.com/bootstrap-alert-messages-demo.html")
        self.driver.find_element(By.ID, "autoclosable-btn-warning").click()
        time.sleep(2)
        locator = By.XPATH
        element = "/html/body/div[2]/div/div[2]/div/div[2]/div[3]"
        self.waiting(locator, element)
        msg = self.driver.find_element(locator, element)
        print(msg.text)
        self.f.write("\nMessage: " + msg.text)

    def window_popup_modal(self):
        self.driver.get("https://demo.anhtester.com/window-popup-modal-demo.html")
        print(self.driver.title)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Follow On Twitter')]").click()
        # self.driver.switch_to.window(0)
        # print(self.driver.title)
        # self.driver.switch_to.default_content()

    def file_upload(self):
        self.driver.get("https://the-internet.herokuapp.com/upload")
        print(self.driver.title)
        self.driver.find_element(By.ID, "file-upload").send_keys("C:/Users/JahidulIslam/PycharmProjects/pythonDemo/data/bird.png")
        self.driver.find_element(By.ID, "file-submit").click()
        success_message = self.driver.find_element(By.XPATH, "//h3[contains(text(),'File Uploaded!')]")
        file_name = self.driver.find_element(By.ID, "uploaded-files")
        print(success_message.text + " with name: " + file_name.text)

time.sleep(2)
