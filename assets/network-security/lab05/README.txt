DNS investigation lab 05 / version 1

All data is original synthetic training data, generated offline. No real traffic was captured or sent. Documentation IPs and example domains only.

Policy: employee endpoints use 192.0.2.53 only. The forwarding resolver may use 198.51.100.53 as upstream.

dns-client.pcap: client-side synthetic Ethernet/IPv4 traffic, 46 frames; UDP and TCP DNS.
dns-upstream.pcap: separate upstream observation, 4 frames, not the same sensor.
packets.csv: independently decoded packet fields from dns-client.pcap; not TShark output.
transactions.csv: query-row pairing by transport/address/port/ID/question; repeated unanswered rows retained.
analysis-results.json: measured counts from file decoding.
endpoint-events.csv, asset-inventory.csv, connection-events.csv: independent fictional context, not measured host telemetry.

Times are UTC. The interval is 2026-11-02T00:00:00Z through 00:02:30.170000Z. Two unanswered query rows are intentional. TC=1 followed by TCP is intentional. The IPv6 address is an AAAA answer transported over IPv4; no IPv6 packet exists in this lab. No DoH/DoT/DoQ or malicious code exists. TXT values are inert training markers.

Open PCAPs locally in Wireshark; do not replay them or resolve the names. All generated files are educational examples, not original vendor workbook materials.
