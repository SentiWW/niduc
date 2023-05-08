from faker import Faker

def create_data(file_name: str, words_per_sentence=10, number_of_sentences=10):
    fake = Faker()
    words = fake.sentence(words_per_sentence, True)
    for i in range(number_of_sentences-1): 
        words += " " + fake.sentence(words_per_sentence, True)

    file = open(file_name, 'w')
    file.write(words)
    file.close

