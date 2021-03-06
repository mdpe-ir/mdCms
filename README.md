# MD CMS

[![](https://img.shields.io/pypi/pyversions/Django.svg)](https://python.org/downloads/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://choosealicense.com/licenses/mit/)

Full-Featured Blog and Cms with Django web framework.

-----

## **For Now We only Support Persian Language**

Screenshots
=

Coming Soon ...

Features
=

- Support Persian Language
- User Registration
- User Login & Logout
- User Profile
- Create, Update, Edit & Delete Posts
- Comments
- Search
- User Change Password
- Password Reset
- Customized admin panel
- Use CKEDITOR

How To Use
=

## Clone project & Install Requirements

> Make sure you have already installed python3 and git.

```

This Part complete comming soon ! 

```

## Migrate & Collect Static

```
$ cd src && python manage.py migrate
$ python manage.py collectstatic
```

## Create Admin User

```
$ python manage.py createsuperuser
```

## Run Server

```
$ python manage.py runserver
```

> Enter your browser http://localhost:8000/. You can login via admin in http://localhost:8000/admin/.

## Add Some Fake Posts

> First add one another user from blog register page or admin panel.

```
$ python manage.py shell
>>> from blog.models import Post
>>> import json
>>> with open('posts.json') as f:
...     json_posts = json.load(f)
...
>>> for post in json_posts:
...     Post(title=post['title'], content=post['content'], author_id=post['user_id']).save()
...
>>> exit()
```

> You can edit posts via admin panel or from corrent user added post.

TODOS
=

- Change Admin Style
- Change Site Style
- More Options For New Post
- Sidebar ✅
- Reply comment
- Search for post any pages
- Create following system
- Read later post
- Add Slider
- Add Another Language
    - English
    - French
    - Arabic
- New Admin Panel
- Support plugins
- Support Them Installer
- Support SMTP email
- Scheduled post
- Add Installer
- Add E-commerce Module
- ...

-----

Author
=

###### Mahan Esnaasharan

Site : Mdpe.ir
