import yt_dlp
import os
import sys
import time

def typing_effect(text, color="\033[1;32m"):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print("\033[0m")

def download_video(link):
    # Download options: Best quality video + audio
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s', # Video ka naam title ke hisab se save hoga
        'quiet': False,
        'no_warnings': True,
    }

    try:
        typing_effect(f"[*] Analyzing link: {link}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        typing_effect("\n[+] Success! Video downloaded in current folder.", "\033[1;34m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: Download fail ho gaya. Link check karein ya library update karein.\033[0m")
        print(f"Details: {e}")

def main():
    os.system('clear')
    print("\033[1;35m")
    print(" 📥 SHV UNIVERSAL VIDEO DOWNLOADER")
    print(" ═" * 35)
    print("\033[1;37m Support: Instagram, YouTube, Facebook & more\033[0m\n")

    while True:
        url = input("\033[1;32mPaste Link (or type 'exit'): \033[0m").strip()
        
        if url.lower() == 'exit':
            print("Closing downloader...")
            break
        
        if not url:
            continue

        download_video(url)
        print("\n" + "─"*40 + "\n")

if __name__ == "__main__":
    main()
