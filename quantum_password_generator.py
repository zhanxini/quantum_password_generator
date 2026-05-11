import secrets
import urllib.request

# URL for EFF's Long Wordlist
 url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"

# Download and parse the wordlist
 with urllib.request.urlopen(url) as response:
     content = response.read().decode('utf-8')
    # Each line is: "11111 word" -> we only want the word
    words = [line.split()[1] for line in content.strip().split('\n')]

# Securely generate a 10-word phrase
passphrase = " ".join(secrets.choice(words) for _ in range(10))

print(f"Your Secure Phrase: {passphrase}")
