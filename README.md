# 🎵Billboard-to-Spotify-Playlist-Creator

Create Spotify playlists featuring the top 100 Billboard songs from any specific date! This Python-based project combines web scraping and the Spotify API to take you on a musical journey through time. 🎶

## 📌 Features

- Fetches the Top 100 Billboard songs for a given date.
- Creates a Spotify playlist automatically with these songs.
- Integrates seamlessly with your Spotify account.
- Demonstrates skills in web scraping, API integration, and Python scripting.

 ## 🚀 How It Works

 - Enter a date (e.g., YYYY-MM-DD) to “time travel” to the Billboard charts for that day.
 - The program scrapes song titles from the Billboard website.
 - It searches Spotify for each song and collects their URIs.
 - Finally, it creates a Spotify playlist and adds the songs to it.

 ## 🛠️ Technologies Used

 - Python: For scripting.
 - BeautifulSoup4: For web scraping.
 - Requests: To interact with the Billboard website.
 - Spotipy: For Spotify API integration.
 - Dotenv: To manage sensitive environment variables.

 ## 📋 Prerequisites

- A Spotify Developer Account to obtain your API credentials.
- Python installed on your system.

 ## 🔧 Setup Instructions

- Clone the Repository:
```
 git clone https://github.com/yourusername/billboard-to-spotify.git
 cd billboard-to-spotify
```
- Install Dependencies:
```
 pip install -r requirements.txt
```
- Set Up Environment Variables:
  Create a .env file in the project directory and add the following:
```
SPOTIFY_CLIENT_ID=<your_client_id>
SPOTIFY_SECRET_KEY=<your_secret_key>
SPOTIFY_REDIRECT_URI=<your_redirect_uri>
SPOTIFY_USER_NAME=<your_spotify_username>
```

- Run the Script:
```
 python main.py
```

##  🎉 Demo

[Demonstration](https://drive.google.com/file/d/1Mrig62-L1NS5-hC5iPTMMXMlalTDA4Y-/view?usp=sharing)

## 📝 Project Structure
```
📦 billboard-to-spotify
├── main.py           # Main script for the project
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
├── README.md            # Project documentation
```

## 🚀 Future Enhancements

- Add a web interface using Flask or FastAPI for easier usage.
- Include support for fetching other chart categories (e.g., top albums or genres).
- Deploy on Docker for portability.
- Generate a playlist for a range of dates.

 
