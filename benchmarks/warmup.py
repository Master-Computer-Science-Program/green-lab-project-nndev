import time
import math

def cpu_intensive_task(duration_seconds):
    """Perform CPU-intensive calculations for the specified duration."""
    end_time = time.time() + duration_seconds
    counter = 0
    
    while time.time() < end_time:
        # Perform computationally expensive operations
        for i in range(1000):
            math.sqrt(counter * math.pi)
            math.sin(counter / 1000.0)
            math.cos(counter / 1000.0)
            counter += 1


def warmup_cpu(duration_minutes=2):
    """
    Warm up the CPU by running intensive tasks.
    
    Args:
        duration_minutes (int): How long to run the warmup (default: 2 minutes)
    """
    duration_seconds = duration_minutes * 60
    
    print(f"Starting CPU warmup for {duration_minutes} minutes...")
    
    start_time = time.time()
    
    cpu_intensive_task(duration_seconds)
    
    elapsed_time = time.time() - start_time
    print(f"CPU warmup completed in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    warmup_cpu()
