from greedy_scheduling import scheduling_by_diff, scheduling_by_div


def test_large_array() -> None:
    with open("tests/LargeArrayGreedy.txt", "r") as file:
        jobs = [(int(w), int(d)) for job in file for w, d in [job.split()]]
    assert scheduling_by_diff(jobs) == 69119377652
    assert scheduling_by_div(jobs) == 67311454237
