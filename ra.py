import tkinter as tk
import threading
import speedtest

def start_test():
    result_label.config(text="Testing... Please wait")

    def run():
        st = speedtest.Speedtest()
        st.get_best_server()

        ping = st.results.ping
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000

        result = (
            f"Ping: {ping:.2f} ms\n"
            f"Download: {download:.2f} Mbps\n"
            f"Upload: {upload:.2f} Mbps"
        )

        result_label.config(text=result)

    threading.Thread(target=run).start()

root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("350x250")

title = tk.Label(root, text="Internet Speed Test", font=("Arial", 16))
title.pack(pady=10)

btn = tk.Button(root, text="Start Test", command=start_test)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()