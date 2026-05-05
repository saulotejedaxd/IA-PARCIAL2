"""
32 - Funciones de Activacion
Introducen no linealidad. Aqui: escalon, sigmoide, tanh, ReLU,
LeakyReLU y Softmax.
"""
import math


def escalon(x): return 1 if x >= 0 else 0
def sigmoide(x): return 1 / (1 + math.exp(-x))
def tanh(x): return math.tanh(x)
def relu(x): return max(0.0, x)
def leaky_relu(x, alpha=0.01): return x if x > 0 else alpha * x


def softmax(xs):
    m = max(xs)
    e = [math.exp(x - m) for x in xs]
    z = sum(e)
    return [v / z for v in e]


if __name__ == "__main__":
    for x in [-2, -0.5, 0, 0.5, 2]:
        print(f"x={x}  esc={escalon(x)}  sig={sigmoide(x):.3f}  tanh={tanh(x):.3f}  relu={relu(x):.3f}  lrelu={leaky_relu(x):.3f}")
    print("softmax([1, 2, 3]):", [round(p, 3) for p in softmax([1, 2, 3])])
