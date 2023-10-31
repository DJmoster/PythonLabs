import random
import pytest

from contextlib import nullcontext as does_not_raise
from charivna_kulka import CharivnaKulka


@pytest.mark.skip
def test_random_choices():
    texts = ['Yes', 'No', 'Maybe']
    weights = [0.9, 0.05, 0.05]

    assert random.choices(texts, weights)[0] == 'Yes'


@pytest.fixture
def kulka_default_instance():
    return CharivnaKulka()


@pytest.fixture
def kulka_default_answers():
    return ['Yes', 'No', 'Maybe']


@pytest.fixture
def kulka_custom_answers():
    return ['test1', 'test2', 'test3']


@pytest.fixture
def kulka_removed_answers():
    return ['test1', 'test2']


@pytest.fixture
def kulka_custom_instance(kulka_custom_answers):
    kulka = CharivnaKulka()

    for i in kulka_custom_answers:
        kulka.add_answer(i)

    return kulka


@pytest.fixture
def kulka_removed_instance(kulka_custom_instance, kulka_removed_answers):
    for i in kulka_removed_answers:
        kulka_custom_instance.remove_answer(i)

    return kulka_custom_instance


class TestCharivnaKulka:
    PREDICT_TEST_COUNT = 500

    @pytest.mark.parametrize(
        'question, expectation',
        [
            ('test question', does_not_raise()),
            (2321, pytest.raises(TypeError)),
            (2321, pytest.raises(TypeError)),
            (['dasads', 123], pytest.raises(TypeError)),
        ]
    )
    def test_predict_exceptions(self, question, expectation, kulka_default_instance):
        with expectation:
            kulka_default_instance.predict(question)

    def test_predict_return_type(self, kulka_default_instance):
        assert isinstance(kulka_default_instance.predict('test'), str)

    def test_predict_default_answers(self, kulka_default_instance, kulka_default_answers):
        for _ in range(TestCharivnaKulka.PREDICT_TEST_COUNT):
            assert kulka_default_instance.predict('test') in kulka_default_answers

    @pytest.mark.parametrize(
        'answer, probability, expectation',
        [
            ('test', None, does_not_raise()),
            ('test', 1.0, does_not_raise()),
            (23, None, pytest.raises(TypeError)),
            ('test', 'test', pytest.raises(TypeError)),
            ('test', 322, pytest.raises(TypeError)),
            ('Yes', 'Yes', pytest.raises(TypeError)),
            ('Yes', None, pytest.raises(CharivnaKulka.AnswerExistsException)),
            ('Yes', 1.5, pytest.raises(CharivnaKulka.AnswerExistsException)),
        ]
    )
    def test_add_answer_exceptions(self, answer, probability, expectation, kulka_default_instance):
        with expectation:
            kulka_default_instance.add_answer(answer, probability)

    def test_predict_custom_answers(self, kulka_custom_instance, kulka_custom_answers, kulka_default_answers):
        kulka_answers = []
        kulka_answers.extend(kulka_default_answers)
        kulka_answers.extend(kulka_custom_answers)

        for _ in range(TestCharivnaKulka.PREDICT_TEST_COUNT):
            assert kulka_custom_instance.predict('test') in kulka_answers

    @pytest.mark.parametrize(
        'answer, expectation',
        [
            ('Yes', does_not_raise()),
            ('No', does_not_raise()),
            ('Maybe', does_not_raise()),
            (11, pytest.raises(TypeError)),
            (None, pytest.raises(TypeError)),
            ('test', pytest.raises(CharivnaKulka.AnswerNotExistsException)),
            ('test324324', pytest.raises(CharivnaKulka.AnswerNotExistsException)),
        ]
    )
    def test_remove_answer_exceptions(self, answer, expectation, kulka_default_instance):
        with expectation:
            kulka_default_instance.remove_answer(answer)

    def test_predict_removed_answers(self, kulka_removed_instance, kulka_removed_answers):
        for _ in range(TestCharivnaKulka.PREDICT_TEST_COUNT):
            assert kulka_removed_instance.predict('test') not in kulka_removed_answers
