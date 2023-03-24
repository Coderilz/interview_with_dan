from main import calc_score, assign_7_tiles, create_bag_of_tiles

def test_calc_score_GUARDIAN():
    result = calc_score('GUARDIAN')
    assert result == 10

def test_calc_score_empty_string():
    result = calc_score('')
    assert result == 0

def test_calc_score_lower_case_string():
    result = calc_score('guardian')
    assert result == 10

def test_assign_7_tiles():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = assign_7_tiles(alphabet)
    assert len(result) == 7

# def test_create_bag_of_tiles():
#     result = create_bag_of_tiles
#     assert == []
        


