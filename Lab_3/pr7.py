#Write a program to copy move and delete files using shut il module.
import os
import shutil

# 1. COPY a file
shutil.copy("source.txt", "copied.txt")

# # 2. MOVE or Rename a file
# shutil.move("copied.txt", "moved_file.txt")

# # 3. DELETE a whole folder (and everything inside)
# shutil.rmtree(".ipynb_checkpoints")

# # Bonus: DELETE a single file (uses os module)
# os.remove("moved_file.txt")
