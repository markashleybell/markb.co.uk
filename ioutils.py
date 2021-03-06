"""File I/O functions."""

import codecs
import configparser
import glob
import os
from jinja2 import Environment, FileSystemLoader

def get_config():
    """Load configuration from files."""
    parser = configparser.RawConfigParser()
    parser.read("config.cfg")

    return {
        "site_name": parser.get("Site", "site_name"),
        "site_url": parser.get("Site", "site_url"),
        "cdn1": parser.get("Site", "cdn1"),
        "cdn2": parser.get("Site", "cdn2"),
        "analytics_id": parser.get("Site", "analytics_id"),
        "disqus_id": parser.get("Site", "disqus_id"),
        "rss_description": parser.get("Site", "rss_description"),
        "output_folder": "public"
    }

def load_templates():
    """Load Jinja templates."""
    environment = Environment(loader=FileSystemLoader("templates/"))

    return {
        "home": environment.get_template("home.html"),
        "articleindex": environment.get_template("articleindex.html"),
        "basic": environment.get_template("basic.html"),
        "post": environment.get_template("post.html")
    }

def write_file_utf8(output_filename, content):
    """Write content to the specified file with UTF-8 encoding."""
    codec = codecs.open(output_filename, "w", "utf-8")
    codec.write(content)
    codec.close()

def delete_files(file_spec):
    """Delete all files matching file_spec glob pattern."""
    for file_name in glob.glob(file_spec):
        os.remove(file_name)
