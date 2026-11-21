with open('data.csv', 'w') as f:
    for i in range(50):
        f.write(f"{i},{i**2}\n")