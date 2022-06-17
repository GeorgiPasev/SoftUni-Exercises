volume_pool_liters = int(input())
debit_first_pipe_per_h = int(input())
debit_second_pipe_per_h = int(input())
worker_out_hours = float(input())

first_l = debit_first_pipe_per_h * worker_out_hours
second_l = debit_second_pipe_per_h * worker_out_hours
total_liters = first_l + second_l


if total_liters < volume_pool_liters:
    percent_first = first_l / volume_pool_liters * 100
    percent_second = second_l / volume_pool_liters * 100
    percent_full = total_liters / volume_pool_liters * 100
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_first:.2f}%. Pipe 2: {percent_second:.2f}%.")
else:
    diff = total_liters - volume_pool_liters
    print(f"For {worker_out_hours:.2f} hours the pool overflows with {diff:.2f} liters.")