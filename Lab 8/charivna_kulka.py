import random


class CharivnaKulka:
    """
    A class of a magic ball that can answer your questions using the **predict(question: str)** method.

    Methods:
        predict(question: str):
            Makes predict for your question.

        add_answer(answer: str, probability: float = None):
            Adds a custom answer for **predict** method also you can set probability of occurrence.

        remove_answer(answer: str):
            Removes the specified answer from the list of answers.
    """

    class AnswerExistsException(Exception):
        pass

    class AnswerNotExistsException(Exception):
        pass

    DEFAULT_PROBABILITY: float = 1.0

    def __init__(self):
        self.__answers: dict[str, float] = {
            'Yes': CharivnaKulka.DEFAULT_PROBABILITY,
            'No': CharivnaKulka.DEFAULT_PROBABILITY,
            'Maybe': CharivnaKulka.DEFAULT_PROBABILITY,
        }

    def __chose_random_answer(self) -> str:
        return random.choices(
            list(self.__answers.keys()),
            list(self.__answers.values())
        )[0]

    def predict(self, question: str) -> str:
        """
        Makes predict for your question.

        Args:
            question (str): The question you want to get an answer to.

        Returns:
            str: Random answer to a question from the list of answers.

        Raises:
            TypeError: When method gets incorrect question type.
        """

        if not isinstance(question, str):
            raise TypeError('Question type must be string!')

        answer = self.__chose_random_answer()

        print(f'You asked Kulka: {question}')
        print(f'[Kulka]: {answer}')

        return answer

    def add_answer(self, answer: str, probability: float = None):
        """
        Adds a custom answer for **predict** method also you can set probability of occurrence.

        Args:
            answer (str): The answer you want to add to the list of answers.
            probability (float): The probability of this answer appearing. *Note: default is 1*

        Returns:
            None

        Raises:
            TypeError: When method arguments are of the wrong type.
            AnswerExistsException: When the answer is already in the list of answers.
        """

        if not isinstance(answer, str):
            raise TypeError('Answer type must be string!')

        if probability is None:
            probability = CharivnaKulka.DEFAULT_PROBABILITY

        if not isinstance(probability, float):
            raise TypeError('Probability type must be float!')

        if answer in self.__answers.keys():
            raise CharivnaKulka.AnswerExistsException('Answer already exists!')

        self.__answers[answer] = probability

    def remove_answer(self, answer: str):
        """
        Removes the specified answer from the list of answers.

        Args:
            answer (str): The answer you want to remove from the list of answers.

        Returns:
            None

        Raises:
            TypeError: When method arguments are of the wrong type.
            AnswerNotExistsException: When the answer does not exist in the answer list.
        """

        if not isinstance(answer, str):
            raise TypeError('Answer type must be string!')

        if answer not in self.__answers.keys():
            raise CharivnaKulka.AnswerNotExistsException('Answer not exists!')

        del self.__answers[answer]
