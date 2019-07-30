# Dead Link Spider

A tool written in python with the scrap module to find dead (and cold) links on wiki pages.

The script goes through each page of a wiki and remembers the page and the links on it.
It then visits every link once and checks if the link is dead or cold.
This will be done by human interaction (simple yes-no interface).
After that the human operator goes through each link and finds a suitable replacement for that link. The link is entered into an interface, the script remembers it. After that the script goes through each page of the wiki it visited which contains dead links (which have at least one new link waiting) and proposes the new links. The human operator then again decides which dead link gets replaced with the new link. The tool should also have hotkeys and the ability to copy to clipboard.

## Contents
* [Getting Started](#getting-started)
*    [Prerequisites](#prerequisites)
*    [Installing](#installing)
* [Built With](#built-with)
* [Contributing](#contributing)
*    [Roadmap](#roadmap)
* [Versioning](#versioning)
* [Authors](#authors)
* [License](#license)
* [Acknowledgments](#acknowledgments)
*    [Project History](#project-history)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

I recommend you to use the `setup_development.sh` script by running

```
./setup_development.sh
```

but if you don't want to do that, here is the complete list of dependencies:

* [Python 3](https://www.python.org/downloads/)
* [Scrapy](https://scrapy.org/)

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Built With

* [Sublime Text 3](https://www.sublimetext.com/) - The code editor I use
* [Python 3](https://www.sublimetext.com/) - For running the dev web server
* [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) - The web browser I use

## Contributing

### Roadmap
Things I already plan to implement, but didn't have yet:
- [ ] Make the spider
- [ ] Parse HTML data
- [ ] Have an in-script browser
- [ ] Hotkeys
- [ ] Copy to clipboard
- [ ] Edit text using regexes
- [ ] Save the new links in a data structure
- [ ] Automatically backup the changed page

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Max Fuxjäger** - *Initial work* - [MaxValue](https://github.com/MaxValue)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

* **Chris Angelico** - *Granting me wiki editing rights*

### Project History
This project was created because I (Max) saw that the links on the Python wiki often lead nowhere.
This was because nobody up until then kept the links up to date and because of code hosting sites
like code.google.com or sourceforge growing out of fashion.
But the wiki is massive! This would take forever. So better build a database.
