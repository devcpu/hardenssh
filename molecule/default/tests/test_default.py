import os,  pytest

import testinfra.utils.ansible_runner

if 'MOLECULE_INVENTORY_FILE' in os.environ:
    testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sshd_config(host):
    cmd = host.run('/usr/sbin/sshd -t')
    assert cmd.rc == 0

    f = host.file('/etc/ssh/sshd_config')
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o644'
    assert f.contains('AllowUsers georgos')
    
    sshd_config = host.check_output('/usr/sbin/sshd -T')
    assert 'port 8022' in sshd_config
    assert 'hostbasedauthentication no' in sshd_config
    assert 'pubkeyauthentication yes' in sshd_config
    assert 'challengeresponseauthentication yes' in sshd_config
    assert 'x11forwarding no' in sshd_config
    assert 'strictmodes yes' in sshd_config
    assert 'usedns no' in sshd_config
    assert 'allowtcpforwarding yes' in sshd_config
    assert 'exposeauthinfo no' in sshd_config
    assert 'authenticationmethods publickey,keyboard-interactive' in sshd_config
    assert 'permitrootlogin no' in sshd_config
    assert 'permitemptypasswords no' in sshd_config
    assert 'passwordauthentication no' in sshd_config
    assert 'allowusers georgos' in sshd_config
    assert 'maxauthtries 3' in sshd_config
    assert 'maxsessions 3' in sshd_config
    assert 'tcpkeepalive yes' in sshd_config

# def test_user_georgos(host):
#     u = host.user('georgos')
#     assert u.exists


    
    

