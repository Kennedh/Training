import speedtest

teste = speedtest.Speedtest()

print("Escolhendo melhor servidor...\n")
teste.get_best_server()

print("Testando download...")
down_bit = teste.download()

print("Testando upload...\n")
upload_bit = teste.upload()

down = down_bit / 1000000
upload = upload_bit / 1000000

print(f"Download speed: {down:.2f} Mbps")
print(f"Upload speed: {upload:.2f} Mbps")
