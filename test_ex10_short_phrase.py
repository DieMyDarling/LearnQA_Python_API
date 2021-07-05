

def test_phrase():
    phrase = input("Set a phrase: ")
    print("Phrase lenght is " + str(len(phrase)))
    assert len(phrase) < 15, "There is 15 or more symbols "

    