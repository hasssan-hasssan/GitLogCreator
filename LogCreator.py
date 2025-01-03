import logging
import time
import os

# Config logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')


class LogCreator:
    COMMENTS: list[str] = []  # Initialize an empty list to store comments
    PROMPT: str = '> '  # Define the prompt string
    ASTERISK: str = '*'  # Define the asterisk symbol
    HASH: str = '#'  # Define the hash symbol
    NOTHING: str = ''  # Define an empty string
    SLEEP_TIME: int | float = 1  # Define the sleep time in seconds
    ANSWERS = ['y', 'n']  # Define acceptable answers

    def hello_message(self):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        self.sleep(self.SLEEP_TIME)
        logging.info('Hello! Welcome to Log Creator.')
        self.sleep(self.SLEEP_TIME)
        logging.info(
            "Write your comments and hit enter. When you're done, type 'end' and press enter.")
        self.sleep(self.SLEEP_TIME)
        logging.info(
            'To format your message as a list, use the following structure:')
        self.sleep(self.SLEEP_TIME)
        logging.info(
            'Use a hash [#] for topics and an asterisk [*] for subtopics.')
        self.sleep(self.SLEEP_TIME)
        logging.info("If you won't just write your message.")
        self.sleep(self.SLEEP_TIME)
        logging.info('Are you ready: (y|n)')
        answer = self.get_valid_input(self.PROMPT)
        if answer == 'y':
            logging.info(
                "Great! Start writing your messages and remember to follow the structure.")
            if self.get_comments(self.PROMPT) == 'done':
                if self.validate_comments(self.COMMENTS):
                    self.generate_git_commit_command(self.COMMENTS)
        else:
            logging.info("See you later.")

    def get_valid_input(self, prompt: str) -> str:
        # Get valid input from the user
        while True:
            answer: str = input(prompt).lower()
            if answer in self.ANSWERS:
                return answer
            else:
                logging.error("Invalid input. Please press 'y' or 'n'.")

    def validate_comments(self, comments: list[str]) -> bool:
        # Validate the comments list
        if not comments:
            logging.info(
                "Why you didn't write any comments, You broke my heart :(")
            return False
        else:
            self.COMMENTS = [comment for comment in self.COMMENTS if comment]
            return True

    def get_comments(self, prompt: str) -> str:
        # Collect comments from the user
        while True:
            comment: str = input(prompt)
            if comment == 'end':
                return 'done'
            else:
                self.COMMENTS.append(comment)

    def generate_git_commit_command(self, comments: list[str]):
        # Generate the git commit command
        git_command = "git commit"

        title = self.get_title()
        if title != 0:
            git_command += title

        logging.info("Generating 'git commit' code, Please wait ...")
        self.sleep(self.SLEEP_TIME)

        msgs = []
        for index, comment in enumerate(comments):
            if comment.startswith(self.HASH):
                git_command += f' -m "- {
                    comment.replace(self.HASH, self.NOTHING)}"'
            elif comment.startswith(self.ASTERISK):
                git_command += f' -m "    - {
                    comment.replace(self.ASTERISK, self.NOTHING)}"'
            else:
                msgs.append(f'{comment}')
        if msgs:
            msgs = ', '.join(msgs)
            git_command += f' -m "{msgs}"'
        logging.info(f'Here you go (just copy that): {git_command}')

    def sleep(self, _time: int | float):
        # Sleep for the specified time
        time.sleep(_time)

    def get_title(self) -> str:
        # Get the commit title from the user
        logging.info("Do you want to add a title to this commit? (y|n)")
        answer = self.get_valid_input(self.PROMPT)
        if answer == 'y':
            logging.info('Write your title: ')
            return f' -m "Title: {input(self.PROMPT)}." -m "More details:"'
        else:
            return 0


if __name__ == '__main__':
    # Create an instance of LogCreator and call the hello_message method
    log_creator = LogCreator()
    log_creator.hello_message()
