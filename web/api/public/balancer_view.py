from http import HTTPStatus

from fastapi.responses import RedirectResponse
from pydantic_core import Url

from web.api.public.router import public_router
from web.api.counter import counter
from web.settings import settings


@public_router.get(
    "/",
)
async def balancer_view(
    video: Url,
) -> RedirectResponse:
    """
    Редиректим каждый N запрос.

    :param video: original storage url
    :return Redirect
    """
    if counter.count >= settings.balancing_frequency:
        counter.refresh()
        url = str(video)
    else:
        counter.increment()
        subdomain = video.host.split(".")[0]
        url = str(
            Url.build(
                scheme=video.scheme,
                host=settings.cdn_host,
                path=f"{subdomain}{video.path}",
            )
        )
    return RedirectResponse(
        url,
        status_code=HTTPStatus.MOVED_PERMANENTLY,
    )
