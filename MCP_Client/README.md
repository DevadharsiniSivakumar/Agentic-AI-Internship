# MCP Clients
MCP clients can connect to MCP servers to access their functionalities like:
- Resources : File-like data that can be read from servers (like API responses or file contents)
- Tools : Functions that can be called from servers (with user approval)
- Prompts : Pre-written templates that help users accomplish specific tasks

## Requirements
- Python 3.10 or higher
- uv as Package manager
- Python MCP SDK 1.2.0 or higher

## Setting up the environment

1. Install uv if not available
2. Initialize the project with (uv init .)
3. Add the dependencies {uv add mcp anthropic python-dotenv}
4. Create client.py which has the content for our MCP client
5. Run the Script using uv run client.py