# Personal Blog 
This repository hosts the code for my personal [website](https://tylerhillery.github.io).

The website is powered by [Pelican](http://getpelican.com/) — a static site generator written in Python.
## Build Locally

The easiest way to do this is in a Python [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

### Create a Virtual Environment

I would create a virtual environment first. I use Python's built in venv package. :

    $ python -m venv venv
    $ source .venv/bin/activate

This creates a virtual environment and then activates it. If you want to exit the virtual environment, type:

    $ deactivate

### Fork / Clone the Repo

If you haven't already, clone your version of the repo:

    $ git clone --recurse-submodules https://github.com/yourusername/repo/fork

### Install Pelican & Dependancies

Use `pip` to install the list of dependencies (including Pelican) into your virtual environment:

    $ pip install -r requirements.txt

### Generate the Website

Now that the dependencies exists, we can build:

    $ invoke build

This takes the Markdown files from the `content/` directory and generates static HTML pages inside the `output/` directory. That's it. No database required.

### Preview the Website

You can serve the generated site so it can be previewed in your browser:

    $ invoke serve

And you should see the blog if you visit [http://localhost:8000](http://localhost:8000).

## Blog Workflow

If you're interested in writing a blog post for the website, you need to:

- [Fork](https://github.com/tylerhillery/tylerhillery.github.io/fork) the repository
- Write a blog post using Markdown in the `content` directory
- Push the changes to a topic branch, like `an-example-article`, on *your* fork of the repository
- Make a [pull request](https://help.github.com/articles/using-pull-requests/) against the `source` branch

## Hosting

This blog is hosted by [GitHub Pages](https://pages.github.com/)

## License

The source code for generation of the blog is under [MIT License](https://github.com/ayushkumarshah/ayushkumarshah.github.io/blob/source/LICENSE.md). Content is copyrighted.

## Contact

If you have any questions, you can [email](mailto:tyhillery@gmail.com) me.