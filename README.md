# _Where to?!_

This repository contains a fully tested and easily extendable app that for a given list of
_users_ and _venues_ answers the age-old question _"Where to so that everyone is happy?!"_.


## Required Inputs and Their Formats


Both users and venues are expected to be contained in plain text files containing JSON data.
It is sufficient to pass the name of the respective files to the app.

### Users

The users file is expected to consist of a list of dictionaries, each describing a user.

A very simple example of a users file might look as follows
```
[
    {
        "name": "John Davis",
        "wont_eat": ["Fish"],
        "drinks": ["Cider", "Rum", "Soft drinks"]
    }
]
```

Here, for the user dictionary, the
 - ``name`` key contains the name of the user,
 - ``wont_eat`` key lists the food that the user is _not willing_ to eat
 - ``drinks`` key lists the drinks that the user _expects_ to find at the venue


### Venues

The venues file is also expected to consist of a list of dictionaries, each describing a venue.

A very simple example of a venues file might look as follows
```
[
    {
        "name": "El Cantina",
        "food": ["Mexican"],
        "drinks": ["Soft drinks", "Tequila", "Beer"]
    }
]
```

Here, for the venue dictionary, the
 - ``name`` key contains the name of the venue,
 - ``food`` key lists the food that is _available_ at the venue
 - ``drinks`` key lists the drinks that are _available_ at the venue


### Assumptions

The single assumption made in the input data is that _venue names are unique_.
There are checks for venue name uniqueness in place; a ``DuplicateVenueError`` is raised in case a violation is detected.

The assumption seems to reflect real life as we tend to distinguish venues with identical names by adding the location to the name.
So, if ever in doubt, "Fabrique" turns into "Fabrique, Convent Garden" to ensure that everyone is eventually showing up at the same venue.


## Output

For given input files containing users and venues, the app will print a self-explanatory output similar to the following output

```
Places to go:
 - The Cambridge
 - Spice of life
Places to avoid:
 - El Cantina
     * There is nothing to drink for Robert Webb
     * There is nothing to eat for Bobby Robson
 - Spirit House
     * There is nothing to drink for Alan Allen
 - Sultan Sofrasi
     * There is nothing to drink for Robert Webb
 - Tally Joe
     * There is nothing to drink for Robert Webb
 - Wagamama
     * There is nothing to drink for Robert Webb
 - Twin Dynasty
     * There is nothing to eat for David Lang
 - Fabrique
     * There is nothing to drink for Robert Webb
     * There is nothing to drink for David Lang
```

Here, ``Places to go`` lists the venues where every user is able to find suitable food and drinks.
The ``Places to avoid`` lists the venues where at least one user is not able to find suitable food or drinks; detailed reasoning is provided in the output.


## Running the Tests

Run the tests from the base directory of this project via
```
python -m unittest discover tests/
```

Note that the tests will contain output saying

> usage: just_one.py [-h] --venues VENUES --users USERS

> just_one.py: error: argument --users is required

and

> usage: just_one.py [-h] --venues VENUES --users USERS

>just_one.py: error: argument --venues is required

This is purely logging information and _does not impact the success of the tests_.


## Deciding Where to Go

The main program `just_one.py` can be run with the sample inputs provided in `input/` via
```
python just_one.py --users input/users.json --venues input/venues.json
```

Note that logging is _turned on_ by default.


## FAQs

This section lists frequently asked questions and tries to provide an answer.

### What's with the Name?

_Where to?!_ is the question that the app answers, so it seemed like a good fit.

As for ``just_one.py`` in order to run the app — we used to go for 'just one' on Fridays, but it hardly ever ended up being 'just one'...

### Why is the logging so verbose?

Imagine the _Where to?!_ app crashing in production with nothing more than a stack trace and the logs to debug.
That's usually where detailed logging pays off from my experience.

### What's the testing strategy?

The main idea is to test _end-to-end on the functionality guaranteed_ -- and not the implementation. This is the reasons why most modules in ``where_to`` are not explicitly tested. The functionality of the individual modules is heavily used but can easily be swapped out with something that achieves the same goals via different means.

The tests verify that:

1. The expected arguments are ``users`` and ``venues``
2. Passing a list of venues where two venues have the same name results in a ``DuplicateVenueError``
3. For a set of test cases, when passing in ``users.json`` and ``venues.json`` files, the expected output is as contained in the corresponding ``expected_output.txt``. For sake of readability, each test case is stored in a separate sub-directory.


## Potential Improvements

The performance of the algorithm which decides where to go can be improved.
The current iteration is very meticulous and is able to answer a broader range of questions than what is actually required by the final output.

While the algorithm internally computes all options for food and drinks for every user at each venue, the final output only focuses on the mere _existence_ of food and drink options.
A simple improvement would be to stop at the first available option of food and drinks for every user at each venue as any further options do not impact the final result.

Given food options and aversions are sets, then the algorithm can be improved by making use of the pigeonhole principle; if there are more food options than aversions, then there's a food option available.
Unfortunately, the same argument does not hold for drinks as the two lists may not share any commonalities.
In case there are as many aversions as there are food options, an element-wise comparision is again required.


## Miscellaneous

The _Where to?!_ app only requires a working Python 2.7 installation.

The documentation was written in Markdown and can be compiled via [`grip`](https://github.com/joeyespo/grip) if necessary.

Made on a Mac using PyCharm and two cups of coffee.
