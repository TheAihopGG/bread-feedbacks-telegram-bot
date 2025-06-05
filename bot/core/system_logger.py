from typing import Callable, Awaitable
from logging import (
    basicConfig,
    getLogger,
    StreamHandler,
    FileHandler,
)

from .configs.system_logger_config import (
    SYSTEM_LOGS_ECHO,
    SYSTEM_LOGS_FORMATTER,
    SYSTEM_LOGS_LEVEL,
    SYSTEM_LOGS_FILENAME,
)

system_logger = getLogger(__name__)
basicConfig(
    format=SYSTEM_LOGS_FORMATTER,
    level=SYSTEM_LOGS_LEVEL,
    handlers=[
        FileHandler(SYSTEM_LOGS_FILENAME),
        StreamHandler(),
    ],
)


def async_system_logger_decorator[**P, R](
    echo: bool = SYSTEM_LOGS_ECHO,
) -> Callable[..., Callable[P, Awaitable[R]]]:
    def inner(
        func: Callable[P, Awaitable[R]],
    ) -> Callable[P, Awaitable[R]]:
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if echo:
                system_logger.debug(
                    f"Calling {func.__name__} with args={args}, kwargs={kwargs}"
                )

                result = await func(*args, **kwargs)

                system_logger.debug(
                    f"Finished {func.__name__} with result={result}",
                )
            else:
                result = await func(*args, **kwargs)
            return result

        return wrapper

    return inner


def system_logger_decorator[**P, R](
    echo: bool = SYSTEM_LOGS_ECHO,
) -> Callable[..., Callable[P, R]]:
    def inner(
        func: Callable[P, R],
    ) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if echo:
                system_logger.debug(
                    f"Calling {func.__name__} with args={args}, kwargs={kwargs}"
                )

                result = func(*args, **kwargs)

                system_logger.debug(
                    f"Finished {func.__name__} with result={result}",
                )
            else:
                result = func(*args, **kwargs)
            return result

        return wrapper

    return inner


__all__ = [
    "system_logger_decorator",
    "async_system_logger_decorator",
    "system_logger",
]
