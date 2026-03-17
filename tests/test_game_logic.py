from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

# FIX: Test of the hint message for a guess that is too high or too low, to verify that the logic is correct and not reversed.

def test_guess_directional_hint_is_correct():
    # When the guess is too high, the message should tell the player to go LOWER.
    _, message_high = check_guess(60, 50)
    assert "LOWER" in message_high

    # When the guess is too low, the message should tell the player to go HIGHER.
    _, message_low = check_guess(40, 50)
    assert "HIGHER" in message_low


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
