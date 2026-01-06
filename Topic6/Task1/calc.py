import operations
import logging

# Налаштування логування: запис у файл calc.log
logging.basicConfig(
    filename='topic6/Task1/calc.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

def main():
    try:
        a, b, op = operations.get_data()
        result = operations.execute_operation(a, b, op)
        
        # Логування введених даних, операції та результату 
        log_message = f"Input: a={a}, b={b} | Operation: {op} | Result: {result}"
        logging.info(log_message)
        
        print(f"Result: {result}")
        
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()