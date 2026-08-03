import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Configuration
USE_SYSTEM_FFMPEG = os.getenv("USE_SYSTEM_FFMPEG", "false").lower() == "true"
BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "downloads"
OUTPUT_DIR.mkdir(exist_ok=True)

YTDLP_COOKIES_BROWSER = os.getenv("YTDLP_COOKIES_BROWSER", "firefox").strip()
YTDLP_COOKIES_PROFILE = os.getenv("YTDLP_COOKIES_PROFILE", "").strip() or None


def get_ffmpeg_path() -> str | None:
    """Get ffmpeg path based on OS configuration."""
    if USE_SYSTEM_FFMPEG:
        return None  # Use system ffmpeg from PATH
    return str(BASE_DIR / "ffmpeg.exe")


def get_cookies_from_browser() -> tuple | None:
    """Get the yt-dlp cookiesfrombrowser spec, or None if disabled."""
    if not YTDLP_COOKIES_BROWSER:
        return None
    return (YTDLP_COOKIES_BROWSER, YTDLP_COOKIES_PROFILE, None, None)
