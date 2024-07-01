import speedtest
from func.Speak import speak


# Create a Speedtest object
def raftaar():
    speed_test = speedtest.Speedtest()

    print("Testing internet speed...")
    speak("Just wait for sometime. ")

    # Download speed test
    download_speed = speed_test.download()

    # Upload speed test
    upload_speed = speed_test.upload()

    # Convert speeds to Mbps (megabits per second)
    download_mbps = download_speed / 1024 / 1024
    upload_mbps = upload_speed / 1024 / 1024

    # Print results with formatting
    print(f"Download speed: {download_mbps:.2f} Mbps")
    print(f"Upload speed: {upload_mbps:.2f} Mbps")
    speak("This is the result. ")
    print("Speed test completed!")

