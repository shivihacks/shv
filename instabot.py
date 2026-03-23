from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random

# --- CONFIGURATION ---
INSTA_USERNAME = "nxtsurajtomar"
INSTA_PASSWORD = "shiva8439"
REEL_URL = "https://www.instagram.com/reel/DWMYgKfDGuG/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ=="
COMMENTS = ["Cool reel!", "🔥 Amazing content", "Love this!", "Great work! 🙌"]

def bot_comment():
    # Browser setup
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Bina window khole chalane ke liye ise uncomment karein
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 1. Login Process
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        
        print("[*] Logging in...")
        driver.find_element(By.NAME, "username").send_keys(INSTA_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(INSTA_PASSWORD)
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(6)

        # 2. Go to Reel
        print(f"[*] Navigating to Reel: {REEL_URL}")
        driver.get(REEL_URL)
        time.sleep(5)

        # 3. Post Comment
        comment_area = driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']")
        comment_area.click()
        time.sleep(2)
        
        # Random comment select karna
        selected_comment = random.choice(COMMENTS)
        
        # Typing effect (asli insaan jaisa dikhne ke liye)
        for char in selected_comment:
            comment_area.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
            
        comment_area.send_keys(Keys.ENTER)
        print(f"[✔] Comment Posted: {selected_comment}")
        time.sleep(5)

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    bot_comment()
