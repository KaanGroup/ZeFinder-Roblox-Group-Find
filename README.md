# Ze-Scraper

Ze-Scraper is a powerful Roblox group finder that performs around 500,000 checks per minute, utilizing free Tor proxies & Account Cookies to bypass Roblox's APIs Ratelimits.  

![Image of the script running](https://i.imgur.com/JI0caCj.png)

## How to Use

### Setup

1. **Prepare Roblox Accounts:**
   - Create 3-4 new empty Roblox accounts.
   - Add the cookies for these accounts into the `new_cookies.txt` file.

2. **Configure Webhook & Discord User ID:**
   - Add your Discord webhook URL and Discord User ID to the `config.json` file.

### Running

1. **Install Python:**
   - Visit [Python.org](https://www.python.org/downloads/) and download the latest release.

2. **Install Libraries:**
   - Run the following command to install the required libraries:
     ```bash
     python -m pip install aiohttp asyncio
     ```

3. **Start the Scraper:**
   - Run the script with the following command:
     ```bash
     python main.py
     ```

### Support

- If you encounter any issues, contact **``@Bueezi``** on Discord.

---

## License

**Proprietary License**

Copyright 2024 Bueezi™. All Rights Reserved.

This software is licensed under the Proprietary License. Unauthorized copying, modification, distribution, or use of this software is strictly prohibited. For full license details, see the `LICENSE` file in this repository.
