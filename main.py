import ast
import random
import math
class thewholething():
    def __init__(self,file):
        self.weight = random.random()
        self.bais = random.random()
        self.cost = 0
        try:txtfile = open(file,'r')
        except:
            print("Error: " + 'unable to locate file')
            exit()
        try:self.inputdata = ast.literal_eval(txtfile.read())
        except:
            print("Error: " + 'invalid data format (code 1)')
            exit()
        txtfile.close()
        try:
            for i in self.inputdata:
                tester = float(i[0])
                tester = float(i[0])
        except:
            print("Error: " + "invalid data format (code 0)")
            exit()
    def get_cost(self):
        self.cost = 0
        for i in self.inputdata:
            x = float(i[0])
            y = float(i[1])
            localperdiction = self.weight * x + self.bais
            self.cost += (y - localperdiction)**2
        return self.cost
    def get_gradient(self):
        n = len(self.inputdata)
        dw = 0
        db = 0
        for i in range(0, n):
            x = float(self.inputdata[i][0])
            y = float(self.inputdata[i][1])
            dw += (1 / n) * -2 * x * (y - self.weight * x - self.bais)
            db += (1 / n) * -2 * (y - self.weight * x - self.bais)
        self.gradients = [dw, db]
        return self.gradients
    def train(self, learningrate,step):
        for i in range(step):
            self.get_gradient()
            self.weight -= (self.gradients[0] * learningrate)
            self.bais -= (self.gradients[1] * learningrate)
            print("iteration", i, ": ", "cost: ", self.get_cost(), 'weight,bais: ', self.weight, self.bais, 'gradients: ', self.gradients)

test = thewholething('data.txt')
print(test.get_cost())
print('training')
test.train(0.7,10)