import pytest
import numpy as np
import psutil
import os
from matrix_multiplication import matrix_multiplication

# Function to generate random matrix of a certain size
def generate_random_matrix(size):
    return np.random.randint(0, 10, (size, size)).tolist()

# Function to obtain memory usage
def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)

def get_cpu_usage():
    process = psutil.Process(os.getpid())
    return process.cpu_percent(interval=1)

@pytest.mark.parametrize("size", [10, 100, 500, 1000])
def test_basic_matrix_multiplication(benchmark, size):
    A = generate_random_matrix(size)
    B = generate_random_matrix(size)

    memory_before = get_memory_usage()
    cpu_before = get_cpu_usage()
    print(f"Uso de memoria antes del benchmark para {size}x{size}: {memory_before:.2f} MB")
    print(f"Uso de CPU antes del benchmark para {size}x{size}: {cpu_before}%")

    result = benchmark.pedantic(matrix_multiplication,
                                args=(A, B),
                                rounds=1,
                                warmup_rounds=2,
                                iterations=5)


    memory_after = get_memory_usage()
    cpu_after = get_cpu_usage()

    print(f"Uso de memoria después del benchmark para {size}x{size}: {memory_after:.2f} MB")
    print(f"Uso de CPU después del benchmark para {size}x{size}: {cpu_after:.2f}%")


    memory_used = memory_after - memory_before
    cpu_used = cpu_after - cpu_before
    print(f"Memoria utilizada durante el benchmark para {size}x{size}: {memory_used:.2f} MB")
    print(f"CPU utilizada durante el benchmark para {size}x{size}: {cpu_used:.2f}%")

    assert len(result) == size
    assert len(result[0]) == size
