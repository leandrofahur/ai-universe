# AI Universe

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Project Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/ufmg/evolutionary-fsm-agentic-control/releases)
[![LangChain](https://img.shields.io/badge/LangChain-powered-blueviolet.svg)](https://www.langchain.com/)
[![CREWAI](https://img.shields.io/badge/CrewAI-powered-magenta.svg)](https://docs.crewai.com/)

> A comprehensive AI development playground exploring LangChain, Agents, and modern AI workflows.

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. **Clone the repository:**
```bash
$ git clone <your-repo-url>
$ cd ai-universe
```

2. **Create virtual environment:**
```bash
$ uv venv --python 3.12
```

3. **Activate virtual environment:**
```bash
$ source .venv/bin/activate
```

4. **Install dependencies:**
```bash
$ uv sync
```

## 📁 Project Structure

```
ai-universe/
├── .venv/                   # Virtual environment
├── .python-version          # Python version specification
├── pyproject.toml           # Project configuration
├── uv.lock                  # Dependency lock file
├── main.py                  # Main entry point
├── langchain/               # LangChain examples and tutorials
├── agents/                  # AI agents and workflows
├── CODE_OF_CONDUCT.md       # Community guidelines
├── LICENSE                  # Project license
└── README.md                # This file
```

## 🛠️ Development Commands

### Environment Management

```bash
# Activate virtual environment
$ source .venv/bin/activate

# Deactivate virtual environment
$ deactivate

# Install new dependencies
$ uv add package-name

# Install development dependencies
$ uv add --dev package-name

# Update dependencies
$ uv lock --upgrade

# Sync dependencies (install/update)
$ uv sync
```

### Running Examples

```bash
# Run main entry point
$ python main.py

# Run LangChain basics example
$ python langchain/basics/01-chainiing-prompts.py
```

### Code Quality

```bash
# Format code with Black
$ black .

# Check code formatting
$ black --check .

# List installed packages
$ uv pip list
```

## 📦 Dependencies

### Core Dependencies
- `langchain>=0.3.26` - LangChain framework
- `langchain-core>=0.3.68` - Core LangChain components
- `langchain-openai>=0.3.28` - OpenAI integration
- `openai>=1.95.1` - OpenAI Python client

### Development Dependencies
- `black>=25.1.0` - Code formatter

## 🔧 Configuration

The project uses `pyproject.toml` for configuration and `uv.lock` for reproducible builds. Key settings:

- **Python Version**: 3.12+
- **Package Manager**: uv
- **Code Formatter**: Black

## 🚀 Getting Started with Examples

### 1. Basic LangChain Example
```bash
# Run the chaining prompts example
$ python langchain/basics/01-chainiing-prompts.py
```

### 2. Main Application
```bash
# Run the main application
$ python main.py
```

## 🤝 Contributing

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Format code with Black
5. Submit a pull request

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## 🆘 Troubleshooting

### Common Issues

**Python version not found:**
```bash
# Remove .python-version if causing conflicts
$ rm .python-version

# Create venv with specific Python version
$ uv venv --python 3.12
```

**Dependencies not found:**
```bash
# Reinstall dependencies
$ uv sync --reinstall
```

**Virtual environment issues:**
```bash
# Remove and recreate virtual environment
$ rm -rf .venv
$ uv venv
$ uv sync
```

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Black Code Formatter](https://black.readthedocs.io/)


## 👨‍💻 Contributors
We welcome all contributors! Here are our current team members:

| Avatar | Name | Role | GitHub |
|--------|------|------|--------|
| <img src="https://avatars.githubusercontent.com/u/46628080?u=7c2c2d90408b1a731118b5b3512d9da890cf2d45&v=4" width="40" /> | **Leandro Miranda Fahur Machado** | Software Engineer | [@leandrofahur](https://github.com/leandrofahur) |

