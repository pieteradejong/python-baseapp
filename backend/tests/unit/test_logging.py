"""Tests for logging setup and functionality."""
import logging
import tempfile
from pathlib import Path

import pytest
from library import AppConfig, setup_logging

def test_setup_logging_console(app_config: AppConfig) -> None:
    """Test console logging setup."""
    setup_logging(app_config)
    logger = logging.getLogger(__name__)
    
    # Verify logger is configured
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)

def test_setup_logging_file() -> None:
    """Test file logging setup."""
    with tempfile.NamedTemporaryFile(suffix='.log') as f:
        config = AppConfig(LOG_FILE=Path(f.name))
        setup_logging(config)
        logger = logging.getLogger(__name__)
        
        # Verify both console and file handlers
        assert len(logger.handlers) == 2
        assert any(isinstance(h, logging.FileHandler) for h in logger.handlers)
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
        
        # Test logging to file
        test_message = "Test log message"
        logger.info(test_message)
        
        # Verify message was written to file
        with open(f.name) as log_file:
            log_content = log_file.read()
            assert test_message in log_content

def test_setup_logging_levels() -> None:
    """Test different logging levels."""
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    
    for level in levels:
        config = AppConfig(LOG_LEVEL=level)
        setup_logging(config)
        logger = logging.getLogger(__name__)
        assert logger.level == getattr(logging, level)

def test_setup_logging_invalid_level() -> None:
    """Test invalid logging level."""
    with pytest.raises(ValueError, match="LOG_LEVEL must be one of"):
        AppConfig(LOG_LEVEL="INVALID") 