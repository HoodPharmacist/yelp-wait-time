# yelp-wait-times


This Flask app utilizes Selenium to scrape restaurant names and wait times within your bookmarks from Yelp and display it in an organized table. The app includes functionality to log in to Yelp, navigate to the user's bookmarks, retrieve links to bookmarked restaurants, and extract restaurant names and wait times.

## Prerequisites

Before running this app, ensure that you have the following installed:

- Python (version 3.x)
- Selenium (`pip install selenium`)
- ChromeDriver

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:


  ```bash
   cd your-repository
   ```   

3.  Install the required Python packages:

```bash
pip install -r requirements.txt
```
   
## Configuration

Before running the app, you need to configure your Yelp login credentials. Open the app.py file and find the yelp_login function. Replace the email and password parameters with your Yelp account email and password:

```bash
def yelp_login(email, password):
    # ...
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/form/input[2]").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/form/input[3]").send_keys(password)
    # ...

```
## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue in this repository.
