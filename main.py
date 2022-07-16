# import speedtest

# test = speedtest.Speedtest()

# print("Loading server list ...")
# test.get_servers()  # -> get list of servers
# best = test.get_best_server()  # -> choose best server
# print("Choosing best server...")

# print(best)

# print(f"Found: {best['host']} located in {best['country']}")

# print("Performing download test...")
# download_result = test.download()
# print("Performing upload test...")
# upload_result = test.upload()
# ping_result = test.results.ping

# print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
# print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
# print(ping_result)
import speedtest

test = speedtest.Speedtest()

# test.get_servers()  # -> get list of servers
# best = test.get_best_server()  # -> choose best server
download_result = test.download() / 1024 / 1024
upload_result = test.upload() / 1024 / 1024
ping_result = test.results.ping
download_result = round(download_result, 2)
upload_result = round(upload_result, 2)
result = {"download_result": download_result, "upload_result": upload_result, "ping_result": ping_result}
print(result)
