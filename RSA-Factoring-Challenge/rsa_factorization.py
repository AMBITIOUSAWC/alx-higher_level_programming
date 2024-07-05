import math
import sys
import time

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize_rsa_number(n):
    """Find the prime factors p and q of RSA number n."""
    if n <= 1:
        return None, None

    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            p = i
            q = n // i
            if is_prime(p) and is_prime(q):
                return p, q

    return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 rsa_factorization.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            n = int(file.read().strip())
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    start_time = time.time()
    p, q = factorize_rsa_number(n)
    end_time = time.time()

    if p and q:
        print(f"Found prime factors: p = {p}, q = {q}")
    else:
        print("Prime factors not found.")

    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
