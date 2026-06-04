# MCP Server

MCP Servers can provide the functionality like:
- **MCP Server**: A server that implements the MCP protocol, allowing clients to connect and interact with it.
- **MCP Client**: A client that can connect to an MCP server and send commands or requests.
- **MCP Protocol**: The communication protocol used between the MCP client and server, defining how messages are formatted and exchanged.
- **Resources**: file-like data that can be read by a client (like API responses or file contents)
- **Tools**: Functions that can be called by the LLMs(with user approval)
- **Prompts**: Pre-written templates that help the users accomplish specific tasks

### Requirements
- Python 3.8 or higher
- uv as package manager
- python MCP SDK 1.2.8 or higher

### Setting up the environment

1. Install uv if not available
2. Initialize the project with (uv init)
3. Add dependencies uv add ("mcp[cli]" https)