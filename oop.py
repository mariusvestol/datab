class Pawn:
	move = 2
	def __init__(self, color, num):
		self.color = color
		self.num = num

p1 = Pawn("white",3)

print(p1.move)
print(p1.color)

"class navn bruker stor bokstav"