def test_42576():
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    assert "leo" == solution(participant, completion)

    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    assert "mislav" == solution(participant, completion)

    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    assert "vinko" == solution(participant, completion)

