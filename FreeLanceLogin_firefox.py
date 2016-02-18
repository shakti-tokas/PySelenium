
from selenium import webdriver

# create new firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.freelancer.in/")

login_butt = driver.find_element_by_link_text("Log In")
login_butt.click()

driver.implicitly_wait(10)

user_field = driver.find_element_by_class_name("username")
pwd_field = driver.find_element_by_class_name("password")
log_butn = driver.find_element_by_id("login-bt")

user_field.send_keys("rajivkapadia504")
pwd_field.send_keys("poppy123$")
log_butn.click()

driver.implicitly_wait(30)

fig = driver.find_element_by_id("profile-figure")
fig.click()

uname = driver.find_element_by_class_name("user-sidebar-name")

print(uname.text)

driver.quit()
