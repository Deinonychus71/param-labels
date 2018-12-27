def assert_is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        assert key(el) >= key(lst[i]) # i is the index of the previous element

def test_hashes():
    from binascii import crc32
    
    with open("ParamLabels.csv") as f:
        csv = [line.rstrip('\n').split(',') for line in f.readlines() if not line.isspace()]
    
    assert_is_sorted(csv, key=lambda i: i[1])
    for line in csv:
        assert crc32(line[1].encode('utf-8')) == int(line[0], 16)