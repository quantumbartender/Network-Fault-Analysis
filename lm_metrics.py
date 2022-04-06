#!/home/gautam-admin/anaconda3/bin/python
o = open('Desktop/metric_test.txt', 'w')

from linux_metrics import cpu_stat
import linux_metrics as lm
o2 = open('Desktop/metric_tester.txt', 'w')
o2.close()
# cpu
o.write('procs running: %d' % cpu_stat.procs_running())
o.write("\n")
cpu_pcts = cpu_stat.cpu_percents(sample_duration=1)
o.write('cpu utilization: %.2f%%' % (100 - cpu_pcts['idle']))
o.write("\n")
# disk
o.write('disk busy: %s%%' % lm.disk_stat.disk_busy('sda', sample_duration=1))
o.write("\n")
r, w = lm.disk_stat.disk_reads_writes('sda1')
o.write('disk reads: %s' % r)
o.write("\n")
o.write('disk writes: %s' % w)
o.write("\n")

# # memory
used, total, _, _, _, _ = lm.mem_stat.mem_stats()
o.write('mem used: %s' % used)
o.write("\n")
o.write('mem total: %s' % total)
o.write("\n")

# network
# rx_bits, tx_bits = lm.net_stat.rx_tx_bits('enp4s0')
# o.write('net bits received: %s' % rx_bits)
# o.write("\n")
# o.write('net bits sent: %s' % tx_bits)
# o.write("\n")

o.close()