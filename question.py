class Question:
    def __init__(self, question_text, options, correct_answer):
        """
        question_text: str - The question being asked
        options: list of str - The list of answer choices (A–D or True/False)
        correct_answer: str - The correct answer string
        """
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        """
        Returns True if user_answer matches correct_answer (case-insensitive)
        """
        return user_answer.strip().lower() == self.correct_answer.strip().lower()
