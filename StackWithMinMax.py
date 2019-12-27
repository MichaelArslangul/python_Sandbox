class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.min_max = []

    def peek(self):
		print(self.stack[-1])

    def pop(self):
		n = len(self.stack)
		if n > 0:
			del self.min_max[-1]
			return self.stack.pop(len(self.stack) - 1)
		else:
			return None

    def push(self, number):
		self.stack.append(number)
		if len(self.stack) == 0:
			self.min_max = [number, number]
		else:
			_min = min(number, self.min_max(len(self.min_max) - 1)[0])
			_max = max(number, self.min_max(len(self.min_max) - 1)[1])
			self.min_max.append([_min, _max])

    def getMin(self):
		return self.min_max[-1][0]

    def getMax(self):
		return self.min_max[-1][1]
