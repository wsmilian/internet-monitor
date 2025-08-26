import speedtest


def main():
    print("Initializing speed test...")
    st = speedtest.Speedtest()
    print("Finding best server...")
    st.get_best_server()
    print(f"Best server: {st.results.server['host']} ({st.results.server['name']}, {st.results.server['country']})\n")

    print("Testing download speed...")
    download = st.download()
    print("Testing upload speed...")
    upload = st.upload()
    ping = st.results.ping

    print(f"Ping: {ping:.2f} ms")
    print(f"Download speed: {download / 1_000_000:.2f} Mbps")
    print(f"Upload speed: {upload / 1_000_000:.2f} Mbps")


if __name__ == "__main__":
    main()
