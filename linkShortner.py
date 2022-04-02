import pyshorteners

link = input("\nEnter your link: ")

shorten_link = pyshorteners.Shortener().tinyurl.short(link)

print(f"\nShortened link: {shorten_link}")