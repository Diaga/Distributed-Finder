# Contributing Guide
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Set Up Environment

1. Download and install [latest version of git](https://git-scm.com/downloads).
2. Clone the repository locally
     ```shell script
    $ git clone https://github.com/Diaga/Distributed-Finder.git
    $ cd Distributed-Finder
    ```
3. Create a virtualenv.
    ```shell script
    $ python3 -m venv venv
    $ . venv/bin/activate
    ```
    On Windows, activating is different.
    ```shell script
    $ venv/Scripts/activate
    ```
4. Install python dependencies
    ```shell script
    $ pip install -r requirements.txt
    ```
5. Install the pre-commit hooks.
    ```shell script
    $ pre-commit install
    ```

## We Use [GitHub Flow](https://guides.GitHub.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [GitHub Flow](https://guides.GitHub.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
1. If you've added code that should be tested, add tests.
1. If you've changed APIs, update the documentation.
1. Ensure the test suite passes.
1. Make sure your code lints.
1. Create that pull request!

## Commit Message and Pull Request Title

Commit message and pull request title should follow [Conventional Commits](https://www.conventionalcommits.org).

An easy way to achieve that is to install [`commitizen`](https://github.com/commitizen/cz-cli) and run `git cz` when committing.
