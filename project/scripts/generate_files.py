import os

# Tamanhos em bytes
file_sizes = [8, 64, 512, 4096, 32768, 262144, 2097152]

output_dir = "../data"

os.makedirs(output_dir, exist_ok=True)
counter = 0

for size in file_sizes:
    filename = f"{output_dir}/file_{size}B.bin"
    counter += 1
    # Dados aleatórios seguros
    data = os.urandom(size)
    
    with open(filename, "wb") as f:
        f.write(data)
    
    print(f"{counter}º Ficheiro criado: {filename} ({size} bytes)")

print("\n--- Todos os ficheiros foram gerados com sucesso. ---")