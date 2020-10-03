#!/usr/bin/python3
#date: 02/10/2020

'''
N1, N2, N3, N4
2, 3, 4 e 1
'''

N1, N2, N3, N4 = [float(notas) for notas in input().split()]
P1, P2, P3, P4 = 2.0, 3.0, 4.0, 1.0

mediapond = ((N1*P1) + (N2*P2) + (N3*P3) + (N4*P4)) / (P1+P2+P3+P4)
if ((mediapond >= 5.0) and (mediapond <= 6.9)):
	exam_score = [float(score) for score in input().split()]
	#substitua todos os exam_score subsequentes pelo indice unitário.
#exam_score = [float(score) for score in input().split if mediapond >= 5.0 and mediapond <= 6.9]
# 2.0 6.5 4.0 9.0
#print(mediapond)
#print(mediapond >= 5.0 and mediapond <= 6.9)
#print([exam_score == False])

media_final = 0.0



print("Media: {:.1f}".format(mediapond))
if mediapond >= 7.0:
	print("Aluno aprovado.")
elif mediapond < 5.0:
	print("Aluno reprovado.")
elif mediapond >= 5.0 and mediapond <= 6.9:#mediapond <=6.9:# or mediapond >=5.0 and mediapond < 7.0:
	print("Aluno em exame.")
	print("Nota do exame: {:.1f}".format(exam_score[0]))#exam_score[0] = float(input("Nota do exame: "))
	media_final = (exam_score[0] + mediapond) / 2.0
	#print(media_final >= 5.0)
	if media_final >= 5.0:
		print("Aluno aprovado.")
		print("Media final: {:.1f}".format(media_final))#:.1f
	elif media_final <= 4.9 or media_final < 5.0:
		print("Aluno reprovado.")
		print("Media final: {:.1f}".format(media_final))#:.1f


