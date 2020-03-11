from datetime import datetime

import factory
import pytest

from django.contrib.auth.models import User


class UserFactory(factory.Factory):
    """ Create a User using factory-boy """

    class Meta:
        abstract = False
        model = User

    username = factory.Sequence(lambda i: "blogtest" + str(i))
    first_name = "John"
    last_name = "Doe"
    email = factory.Sequence(lambda i: "blogtest%s@example.com" % i)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def basic_page_data():
    # Required fields for Page object
    return {"title": "Page title", "slug": "pg1", "content": "Contents"}


@pytest.fixture
def blog_post_data():
    mock_user: User = UserFactory()
    # Required fields for Blog Post objects
    return {
        "author": mock_user,
        "title": "Post title",
        "slug": "post_slug",
        "image": b"image",
        "text": "Lorem ipsum",
        "tags": ["1"],
        "is_visible": True,
        "published": True,
        "created": datetime.strptime(
            "Feb 29 2020  11:22PM", "%b %d %Y %I:%M%p"
        ),
        "updated": datetime.strptime(
            "Feb 29 2020  11:33PM", "%b %d %Y %I:%M%p"
        ),
    }

