"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
  if x <= 1:
    return x
  else:
    (ra, rb) = (foo(x - 1), foo(x - 2))
    return ra + rb
  pass


def longest_run(mylist, key):
  counter = 0
  runningcount = 0

  for num in mylist:
    if num == key:
      counter = counter + 1
      runningcount = max(counter, runningcount)
    else:
      counter = 0
  return runningcount

class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def longest_run_recursive(mylist, key):
  
  left = mylist[:(len(mylist) // 2)]
  right = mylist[(len(mylist) // 2):]
  
  if len(mylist) == 0:
    return Result(0, 0, 0, False)
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1, 1, 1, True)
    else:
      return Result(0,0,0, False)

  left_run = longest_run_recursive(left, key)
  right_run = longest_run_recursive(right, key)

  left_size = left_run.left_size
  right_size = right_run.right_size

  if left_run.is_entire_range and right[0] == key:
    left_size = left_size + right_run.left_size
  
  if right_run.is_entire_range and left[-1] == key:
    right_size = right_size + left_run.right_size

  longest = max(left_run.longest_size, right_run.longest_size,
                left_run.right_size + right_run.left_size)

  is_entire_range = left_run.is_entire_range & right_run.is_entire_range

  return Result(left_size,right_size,longest,is_entire_range)

## Feel free to add your own tests here.
def test_longest_run():
  assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
