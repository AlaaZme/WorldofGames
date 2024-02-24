from selenium import webdriver
from time import sleep

res = "Fail"
try_times=0

while "Fail" in res:
    try_times +=1
    dr2 = webdriver.Chrome()
    #dr = webdriver.Edge()
    dr2.get("http://localhost:81")
    dr2.find_element(by="xpath" , value="//*[@id=\"name\"]/option[1]").click()
    dr2.find_element(by="id" , value="diff").send_keys("4")
    dr2.find_element(by="xpath", value="//*[@id=\"home\"]/form[1]/button").click()

    dr2.find_element(by="id",value="Guess").send_keys('3')
    dr2.find_element(by="xpath",value="//*[@id=\"GuessGame\"]/form/button").click()
    res = dr2.find_element(by="xpath",value="//*[@id=\"container\"]/h2[3]").get_attribute("innerHTML")
    if "Fail" not in res:
        dr2.find_element(by="xpath",value="// *[ @ id = \"container\"] / form[2] / button").click()
        sleep(5)
print(f"GussGame:  {res}   try times:{try_times}")
res = "Fail"
try_times=0
'''

while "Fail" in res:
    try_times +=1
    dr = webdriver.Chrome()
    #dr = webdriver.Edge()
    dr.get("http://localhost:81")
    dr.find_element(by="xpath" , value="//*[@id=\"name\"]/option[2]").click()
    dr.find_element(by="id" , value="diff").send_keys("1")
    dr.find_element(by="xpath",value="//*[@id=\"home\"]/form[2]/button").click()
    dr.find_element(by="xpath",value="//*[@id=\"Guess How much in ILS\"]").send_keys('200')
    dr.find_element(by="xpath",value="//*[@id=\"Currency Game\"]/form/a/button").click()
    res = dr.find_element(by="xpath",value="//*[@id=\"container\"]/h3[3]").get_attribute("innerHTML")
print(f"Currency Game: {res}   try times:{try_times}")

'''