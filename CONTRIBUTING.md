# Contributing to Python Chain

It's awesome that you want to contribute to this service! You can contribute in several ways, like:

* Creating new features
* Fixing existing bugs
* Improving documentation and examples

To help you on this journey we've created this document that will guide you through several steps, like [creating your development environment](#developing-python-chain), [deploying dependencies](#deploying-dependencies) and [running tests](#running-tests).

## Table of contents

* [Contributing to Python Chain](#)
  * [Developing Python Chain](#developing-python-chain)
  * [Deploying Dependencies](#deploying-dependencies)
  * [Running Tests](#running-tests)
  * [Documenting](#documenting)
  * [Versioning](#versioning)

## Developing Python Chain

On this project, we're following some conventions and it would be awesome if you could do so! Following conventions make it easier for any developer to stretch and maintain your code 😀. The major guidelines that you must follow are:

* **Domain Driven Design** => you can learn about it [here](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html), [here](https://techbeacon.com/app-dev-testing/get-your-feet-wet-domain-driven-design-3-guiding-principles) and [here](https://www.livrariacultura.com.br/p/livros/informatica-e-tecnologia/software/domain-driven-design-46458301?id_link=8787&adtype=pla&id_link=8787&gclid=EAIaIQobChMIg7i7g6_24gIVFwmRCh3UiQYBEAYYAiABEgKbt_D_BwE)
* **Test Driven Development** => you can learn about it [here](https://www.devmedia.com.br/test-driven-development-tdd-simples-e-pratico/18533) and [here](https://hackernoon.com/introduction-to-test-driven-development-tdd-61a13bc92d92)

After understanding some of our core concepts, you can now check out our folder structure. We're following the DDD structure on that:

```
python-chain
│
├── chain
| ├── core
│ │   └── domains
│ │       └── <domain>
| └── tests
|     ├── acceptance
|     |   └── steps
|     └── <unit tests>
├── requirements
├── docs
└── deploy
```

Our entire source code is inside the `chain` folder. Everything else is just folders and files to help you build the project or documentation. Inside the `chain` folder we have the following sections:

* [Core](#core-folder)
* [Tests](#tests-folder)

### Core Folder

You can find it on the following path: `<root>/chain/core`. There, you'll find every code of our core module. The codebase is organized in the following sections (folders):

* `domains` - All the domains of the application.

Most of the magic happens on the `domains` section. There's no pattern of file naming inside a specific domain. They can contain any type of file which is needed to perform a task. But, the most commons are: `handlers`, `models`, `generators`, `transformers` and so on.

### Tests Folder

You can find it on the following path: `<root>/chain/tests`. There, you'll find all the unit tests that are currently active. We're using [Pytest](https://docs.pytest.org/en/latest/) for the unit tests and [Behave](https://behave.readthedocs.io/en/latest/) to acceptance tests. Please, read their docs before creating new tests.

All unit tests are organized mimicking the structure of the chain folders. The acceptance tests are organized inside the `acceptance` folder and divided by features.

## Deploying Dependencies

To install the development version of the application on your machine you must first install all the following dependencies:

* [Python 3.7.3](https://www.python.org/downloads/release/python-373/)

It is strongly recommended to also install the following tools:

* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Now, with all the dependencies installed, you can follow the installation steps on your favorite shell:

### 1. Clone the project
```
$ git clone git@github.com:quintoandar/python-chain.git
$ cd python-chain
```

### 2. Setup the Python environment for the project
```
$ make environment
```

### 3. Install dependencies
```
$ make install-dev
```

Now, your module is good to go! And you can start debugging it.

## Running Tests

Since our application is TDD all code must have automated chain.tests. Please, be aware to not "overtest" it too. You should focus on **integration** and **acceptance** tests and write **unit** tests only when a function really needs it. You can see a pretty good article about it [here](https://kentcdodds.com/blog/write-tests).

On this application, we're using [Pytest](https://docs.pytest.org/en/latest/) as our unit test framework and [Behave](https://behave.readthedocs.io/en/latest/) as our behavior test framework. You can run them with:

```
$ pytest
$ behave
```

## Documenting

In order to keep a good, usable and maintainable code we need to document every part of our code. We're currently using [Sphinx](http://www.sphinx-doc.org/en/master/) with [Read the Docs](https://readthedocs.org) for visualization.

## Versioning

We use [SemVer 2.0.0](https://semver.org/) for versioning our releases. Also, we recommend you to use the [Python Black](https://github.com/python/black) format. We've created a script to do it for you. You can run the `make black` command before committing your code.
