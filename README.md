# Python Base App

[![python-baseapp](https://github.com/pieteradejong/python-baseapp/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pieteradejong/python-baseapp/actions/workflows/ci.yml)

A minimal, lean Python web application template that provides a clean starting point for new projects. Built with a focus on simplicity and maintainability, using only essential dependencies. The project emphasizes:

- 🎯 **Minimal Dependencies**: Only essential packages included
- 🚀 **Fast Development**: Quick setup and iteration
- 🔒 **Type Safety**: Built-in type checking without complexity
- 📦 **No External Services**: Runs without Redis, databases, or other external dependencies
- 🛠️ **Modern Tooling**: Latest stable versions of core tools
- 🧪 **Testing Ready**: Basic testing setup without over-engineering

## Project Philosophy

This template is designed to be a minimal, practical starting point that you can build upon. It intentionally avoids:

- ❌ Complex dependency trees
- ❌ External service requirements
- ❌ Over-engineered solutions
- ❌ Unnecessary abstractions
- ❌ Development environment complexity

Instead, it focuses on:

- ✅ Essential dependencies only
- ✅ Fast local development
- ✅ Clear, maintainable code
- ✅ Practical best practices
- ✅ Easy onboarding for new developers

## Tech Stack

### Backend
- **Framework**: FastAPI 0.109.2 - Modern, fast web framework for building APIs with Python
- **Server**: Uvicorn 0.27.1 - Lightning-fast ASGI server
- **Data Validation**: Pydantic 2.6.1 - Data validation using Python type annotations
- **Configuration**: pydantic-settings - Type-safe configuration management
- **Environment**: Python 3.12.2 with strict type checking

### Development Tools
- **Code Quality**:
  - Black 24.2.0 - Code formatting
  - Ruff 0.2.2 - Fast Python linter (replaces multiple tools)
  - MyPy 1.8.0 - Static type checking
- **Testing**: pytest 7.2.0 - Testing framework
- **Environment**: python-dotenv 1.0.1 - Environment variable management

### Frontend (Optional)
- **Framework**: React with Vite
- **Package Manager**: npm/yarn
- **Development**: Node.js 18+

## Features

- 🐍 Python 3.12.2 with strict type checking
- 🚀 FastAPI backend with automatic API documentation
  - OpenAPI/Swagger UI at `/docs`
  - ReDoc at `/redoc`
  - Automatic request validation
  - Async support
  - High performance
- ⚡ Modern frontend with Vite/React (optional)
- 🔒 Type-safe configuration management with pydantic
- 📝 Comprehensive logging system
- 🧪 Testing setup with pytest
- 🎨 Code formatting with Black
- 🔍 Linting with Ruff
- 🔄 CI/CD ready

## Dependencies

We maintain a minimal set of dependencies to keep the project lean and maintainable:

### Core Dependencies (requirements.txt)
```
fastapi==0.109.2    # Web framework
uvicorn==0.27.1     # ASGI server
pydantic==2.6.1     # Data validation
pydantic-settings==2.1.0 # Configuration
python-dotenv==1.0.1 # Environment variables
```

### Development Dependencies
```
black==24.2.0       # Code formatting
ruff==0.2.2         # Linting (replaces multiple tools)
mypy==1.8.0         # Type checking
pytest==7.2.0       # Testing
```

Key points about our dependencies:
- Each package serves a specific, essential purpose
- No overlapping functionality
- Latest stable versions
- No external service requirements
- Minimal development setup

## Quick Start

### Prerequisites

- Python 3.12.2 (explicitly required)
  ```bash
  # macOS
  brew install python@3.12
  
  # Ubuntu/Debian
  sudo apt update
  sudo apt install python3.12 python3.12-venv
  
  # Verify installation
  python3.12 --version  # Should show Python 3.12.2
  ```
- Node.js 18+ (for frontend)
  ```bash
  # macOS
  brew install node@18
  
  # Ubuntu/Debian
  curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
  sudo apt install nodejs
  
  # Verify installation
  node --version  # Should show v18.x.x
  ```
- Git
  ```bash
  # macOS
  brew install git
  
  # Ubuntu/Debian
  sudo apt install git
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone <this-repository-url>
   cd python-baseapp
   ```

2. Make the initialization script executable:
   ```bash
   chmod +x init.sh
   ```

3. Run the initialization script:
   ```bash
   ./init.sh
   ```
   This will:
   - Verify Python 3.12.2 is installed
   - Create a virtual environment with Python 3.12.2
   - Install Python dependencies
   - Install frontend dependencies (if frontend/ exists)
   - Set up pre-commit hooks
   - Clean up any existing caches

   If you encounter any issues:
   - Ensure Python 3.12.2 is installed and available as `python3.12`
   - Check that the virtual environment is created with Python 3.12.2
   - Verify all dependencies are installed correctly

### Configuration

1. Create a `.env` file in the project root:
   ```env
   APP_ENV=development
   APP_DEBUG=true
   APP_NAME="Python Base App"
   APP_VERSION="0.1.0"
   API_HOST=0.0.0.0
   API_PORT=8000
   LOG_LEVEL=INFO
   LOG_FILE=app/logs/app.log
   ```

2. Create a `config.json` for application settings:
   ```json
   {
       "CANDIDATE_ID": "your-id-here"
   }
   ```

### Running the Application

1. Start all services:
   ```bash
   ./run.sh
   ```
   This will:
   - Verify Python 3.12.2 is being used
   - Check required environment variables
   - Start the backend API (http://localhost:8000)
   - Start the frontend dev server (http://localhost:5173)
   - Start the API documentation (http://localhost:8000/docs)

2. View logs:
   ```bash
   tail -f app/logs/backend.log app/logs/frontend.log
   ```

### Troubleshooting

If you encounter issues:

1. **Python Version Issues**
   ```bash
   # Check Python version
   python3.12 --version  # Should show Python 3.12.2
   
   # If using a different version, install Python 3.12.2
   # macOS
   brew install python@3.12
   
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3.12 python3.12-venv
   ```

2. **Virtual Environment Issues**
   ```bash
   # Remove existing virtual environment
   rm -rf venv
   
   # Recreate with correct Python version
   python3.12 -m venv venv
   source venv/bin/activate
   
   # Verify Python version in virtual environment
   python --version  # Should show Python 3.12.2
   ```

3. **Dependency Issues**
   ```bash
   # Ensure you're in the virtual environment
   source venv/bin/activate
   
   # Reinstall dependencies
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

### Testing

Run tests with pytest:
```bash
pytest tests/
```

For coverage report:
```bash
pytest --cov=src tests/
```

### Project Structure

```
python-baseapp/
├── src/               # Core application code
├── app/              # Application package
│   ├── api/         # FastAPI routes
│   ├── models/      # Data models
│   └── logs/        # Application logs
├── frontend/         # React frontend
├── tests/           # Test suite
├── .env             # Environment variables
├── config.json      # Application config
├── requirements.txt # Python dependencies
└── run.sh          # Service management
```

## Best Practices

This project follows strict development standards:

1. **Type Safety**
   - Strict type checking enabled
   - No untyped functions or variables
   - Comprehensive type hints
   - Type-safe configuration

2. **Configuration**
   - Environment variables for deployment
   - JSON config for application settings
   - Type-safe config validation
   - Environment-specific settings

3. **Logging**
   - Structured logging
   - Both console and file output
   - Configurable log levels
   - Proper error tracking

4. **Error Handling**
   - Custom exception classes
   - Proper error propagation
   - Contextual error messages
   - Comprehensive logging

5. **Security Best Practices**
   - Validate all input
   - Use type-safe security checks
   - Regular dependency updates
   - Secure error handling
   - Proper authentication
   - Rate limiting
   - Security headers
   - CORS and CSP
   - No security theater
   - Focus on real threats

6. **Development Velocity**
   - Fast local development
   - Quick feedback loops
   - Efficient tooling
   - Smart caching
   - Automated routine tasks
   - Clear separation of concerns
   - Practical best practices

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

[Your chosen license]