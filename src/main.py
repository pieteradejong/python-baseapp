"""
Base App - Main Application Entry Point

This module initializes and runs the application with proper configuration
and logging setup.
"""
import logging
from pathlib import Path
from typing import Optional

from library import AppConfig, config, setup_logging


def init_app(config_path: Optional[Path] = None) -> None:
    """
    Initialize the application with configuration and logging.
    
    Args:
        config_path: Optional path to JSON config file
    """
    # Setup logging first so we can log the initialization process
    setup_logging(config)
    logger = logging.getLogger(__name__)
    
    try:
        # Load JSON config if provided
        if config_path:
            from library import load_json_config
            json_config = load_json_config(str(config_path))
            logger.info("Loaded JSON configuration from %s", config_path)
        
        logger.info("Initializing %s v%s", config.APP_NAME, config.APP_VERSION)
        logger.info("Environment: %s (Debug: %s)", config.ENV, config.DEBUG)
        logger.info("API will run on %s:%d", config.API_HOST, config.API_PORT)
        
    except Exception as e:
        logger.error("Failed to initialize application: %s", e, exc_info=True)
        raise


def main() -> None:
    """Run the application."""
    logger = logging.getLogger(__name__)
    try:
        logger.info("Starting application...")
        # Application startup code here
        
    except Exception as e:
        logger.error("Application failed: %s", e, exc_info=True)
        raise
    finally:
        logger.info("Application shutdown complete")


if __name__ == "__main__":
    init_app()
    main()
