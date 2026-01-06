import operations

def main():
    a, b, op = operations.get_data()
    result = operations.execute_operation(a, b, op)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()