"""
OS MODULE & PATHLIB — Working with files, paths and the filesystem
"""

# =====================================================================
# os module — low-level interaction with the operating system
# =====================================================================

import os


# ---------------------------------------------------------
# Current working directory
# ---------------------------------------------------------

os.getcwd()
# Returns current working directory

os.chdir("path/to/folder")
# Change current working directory


# ---------------------------------------------------------
# Listing files and directories
# ---------------------------------------------------------

os.listdir(".")
# List files and folders in a directory

os.scandir(".")
# Iterator with file info (faster, more detailed)


# ---------------------------------------------------------
# Creating and removing directories
# ---------------------------------------------------------

os.mkdir("new_folder")
# Create a single directory

os.makedirs("a/b/c")
# Create nested directories

os.rmdir("new_folder")
# Remove empty directory

os.removedirs("a/b/c")
# Remove nested empty directories


# ---------------------------------------------------------
# File and path operations
# ---------------------------------------------------------

os.path.exists("file.txt")
# Check if path exists

os.path.isfile("file.txt")
os.path.isdir("folder")

os.path.abspath("file.txt")
# Absolute path

os.path.join("folder", "file.txt")
# OS-independent path creation

os.path.basename("/a/b/file.txt")   # file.txt
os.path.dirname("/a/b/file.txt")    # /a/b

os.path.getsize("file.txt")
# File size in bytes


# ---------------------------------------------------------
# Environment variables
# ---------------------------------------------------------

os.environ
# Access environment variables

os.getenv("HOME")
# Get specific variable


# ---------------------------------------------------------
# Running system commands
# ---------------------------------------------------------

os.system("ls")
# Run shell command (simple, not recommended for complex tasks)


# =====================================================================
# pathlib — modern, object-oriented path handling (RECOMMENDED)
# =====================================================================

from pathlib import Path


# ---------------------------------------------------------
# Creating Path objects
# ---------------------------------------------------------

p = Path("data/file.txt")
# Path object (works on all OS)

Path.home()
# User home directory

Path.cwd()
# Current working directory


# ---------------------------------------------------------
# Path properties
# ---------------------------------------------------------

p.name          # file.txt
p.stem          # file
p.suffix        # .txt
p.parent        # data/


# ---------------------------------------------------------
# Checking paths
# ---------------------------------------------------------

p.exists()
p.is_file()
p.is_dir()


# ---------------------------------------------------------
# Creating directories
# ---------------------------------------------------------

Path("new_dir").mkdir()
# Create directory

Path("a/b/c").mkdir(parents=True, exist_ok=True)
# Create nested dirs safely


# ---------------------------------------------------------
# Listing directory contents
# ---------------------------------------------------------

for file in Path(".").iterdir():
    print(file)

# Recursive search
Path(".").rglob("*.py")


# ---------------------------------------------------------
# Reading & writing files
# ---------------------------------------------------------

p.read_text()
p.write_text("Hello world")

p.read_bytes()
p.write_bytes(b"binary data")


# ---------------------------------------------------------
# Joining paths (NO os.path.join needed!)
# ---------------------------------------------------------

data_file = Path("data") / "file.txt"


# ---------------------------------------------------------
# Resolving absolute paths
# ---------------------------------------------------------

p.resolve()
# Absolute normalized path


# ---------------------------------------------------------
# Deleting files and folders
# ---------------------------------------------------------

p.unlink()
# Delete file

Path("empty_dir").rmdir()
# Delete empty directory


# =====================================================================
# os vs pathlib (exam-important comparison)
# =====================================================================

# os:
# - procedural (functions)
# - older
# - still widely used

# pathlib:
# - object-oriented
# - cleaner syntax
# - recommended for new code
# - cross-platform by design


# =====================================================================
# Typical exam use-cases
# =====================================================================

# Check if file exists and read it
p = Path("data.txt")
if p.exists():
    content = p.read_text()

# Create directory and save file
out = Path("results")
out.mkdir(exist_ok=True)
(out / "output.txt").write_text("Done")

