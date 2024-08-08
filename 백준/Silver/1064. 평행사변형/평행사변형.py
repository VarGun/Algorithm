def calculate_lengths(x1, y1, x2, y2, x3, y3):
    length_ab = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    length_ac = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    length_bc = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    return length_ab, length_ac, length_bc

def check_collinear(x1, y1, x2, y2, x3, y3):
    return (x1 - x2) * (y1 - y3) == (y1 - y2) * (x1 - x3)

def main():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    
    if check_collinear(x1, y1, x2, y2, x3, y3):
        print(-1.0)
        return
    
    length_ab, length_ac, length_bc = calculate_lengths(x1, y1, x2, y2, x3, y3)
    lengths = [length_ab + length_ac, length_ab + length_bc, length_ac + length_bc]
    result = max(lengths) - min(lengths)
    
    print(2 * result)

if __name__ == "__main__":
    main()
