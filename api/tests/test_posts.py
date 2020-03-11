import pytest

from blog.models import Post


base_url = "/api/v1/posts"


@pytest.mark.django_db
def test_post_details_get(blog_post_data, api_client):
    Post.objects.create(**blog_post_data)
    post1 = Post.objects.get(slug="post1")

    url = f"{base_url}post1/"

    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["slug"] == post1.slug
