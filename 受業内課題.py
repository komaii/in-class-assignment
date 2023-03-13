#入場人数確認
print("入場人数を入力してください。")
num = input()
num = int(num)

#入場ゲート確認(今回は内野席のみ)

for i in range(0,num):
  print(i,"人目：1塁側か3塁側のどちらか入力してください")
  gate = input()
  gate = str(gate)

  flag_gate = 0
  if gate == "3塁側":
    flag_gate = 1
  if flag_gate == 0:  #1塁側
    print("1，2ゲートで検温を行ってください")
  else:               #3塁側
    print("3,4ゲートで検温を行ってください")
    
#検温    
  print("体温を入力してください（34.1℃～42℃）")
  t_list = []
  temp = input()
  temp = float(temp)
  t_list.append(temp)
  flag_fever = 0
  flag_error = 0
  if temp <= 34 or temp >= 42:
      flag_error = 1
  if  temp >= 37.5:                           #37.5℃以上入場不可
     flag_fever = 1
  if flag_error == 1:
    print("入力範囲外です。もう一度並び直してください")
    continue
  if flag_error == 0:
    if flag_fever == 0:
      print("手荷物検査を行ってください")
    if flag_fever == 1:
       print("発熱があるので入場できません")
       continue
       
#手荷物検査
  if flag_error == 0 and flag_fever == 0:
    print("手荷物にビン、カン、600mlを超えるペットボトル、アルコール等があるか選択してください")
    ban_list = ["ビン","カン","600mlを超えるペットボトル","アルコール","なし"]
    ban_num = len(ban_list)
    ban_id = [0,1,2,3,4]
  for i in range(0,ban_num):
    print(ban_id[i],ban_list[i])
  if flag_error == 0 and flag_fever == 0:    
    ban = input()
    ban = int(ban)

  flag_ban = 0
  if flag_error == 0 and flag_fever == 0:
    if ban == 4:
      flag_ban =1
    if flag_ban == 0:
      print("持ち込み禁止物があるので入場できません")
      continue

#チケット、通路確認
  if flag_ban == 1:
    print("チケット確認を行ってください")
    print("チケットに記載されている座席番号を入力してください。(1～250)")
  if gate == "1塁側":
    seat_number = input()
    seat_number = float(seat_number)
   
    if seat_number >=225 and seat_number <=250:
      print("101通路から入ってください")
    elif seat_number >=200 and seat_number <225:
      print("102通路から入ってください")
    elif seat_number >=175 and seat_number <200:
      print("103通路から入ってください")
    elif seat_number >=150 and seat_number <175:
      print("104通路から入ってください")
    elif seat_number >=125 and seat_number <150:
      print("105通路から入ってください")
    elif seat_number >=100 and seat_number <125:
      print("106通路から入ってください")
    elif seat_number >=75 and seat_number <100:
      print("107通路から入ってください")
    elif seat_number >=50 and seat_number <75:
      print("108通路から入ってください")
    elif seat_number >=25 and seat_number <50:
      print("109通路から入ってください")
    elif seat_number >=1 and seat_number <25:
      print("110通路から入ってください")
      
  if gate == "3塁側":
    seat_number = input()
    seat_number = float(seat_number)
    
    if seat_number >=225 and seat_number <=250:
      print("111通路から入ってください")
    elif seat_number >=200 and seat_number <225:
      print("112通路から入ってください")
    elif seat_number >=175 and seat_number <200:
      print("113通路から入ってください")
    elif seat_number >=150 and seat_number <175:
      print("114通路から入ってください")
    elif seat_number >=125 and seat_number <150:
      print("115通路から入ってください")
    elif seat_number >=100 and seat_number <125:
      print("116通路から入ってください")
    elif seat_number >=75 and seat_number <100:
      print("117通路から入ってください")
    elif seat_number >=50 and seat_number <75:
      print("118通路から入ってください")
    elif seat_number >=25 and seat_number <50:
      print("119通路から入ってください")
    elif seat_number >=1 and seat_number <25:
      print("120通路から入ってください")


#座席案内
  print("列番号を入力してください(1～20)")
  if gate == "1塁側":
    line_number = input()
    line_number = float(line_number)
    if line_number >= 1 and line_number <= 10:
      print("通路から入って左前方に座席があります。")
    elif line_number >= 11 and line_number <= 20:
      print("通路から入って左後方に座席があります。")
  if gate == "3塁側":
    line_number = input()
    line_number = float(line_number)
    if line_number >= 1 and line_number <= 10:
      print("通路から入って右前方に座席があります。")
    elif line_number >= 11 and line_number <= 20:
      print("通路から入って右後方に座席があります。")
