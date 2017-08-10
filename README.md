# Dead Link Spider
*a tool written in python with the scrap module to find dead (and cold) links on wiki pages*

## Info

The script goes through each page of a wiki and remembers the page and the links on it. It then visits every link once and checks if the link is dead or cold. This will be done by human interaction (simple yes-no interface). After that the human operator goes through each link and finds a suitable replacement for that link. The link is entered into an interface, the script remembers it. After that the script goes through each page of the wiki it visited which contains dead links (which have at least one new link waiting) and proposes the new links. The human operator then again decides which dead link gets replaced with the new link. The tool should also have hotkeys and the ability to copy to clipboard.

## Roadmap

- [ ] Make the spider
- [ ] Parse HTML data
- [ ] Have an in-script browser
- [ ] Hotkeys
- [ ] Copy to clipboard
- [ ] Edit text using regexes
- [ ] Save the new links in a data structure
- [ ] Automatically backup the changed page

## Tools to be used

- Python3
- Python scrapy module
- Python argparse module
- Python re module (maybe the newer regex module)
- Python browser module???
- Python clipboard module???
- Python hotkey module???
