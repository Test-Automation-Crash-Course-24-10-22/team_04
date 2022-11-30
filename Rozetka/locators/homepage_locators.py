from selenium.webdriver.common.by import By


class HomePageLocators:

    searching_field = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div[1]/input')
    searching_button = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button')
    auth_button = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user')
    from_UA_to_RU = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[1]/rz-lang/ul/li[1]')
    logout_button = (By.XPATH, '/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[2]/ul/li[14]')
    basket_button = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[7]/rz-cart')
    open_menu = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/rz-mobile-user-menu')
