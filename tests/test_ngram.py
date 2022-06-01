from ngram.ngram import generate_N_grams


def test_english():
    assert generate_N_grams('सूर्य पूर्वबाट उदाइरहेको छ।', 1) == [
        'सूर्य', 'पूर्वबाट', 'उदाइरहेको']
    assert generate_N_grams('सूर्य पूर्वबाट उदाइरहेको छ।', 2) == [
        'सूर्य पूर्वबाट', 'पूर्वबाट उदाइरहेको']
    assert generate_N_grams('सूर्य पूर्वबाट उदाइरहेको छ।', 3) == [
        'सूर्य पूर्वबाट उदाइरहेको']


def test_nepali():
    assert generate_N_grams('The sun is rising from the east.', 1) == [
        'The', 'sun', 'rising', 'east']
    assert generate_N_grams('The sun is rising from the east.', 2) == [
        'The sun', 'sun rising', 'rising east']
    assert generate_N_grams('The sun is rising from the east.', 3) == [
        'The sun rising', 'sun rising east']
