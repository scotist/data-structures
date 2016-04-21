"""Implement merge sort algorithm."""


def merge_sort(seq):
    """Merge Sort Function."""
    length = len(seq)
    if length < 2:
        return
    middle = length // 2
    left = seq[:middle]
    right = seq[middle:]
    merge_sort(left)
    merge_sort(right)
    i_left = 0
    i_right = 0
    i_seq = 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            seq[i_seq] = left[i_left]
            i_left += 1
        else:
            seq[i_seq] = right[i_right]
            i_right += 1
        i_seq += 1

    while i_left < len(left):
        seq[i_seq] = left[i_left]
        i_left += 1
        i_seq += 1

    while i_right < len(right):
        seq[i_seq] = right[i_right]
        i_right += 1
        i_seq += 1

if __name__ == "__main__":
    from time_sorting import time_sorting
    time_sorting(merge_sort)
