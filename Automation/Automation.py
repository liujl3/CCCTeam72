import os
import pexpect
import sys
import time
import logging

if __name__ == "__main__":
"""
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                        level=logging.INFO)
    logging.info('Start to build Openstack instance:')

    process = pexpect.spawn('sh ./script_os.sh')
    process.logfile_read = sys.stdout.buffer
    process.expect(
        'Please enter your OpenStack Password for project unimelb-comp90024-team-72 as user haoyu.zhang@student.unimelb.edu.au:')
    process.sendline('YTljYzQzZTM1OTkwNjY4')
    i = process.expect('BECOME password:')
    process.sendline('9588')
    process.expect(pexpect.EOF, timeout=300)
"""


    logging.info('Waiting for setting up instance')
    time.sleep(200)

    for name in ['WebServer', 'CouchDB', 'Harvest','DataAnalysis']:
        logging.info('Start to build ' + name +':')
        pexpect.run('ansible-playbook -i hosts -u ubuntu --key-file=CCC.pem Automation_'+ name +'.yml',
                    events={'Are you sure you want to continue connecting (yes/no)?': 'yes\n'},
                    logfile=sys.stdout.buffer, timeout=1000)