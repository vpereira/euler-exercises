import pyopencl as cl
import numpy as np

"""
	If we list all the natural numbers below 10 that are multiples of 3 or 5,
	we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
"""


ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

kernel_source = """
__kernel void mark_multiples(__global int *out) {
    int i = get_global_id(0);
    if ((i % 3 == 0) || (i % 5 == 0)) {
        out[i] = i;
    } else {
        out[i] = 0;
    }
}
"""

program = cl.Program(ctx, kernel_source).build()

# 4. Create a buffer on the device to store results for 0..999
N = 1000
mf = cl.mem_flags
output_buffer = cl.Buffer(ctx, mf.WRITE_ONLY, size=N * np.dtype(np.int32).itemsize)

mark_multiples_kernel = program.mark_multiples
mark_multiples_kernel.set_arg(0, output_buffer)
cl.enqueue_nd_range_kernel(queue, mark_multiples_kernel, (N,), None)

# 6. Read the results back to host memory
result_host = np.empty(N, dtype=np.int32)
cl.enqueue_copy(queue, result_host, output_buffer)

answer = np.sum(result_host)

print("Sum of multiples of 3 or 5 below 1000 is:", answer) # 233168

