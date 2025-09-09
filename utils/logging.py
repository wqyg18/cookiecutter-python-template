import sys
from pathlib import Path
from loguru import logger

# This logger.py template is designed for production use with loguru version 0.7.3.
# It provides colored console output for interactive sessions and structured JSON
# logging to a file for persistent, machine-readable records.

def setup_logger(
    log_level="INFO",
    console_format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                   "<level>{level: <8}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                   "<level>{message}</level>",
    log_file_path="logs/app.log",
    json_log_level="DEBUG",
    log_rotation="10 MB",
    log_retention="30 days",
    log_compression="zip"
):
    """
    Configures the Loguru logger with both console and JSON file sinks.

    In a production environment, it is recommended to have structured (JSON)
    logs for easier parsing and analysis by log management systems. Colored
    console logs are beneficial for development and real-time monitoring.

    Args:
        log_level (str): The minimum log level for the console output.
        console_format (str): The format string for console logs.
        log_file_path (str or Path): The path to the log file.
        json_log_level (str): The minimum log level for the JSON file output.
        log_rotation (str): The condition for rotating the log file (e.g., "10 MB", "12:00"). [1, 14]
        log_retention (str): How long to keep old log files (e.g., "30 days"). [1, 7]
        log_compression (str): The compression format for rotated files (e.g., "zip", "gz").
    """
    # It's important to remove the default handler to avoid duplicate logs. [5, 11]
    logger.remove()

    # Configure the console sink with colored output.
    # The `colorize=True` argument enables colorized logging in the console.
    # Loguru automatically detects if the terminal supports colors. [3, 7]
    logger.add(
        sys.stderr,
        level=log_level,
        format=console_format,
        colorize=True,
        backtrace=True,  # Show full stack trace on exceptions
        diagnose=False   # Recommended to be False in production to avoid leaking sensitive data [5, 8]
    )

    # Configure the file sink for JSON logging.
    # The `serialize=True` argument formats log records as JSON. [1, 13]
    log_file = Path(log_file_path)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger.add(
        log_file,
        level=json_log_level,
        serialize=True,
        rotation=log_rotation,
        retention=log_retention,
        compression=log_compression,
        backtrace=True,  # Include full stack trace in logs
        diagnose=False   # Keep False in production [5, 8]
    )

    logger.info("Logger configured with console and JSON file sinks.")


# Example of how to use the configured logger.
if __name__ == "__main__":
    # Configure the logger when the application starts.
    # This should ideally be done once at the entry point of your application. [11]
    setup_logger()

    logger.debug("This is a debug message and will only appear in the JSON log.")
    logger.info("Application is starting up.")
    logger.success("This is a success message.")
    logger.warning("There might be an issue here.")
    logger.error("An error has occurred.")
    logger.critical("A critical error has occurred, shutting down.")

    # Example of logging an exception.
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("An exception was caught.")

    # Example of using bind to add contextual data to logs.
    user_logger = logger.bind(user_id=123, ip="192.168.1.1")
    user_logger.info("User performed an action.")