# Depopwatch
[![PyPI version](https://badge.fury.io/py/depopwatch.svg)](https://badge.fury.io/py/depopwatch)
[![Build Status](https://travis-ci.org/WilliamWCYoung/depopwatch.svg?branch=master)](https://travis-ci.org/WilliamWCYoung/depopwatch)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/WilliamWCYoung/depopwatch/master/LICENSE.txt)

## Introduction

Depopwatch is a very simple module to watch Depop accounts for new listings.

This module was created as an alarm for foreign listings, due to activity only occurring in the early hours of the morning locally. There were no alternatives so Depopwatch was made.

## Installation

Installing is as easy as ``` pip install depopwatch ```

## Examples

To create a listener, first import the class

``` 
from depopwatch import Listener
```

Initalize it with a username

```
my_listener = Listener("examplename")
```

And sporadically check for new listings

```
my_listener.search_account()
```

This will return an array populated with the item urls of new listings

## Final
I've included the script I use in ```./examples/pushover_example```. It uses [Pushover](https://github.com/Thibauth/python-pushover) to send a notification to a device alerting to any new listing.
