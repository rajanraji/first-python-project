from loguru import logger
import sys

def setup_logging(level: str = "INFO") -> None:
    logger.remove()  # remove default
    logger.add(
        sys.stderr,
        level=level.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level: <7}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        enqueue=False,
        colorize=True,
        backtrace=False,
        diagnose=False,
    )
