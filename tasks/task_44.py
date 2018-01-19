import random

def max_sum_subarray(arr):
  max_found = None
  current_range_sum = 0
  for val in arr:
    current_range_sum += val
    max_found = max(max_found, current_range_sum)
    
    # if a current_range has gotten to be negative,
    # we reset the current_range_sum to 0 because
    # the next contiguous subarray cannot possibly
    # be at its max value if it includes the current,
    # negative subrange.
    current_range_sum = max(current_range_sum, 0)
  return max_found

print "Max sum of a subarray in %s is %d" % ([1,2,3,-5,4], max_sum_subarray([1,2,3,-5,4]))
print "Max sum of a subarray in %s is %d" % ([-8, -23, -14], max_sum_subarray([-8, -23, -14]))
print "Five Random Test Cases"
for x in xrange(5):
  a = [int(10*random.random()) for i in xrange(10)]
  print "Max sum of a subarray in %s is %d" % (a, max_sum_subarray(a))


def clock_angle(h, m):
  h_deg = (h * 30) % 360
  m_deg = (m * 6) % 360
  h_deg += m / 2        # hr moves 30 degrees per 60 minutes
  angle = abs(h_deg - m_deg)
  if angle > 180:
    angle = 360 - angle
  return angle


print "The smallest angle at %d:%02d is %d degrees" % (12, 0, clock_angle(12, 0))
print "The smallest angle at %d:%02d is %d degrees" % (3, 15, clock_angle(3, 15))
print "The smallest angle at %d:%02d is %d degrees" % (6, 0, clock_angle(6, 0))
print "Five Random Test Cases"
for x in xrange(5):
    h, m = int(12*random.random())+1, int(60*random.random())
    print "The smallest angle at %d:%02d is %d degrees" % (h, m, clock_angle(h, m))