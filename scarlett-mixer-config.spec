Name:           scarlett-mixer-config
Version:        0.1
Release:        1%{?dist}
Summary:        Configure snd_usb_audio for Focusrite Scarlett 2nd/3rd gen devices

License:        MIT
URL:            https://www.kernel.org

Requires:       kernel >= 5.14.0

%description
This sets the options needed in /etc/modprobe.d/scarlett-mixer.conf to enable
the mixer devices to be initialized. In combination with alsa-scarlett-gui,
this enables to you configure hardware mixing and routing of the many PCM
devices provided by the Focusrite Scarlett series of audio interfaces.


%build
cat > scarlett-mixer.conf <<EOF
# Scarlett 18i8 gen 2
options snd_usb_audio vid=0x1235 pid=0x8204 device_setup=1
EOF

%install
install -m 644 scarlett-mixer.conf %{_sysconfdir}/modprobe.d/scarlett-mixer.conf

%files
%{_sysconfdir}/modprobe.d/scarlett-mixer.conf

%changelog
* Wed Apr 05 2023 Patrick
- 
