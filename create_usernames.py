def create_usernames():
	with open('input_file.txt','r') as file:
		users={}
		for i,line in enumerate(file):
			line= line.strip()
			col = line.split(' ')
			username=(col[0][0] + col[1]).lower()
			if i == 0:
				username= 'Username'
			elif username not in users:
				users[username] =1
			else:
				users[username] +=1
				username = username +str(users[username])
			with open('output_file.txt', 'a') as w:
				w.writelines(line + ' '+ username + '\n')
			print(users)
create_usernames()