import pyopencl as cl
import numpy as np

# OpenCL kernel code to calculate Fibonacci numbers
kernel_code = """
__kernel void fibonacci(__global int* fib_sequence, const unsigned int n) {
    int id = get_global_id(0);
    if (id < n) {
        if (id == 0) {
            fib_sequence[id] = 1;
        } else if (id == 1) {
            fib_sequence[id] = 2;
        } else {
            fib_sequence[id] = fib_sequence[id - 1] + fib_sequence[id - 2];
        }
    }
}
"""


ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# Create memory buffers
n = 33  # Number of Fibonacci numbers to generate (safe number for 4 million range)
fib_sequence = np.zeros(n, dtype=np.int32)

fib_buffer = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, fib_sequence.nbytes)

program = cl.Program(ctx, kernel_code).build()

program.fibonacci(queue, fib_sequence.shape, None, fib_buffer, np.uint32(n))

# Read the results back into host memory
cl.enqueue_copy(queue, fib_sequence, fib_buffer).wait()

even_fib_sum = np.sum(fib_sequence[fib_sequence < 4000000][fib_sequence % 2 == 0])

print(f"Sum of even Fibonacci numbers below 4 million: {even_fib_sum}") # 4

