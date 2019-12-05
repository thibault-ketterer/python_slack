import os, time
# cmd.exe /c "echo %USERNAME%" 2> /dev/null
# path_to_watch = "/mnt/c/Users/Eleves/Desktop/"
winuser = os.popen('cmd.exe /c "echo %USERNAME%"').read()
print(winuser)
path_to_watch = "/mnt/c/Users/" + winuser[:-1] + "/Desktop/"
# before = dict ([(f, None) for f in os.listdir (path_to_watch)])
alist = []
for f in os.listdir (path_to_watch):
    item = (f, None)
    alist.append(item)
print(alist)
before = dict(alist)
# print("before", before)
while 1:
  time.sleep (2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  # print("after", after)
  added = []
  for f in after:
      if not f in before:
          added.append(f)
  #added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: print("Added: ", ", ".join (added))
  if removed: print("Removed: ", ", ".join (removed))
  before = after
