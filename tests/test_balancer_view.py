from fastapi import FastAPI

from web.settings import settings


def test_balancer_view(
    client,
    fastapi_app: FastAPI,
) -> None:
    """
    Проверяет ручку балансировки.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """

    url = fastapi_app.url_path_for("balancer_view")
    for i in range(1, settings.balancing_frequency + 1):
        response = client.get(
            url,
            params={"video": "http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8"},
            allow_redirects=False,
        )
        if i == settings.balancing_frequency:
            assert (
                response.headers["location"]
                == "http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8"
            )
        else:
            assert (
                response.headers["location"]
                == f"http://{settings.cdn_host}/s1/video/1488/xcg2djHckad.m3u8"
            )
