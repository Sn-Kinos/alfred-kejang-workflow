kejang_ver = input("케장콘 버전 입력 (e.g. 15): ")

print("----- 케장콘 내용을 복사/붙여넣기 후 빈 줄에 Ctrl+D 입력 -----")
kejang_contents = []
while True:
  try:
    line = input()
  except EOFError:
    break
  kejang_contents.append(line)

kejang_alfred = []
for kejang in kejang_contents:
  kejang_alfred.append({
    "title": "케장콘 " + kejang_ver,
    "subtitle": kejang[4:],
    "arg": kejang_ver,
  })

print(kejang_alfred)
