import time

# Ensure you've installed the 'webdriver_manager' package
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

# URL of WhatsApp Web
whatsapp_url = "https://web.whatsapp.com/"

# Number you want to send the message to (include country code)
recipient_number = "+919656778508"

# Message you want to send
message = "Hello there! This message is sent using Python automation. 🐍"

# Initialize the WebDriver
driver = Chrome(ChromeDriverManager().install())  # This will automatically manage the Chrome WebDriver

# Open WhatsApp Web
driver.get(whatsapp_url)

# Wait for the user to scan the QR code and log in
input("Press enter after scanning QR code and logging in...")

# Locate the search input box to search for the recipient number
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')

# Type the recipient's number
search_box.send_keys(recipient_number)
time.sleep(2)  # Let search results load

# Press Enter to search for the number
search_box.send_keys("\n")

# Wait for a bit for the chat to load
time.sleep(2)

# Find the chat input box
chat_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

# Type the message
chat_box.send_keys(message)

# Simulate pressing Enter to send the message
chat_box.send_keys("\n")

# Wait for a bit before closing the browser
time.sleep(5)

# Close the browser
driver.quit()
