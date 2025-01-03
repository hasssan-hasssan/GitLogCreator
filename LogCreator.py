import logging
import time
import os

# Config logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')


class LogCreator:
    COMMENTS: list[str] = []
    PROMPT: str = '> '
    ASTERISK: str = '*'
    HASH: str = '#'
    NOTHING: str = ''
    SLEEP_TIME: int | float = 2

    def hello_message(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.sleep(self.SLEEP_TIME)
        logging.info('Hello! welcome to Log Creator.')
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
                if self.validate_comments(self.COMMENTS) != 0:
                    self.generate_git_commit_command(self.COMMENTS)
        else:
            logging.info("See you later.")

    def get_valid_input(self, prompt: str):
        while True:
            answer: str = input(prompt).lower()
            if answer in ['y', 'n']:
                return answer
            else:
                logging.error("Invalid input. Please press 'y' or 'n'. ")

    def validate_comments(self, comments: list[str]):
        if not comments:
            logging.info(
                "Why you didn't write any comments, You broke my heart :(")
            return 0
        else:
            self.COMMENTS = [comment for comment in self.COMMENTS if comment]

    def get_comments(self, prompt: str):
        while True:
            comment: str = input(prompt)
            if comment == 'end':
                return 'done'
            else:
                self.COMMENTS.append(comment)

    def generate_git_commit_command(self, comments: list[str]):
        logging.info("Generating 'git commit' code, Please wait ...")
        self.sleep(self.SLEEP_TIME)
        git_command = "git commit"
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
            git_command += f'-m "{msgs}"'
        logging.info(f'Here you go (just copy that): {git_command}')

    def sleep(self, _time: int | float):
        time.sleep(_time)


if __name__ == '__main__':
    log_creator = LogCreator()
    log_creator.hello_message()
