def a(self,driver):
    # resourceId 方式
    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")')
    # text 方式
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")')
    # description 方式
    self.driver.find_element_by_android_uiautomator('new UiSelector().description("%s")')
    # className 方式
    self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")')
    # index 方式
    self.driver.find_element_by_android_uiautomator('new UiSelector().index("%s")')
    # className + index 方式
    self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s").childSelector(new UiSelector().index("%d"))')
    # 伪xpath方法定位
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("Custom View").fromParent(new UiSelector().text("Accessibility Service"))').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().text("Custom View"))').click()