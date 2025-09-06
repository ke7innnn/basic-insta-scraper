from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome()

profiles_toscrape = ["sydney_sweeney","cristiano","ishowspeed","ke7innn"]

USERNAME = "worldisyo7rs"
PASSWORD = "nivek659"


driver.get("https://www.instagram.com/accounts/login/?hl=en")
driver.implicitly_wait(10)

username = driver.find_element("xpath","//input[@aria-label='Phone number, username, or email']")
password = driver.find_element("xpath","//input[@type='password']")


username.send_keys(USERNAME)
password.send_keys(PASSWORD)

submit = driver.find_element("xpath","//button[@type='submit']")
submit.click()
time.sleep(7)
data = []

try:
    for profiles in profiles_toscrape:
        driver.get(f"https://www.instagram.com/{profiles}")
        time.sleep(4)

        try:
            bio_element = driver.find_element(
                "xpath", "//span[contains(@class, '_ap3a') and contains(@class, '_aaco')]"
            )
            bio = bio_element.text
        except:
            bio = "No Bio"
        try:
            stats = driver.find_elements("xpath", "//ul//li//span")
            posts = stats[0].text if len(stats) > 0 else "N/A"
            followers = stats[1].text if len(stats) > 1 else "N/A"
            following = stats[2].text if len(stats) > 2 else "N/A"
        except:
            posts, followers, following = "N/A", "N/A", "N/A"


        try:
            pfp = driver.find_element("xpath","//img[contains(@alt,'profile picture')]")
            pfp_url = pfp.get_attribute("src")
        except:
            fp_url = "No pfp"

        info = {
            "Name": profiles ,
            "Bio": bio,
            "Posts": posts,
            "Followers": followers,
            "Following": following,
            "Profile_Picture": pfp_url,
        }
        data.append(info)
except:
    data.append({
            "Name": profiles,
            "Bio": "Error",
            "Posts": "N/A",
            "Followers": "N/A",
            "Following": "N/A",
            "Profile_Picture": "N/A",
            
        })

df = pd.DataFrame(data)
df.to_csv("bios.csv",index=False)


driver.quit()




