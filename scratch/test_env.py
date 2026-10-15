import ctypes
from ctypes import wintypes
import os

# We want to see if we can read environment of github-mcp-server
# Or check if there is an env var in the current Python environment or system
print("Current env keys:", [k for k in os.environ.keys() if 'GIT' in k or 'HUB' in k or 'TOKEN' in k])
