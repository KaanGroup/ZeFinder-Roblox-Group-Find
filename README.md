# Ze-Finder

Ze-Finder is a powerful Roblox group finder that performs around 500,000 checks per minute, utilizing free Tor proxies & Account Cookies to bypass Roblox's APIs Ratelimits.  

![Image of the script running](https://i.imgur.com/JI0caCj.png)

## Setup

<a href="https://youtu.be/tavy6EUamYk" target="_blank">
  <img src="https://img.youtube.com/vi/tavy6EUamYk/0.jpg" alt="Watch the video" style="width:100%; max-width:600px;">
</a>

1. **Install Python:**
   - Visit [Python.org](https://www.python.org/downloads/) and download the latest release.

2. **Install Libraries:**
   - Run the following command to install the required libraries:
     ```bash
     python -m pip install aiohttp asyncio psutil requests
     ```
3. **Download & Exctract the repository:**
   - [Download this repository](https://github.com/Bueezi/ZeFinder-Roblox-Group-Finder/archive/refs/heads/main.zip) as a zip file & then extract it
4. **Prepare Roblox Accounts:**
   - Create 3-4 new empty Roblox accounts.
   - Add the cookies for these accounts into the `new_cookies.txt` file.

5. **Configure Webhook & Discord User ID:**
   - Add your Discord webhook URL and Discord User ID to the `config.json` file.


6. **Start the Scraper:**
   - Run the script with the following command:
     ```bash
     python -m main.py
     ```

### Support

- If you encounter any issues, contact **``@Bueezi.``** on Discord.

---

## License

**Proprietary License**

Copyright 2024 Bueezi™. All Rights Reserved.

This software is licensed under the Proprietary License. Unauthorized copying, modification, distribution, or use of this software is strictly prohibited. For full license details, see the `LICENSE` file in this repository.
