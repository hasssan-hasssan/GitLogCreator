# Log Creator

Log Creator is a simple and interactive Python tool designed to help you generate structured Git commit messages easily. It provides a user-friendly interface for writing comments, formatting them as lists, and generating the `git commit` command with the provided comments.

## Features

- Interactive command-line interface.
- Supports structured comments with topics and subtopics.
- Generates Git commit commands with formatted messages.
- Provides helpful instructions and feedback.

## How It Works

1. **Start the Program:**
   When you run the program, it clears the terminal screen and welcomes you to Log Creator.

2. **Instructions:**
   The program provides instructions on how to write your comments and format them using hash (#) for topics and asterisk (\*) for subtopics.

3. **User Input:**
   You can start writing your comments. When you are done, type `end` and press enter. If you choose to add a title to your commit, you will be prompted to write the title.

4. **Generate Git Commit Command:**
   Once you have finished writing your comments, Log Creator generates the `git commit` command with the provided comments, structured as specified.

5. **Copy the Command:**
   The generated Git commit command is displayed, and you can copy it to use in your Git workflow.

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/log-creator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd GitLogCreator
   ```
3. Run the script:
   ```sh
   python LogCreator.py
   ```
4. Output:

   ```sh
   [INFO] - Hello! Welcome to Log Creator.
   [INFO] - Write your comments and hit enter. When you're done, type 'end' and press enter.
   [INFO] - To format your message as a list, use the following structure:
   [INFO] - Use a hash [#] for topics and an asterisk [*] for subtopics.
   [INFO] - If you won't just write your message.
   [INFO] - Are you ready: (y|n)
   > y
   [INFO] - Great! Start writing your messages and remember to follow the structure.
   > #Added new features
   > *Some descriptions about feature
   > #Bug Fixed
   > *Fixed issue with validate something
   > end
   [INFO] - Do you want to add a title to this commit? (y|n)
   > y
   [INFO] - Write your title:
   > Working on a new feature
   [INFO] - Generating 'git commit' code, Please wait ...
   [INFO] - Here you go (just copy that): git commit -m "Title: Working on a new feature." -m "More details:" -m "- Added new features" -m "    - Some descriptions about feature" -m "- Bug Fixed" -m "    - Fixed issue with validate something"
   ```

5. Copy and paste command then hit enter.

   ```sh
   git commit -m "Title: Working on a new feature." -m "More details:" -m "- Added new features" -m "    - Some descriptions about feature" -m "- Bug Fixed" -m "    - Fixed issue with validate something"

   ```

6. Run git log command:

   ```sh
   > git log
   ```

7. Output:

   ```sh
   commit 3e6f68b2d86b86a3ac36b533dcad05ed43409e58 (HEAD -> master)
   Author: #######################################################
   Date:   Fri Feb 5 18:00:00 2022 +0330

       Title: Working on a new feature.

       More details:

       - Added new features

           - Some descriptions about feature

       - Bug Fixed

           - Fixed issue with validate something

   ```

---

**Enjoy a more organized workflow by writing neat and structured commits. Happy coding!**
