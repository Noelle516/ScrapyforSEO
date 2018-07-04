# Scrapy for SEO

This is a Scrapy project to scrape websites and seperate them by tags. The spider in this project requires a user input in the command prompt. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

These must be installed before starting:

* [Python](https://www.python.org/downloads/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/)


### Installing Scrapy

A step by step series of examples that tell you how to get a virtualenv running

1. Open the Anaconda Prompt (can be found by looking up Anaconda in Start Menu)
2. Create a virtualenv
```
conda create -n yourenvname python=x.x anaconda
```
3. Install Scrapy (conda-forge is the channel)
```
conda install -n yourenvname -c conda-forge scrapy
```


## Running the Spider

You can run the spider using the scrapy crawl command:
```
scrapy crawl user
```
**Make sure to use the command prompt, activate your virtualenv, and choose the correct directory**

## Authors

* **Noelle Rivera** - *Initial work* - [NoelleRivera516](https://github.com/Noelle516)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## References
For more information: [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
