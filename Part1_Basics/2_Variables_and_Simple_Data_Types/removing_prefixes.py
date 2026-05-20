# Removing prefixes is a common task within strings.

# EX: Say we want to remove the common prefix 'https://'
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)