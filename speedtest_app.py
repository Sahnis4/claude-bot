import speedtest

def run_speed_test():
    st = speedtest.Speedtest()

    # Get best server based on ping
    st.get_best_server()

    # Run tests
    ping = st.results.ping
    download = st.download() / 1_000_000   # convert to Mbps
    upload = st.upload() / 1_000_000       # convert to Mbps

    # Print results
    print(f"Ping: {ping:.2f} ms")
    print(f"Download: {download:.2f} Mbps")
    print(f"Upload: {upload:.2f} Mbps")

if __name__ == "__main__":
    run_speed_test()
