cd C:\Program Files\Wireshark

tshark -f "ip dst host not 192.168.137.1" -i "WLAN" -w E:\\www\\mua_live_spider\\test.pcap