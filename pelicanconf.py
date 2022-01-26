AUTHOR = 'Tyler Hillery'
SITEURL = 'https://localhost:8000'
SITENAME = 'Tyler Hillery'
SITETITLE = "Tyler Hillery"
SITESUBTITLE = "Data Enthusiast & Lifelong Learner"
SITEDESCRIPTION  = "Tyler's Thoughts and Writings"
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

#Theme settings
THEME = "themes/Flex" 
THEME_COLOR_ENABLE_USER_OVERRIDE = True #Adds toggle light & dark mode on footer
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True #Uses clients light/dark mode system preferences
THEME_COLOR = 'dark' #default is dark
PYGMENTS_STYLE = 'pastie'
PYGMENTS_STYLE_DARK = 'monokai'
GITHUB_CORNER_URL = "https://github.com/TylerHillery"

#Menu items which are show on top of the page
MAIN_MENU = True
MENUITEMS = (
    ('About', '/pages/about.html'),
    #('Contact', '/pages/contact.html'),
    ('Projects', '/pages/projects.html'),
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html')
)

#General Pelican Settings
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = False #how many articles are on one page
AUTHOR_SAVE_AS = '' #since I am the only author
LOAD_CONTENT_CACHE = False #Helpful when experimenting 

# Social widget
SOCIAL = (
    ('github', 'https://github.com/TylerHillery'),
    ('linkedin','https://www.linkedin.com/in/tylerhillery/'),
    ('twitter','https://twitter.com/_TylerHillery'),
    ('envelope', 'mailto:tyhillery@gmail.com')
)

#Path variables
PATH = 'content'
OUTPUT_PATH = 'output'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images','extra', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#License 
COPYRIGHT_NAME = 'Tyler Hillery'
COPYRIGHT_YEAR = 2022

#Plugins settings
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['readtime', 'neighbors']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Default Markdown settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#DISQUS Comment plugin
DISQUS_SITENAME = 'tylerblogs'