#!/usr/bin/env python3
"""Post-render: keep the old Pelican feed URL alive.

The Pelican site served its Atom feed at /feeds/all.atom.xml. Feed
readers don't follow HTML redirect pages, so copy the Quarto feed to
the legacy path.
"""
import pathlib
import shutil

site = pathlib.Path(__file__).resolve().parent.parent / '_site'
feed = site / 'index.xml'
legacy = site / 'feeds' / 'all.atom.xml'
if feed.exists():
    legacy.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(feed, legacy)
    print(f'copied {feed.name} -> feeds/all.atom.xml')
